'use strict';

import React, {
  useState, 
  useEffect,
  useCallback,
  useMemo,
  useRef,
  StrictMode,
} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'
import { AgGridReact } from 'ag-grid-react'; // React Grid Logic
import "ag-grid-community/styles/ag-grid.css"; // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css"; // Theme

const App = () => {
  const gridRef = useRef();
  const [cookingdata, setCookingdata] = useState([]);
  const [formData, setFormData] = useState({
    ID: '',
    Category: '',
    CookingTime: '',
    FileName: ''
  });
  
  let updated_data = null;
  let selected_row_data = null;
  let add_index;
  const fetchCookingdata = async (buttonValue) => {
      let response;
      if (buttonValue === 'GetData') {
        // add code here to call the appropriate get method based on the form value
      } 
      else if (buttonValue === 'getById') {
        response = await api.get(`/CookingData/GetID${formData.ID}`);
      } 
      else if (buttonValue === 'getByCategory') {
        response = await api.get(`/CookingData/GetRecipe_UsingCategory${formData.Category}`);
      } 
      else if (buttonValue === 'getByCookingTime') {
        response = await api.get(`/CookingData/GetRecipe_UsingCookingTime${formData.CookingTime}`);
      }
      else if (buttonValue === 'getAllRecipes') {
        response = await api.get('/CookingData/GetData');
      } 
      else if (buttonValue === 'SaveData') {
        const selectedData = gridRef.current.api.getSelectedRows();
        for (var i = 0; i < selectedData.length; i++){
          selected_row_data = selectedData[i];
          console.log(selected_row_data);
          await api.put(`/CookingData/Update_CookingData/${selected_row_data.ID}`, selected_row_data);
        }
        return;
      }
      else if (buttonValue === 'UploadData') {
        response = await api.post(`/CookingData/InsertFileData/${formData.FileName}`);
        response = await api.get('/CookingData/GetData');
      }
      else{
        response = await api.get(`/CookingData/GetID${formData.ID}`);
      }
      setCookingdata(response.data);
    }
//RecipeDataSet1.csv
  useEffect(() => {
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  
  };

  // const handleCellValueChanged = async (params) => {
  //   updated_data = params.data;
  //   console.log(updated_data);
  // };

  const handleButtonClick = async (buttonValue)  => {
    if (buttonValue === 'getById'){
        fetchCookingdata('getById');
      }

      else if (buttonValue === 'getAllRecipes') {
        fetchCookingdata('getAllRecipes');
      }

      else if (buttonValue === 'getByCategory') {
        fetchCookingdata('getByCategory');
      }

      else if (buttonValue === 'getByCookingTime') {
        fetchCookingdata('getByCookingTime');
      }

      else if (buttonValue === 'SaveData') {
        fetchCookingdata('SaveData');
      }

      else if (buttonValue === 'UploadData') {
        fetchCookingdata('UploadData');
      }

  }
  
  const [colDefs, setColDefs] = useState([
    { field: "ID", editable: true, filter: true, pinned: 'left', cellDataType: 'number'},
    { field: "Title", editable: true, filter: true, pinned: 'left', cellDataType: 'text'},
    { field: "Ingredients", editable: true, filter: true, cellDataType: 'text'},
    { field: "CookingTime", editable: true, filter: true, cellDataType: 'number'},
    { field: "Category", editable: true, filter: true, cellDataType: 'text'},
    { field: "Steps",editable: true, filter: true, cellDataType: 'text'}
  ]);

  const createNewRowData = () => {
    const newData = {
      ID: 1,
      Title: 'Dosa',
      Ingredients: 'Dosa',
      CookingTime: 30,
      Category: 'Dosa',
      Steps: 'Dosa'
    };
    return newData;
  }

  const onRemoveSelected = useCallback(() => {
    const selectedData = gridRef.current.api.getSelectedRows();
    const res = gridRef.current.api.applyTransaction({remove: selectedData});
  }, []);

const addSingleItem = useCallback(() => {
  const newItem = createNewRowData();
  const res = gridRef.current.api.applyTransaction({
    add: [newItem],
  });
}, []);

const addMultipleItems = useCallback((addIndex) => {
  const newItems = [
    createNewRowData(),
    createNewRowData(),
    // Add more rows as needed
  ];
  const res = gridRef.current.api.applyTransaction({
    add: newItems,
    addIndex: addIndex,
  });
}, []);

  const clearData = useCallback(() => {
    const selectedData = gridRef.current.api.getSelectedRows();
  
    if (selectedData.length > 0) {
      const res = gridRef.current.api.applyTransaction({
        remove: selectedData,
      });
    } else {
      const allData = gridRef.current.api.getModel().rowsToDisplay.map((node) => node.data);
      const res = gridRef.current.api.applyTransaction({
        remove: allData,
      });
    }
  }, []);

  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href="#">
            Cook Book - RECIEPS
          </a>
        </div>
      </nav>

      <div className='container'>
        <form>

        <div className='container-fluid'>
          <a className='navbar-brand'>
            Filter By : 
          </a>
        </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='ID' className='form-label'>
              ID
            </label>
            <input type='text' className='form-control' ID='ID' name='ID' onChange={handleInputChange} value={formData.ID} style={{ width: '100px' }}/>
          </div>
          
          <div className='mb-3 mt-3'>
            <label htmlFor='Category' className='form-label'>
            Category
            </label>
            <input type='text' className='form-control' id='Category' name='Category' onChange={handleInputChange} value={formData.Category} style={{ width: '100px' }}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='CookingTime' className='form-label'>
            Cooking Time
            </label>
            <input type='text' className='form-control' id='CookingTime' name='CookingTime' onChange={handleInputChange} value={formData.CookingTime} style={{ width: '100px' }}/>
          </div>

          <div className='container-fluid'>
          <a className='navbar-brand'>
            Upload : 
          </a>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='FileName' className='form-label'>
            File Name
            </label>
            <input type='text' className='form-control' id='FileName' name='FileName' onChange={handleInputChange} value={formData.FileName} style={{ width: '100px' }}/>
          </div>

          <br></br>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('GetData')} style={{ marginRight: '15px' }}>
            Get Data
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('SaveData')} style={{ marginRight: '15px', backgroundColor: 'green'}}>
            Save Data
          </button>
        
          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('UploadData')} style={{ marginRight: '15px', backgroundColor: 'magenta' }}>
            Upload Data
          </button>

          <br></br>
          <br></br>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllRecipes')} style={{ marginRight: '15px', backgroundColor: 'gray'}}>
            Get All Recipes
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getById')} style={{ marginRight: '15px', backgroundColor: 'gray' }}>
            Get Recipe By ID
          </button> 

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCategory')} style={{ marginRight: '15px', backgroundColor: 'gray' }}>
            Get Recipes By Category
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCookingTime')} style={{ marginRight: '15px', backgroundColor: 'gray' }}>
            Get Recipes By Cooking Time
          </button>

          <br></br>
          <br></br>

          <button type='button' className='btn btn-primary' onClick={() => addSingleItem(undefined)} style={{ marginRight: '15px' }}>Add Single Item</button>

          <button type='button' className='btn btn-primary' onClick={() => addMultipleItems(undefined)} style={{ marginRight: '15px' }}>
          Add Multiple Items </button>
        
          <button type='button' className='btn btn-primary' onClick={onRemoveSelected} style={{ marginRight: '15px', backgroundColor: 'purple' }}>Remove Selected</button>

          <button type='button' className='btn btn-primary' onClick={clearData} style={{ marginRight: '15px', backgroundColor: 'red' }}>Clear Data</button>

        </form>

        <br></br>

        <div className="ag-theme-quartz" style={{ height: 500}}>
          <AgGridReact 
          ref={gridRef}
          rowData={cookingdata} 
          columnDefs={colDefs} 
          //onCellValueChanged={handleCellValueChanged}
          onClick={() => handleButtonClick('SaveData')} 
          rowSelection={'multiple'}
          pagination={true}
          />
        </div>
      </div>
    </div>
  )
}

export default App;
