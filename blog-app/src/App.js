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
    CookingTime: ''
  });
  
  let updated_data = null;
  let selected_row_data = null;
  let add_index;
  const fetchCookingdata = async (buttonValue) => {

      let response;
      if (buttonValue === 'getById') {
        response = await api.get(`/CookingData/GetID${formData.ID}`);
      }
      else if (buttonValue === 'getAllRecipes') {
        response = await api.get('/CookingData/GetData');
      }
      else if (buttonValue === 'getByCategory') {
        response = await api.get(`/CookingData/GetRecipe_UsingCategory${formData.Category}`);
      }
      else if (buttonValue === 'getByCookingTime') {
        response = await api.get(`/CookingData/GetRecipe_UsingCookingTime${formData.CookingTime}`);
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
      else{
        response = await api.get(`/CookingData/GetID${formData.ID}`);
      }
      setCookingdata(response.data);
    }

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

  }

  // const [rowData, setRowData] = useState([
  //   { ID: "Voyager", Title: "NASA", Ingredients: "Ingredients", CookingTime: "1977-09-05", Category: "Category", Steps: "Steps" },
  // ]);
  // const gridOptions = {rowSelection: 'multiple', pagination: true}
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

  const addItems = useCallback((addIndex) => {
    add_index =  gridRef.current.api.getSelectedRows();
    const newItems = [
      createNewRowData()
    ];
    const res = gridRef.current.api.applyTransaction({
      add: newItems,
      addIndex: addIndex
    });
  }, []);

 

  const clearData = useCallback(() => {
    const rowData = [];
    gridRef.current.api.forEachNode(function (node) {
      rowData.push(node.data);
    });
    const res = gridRef.current.api.applyTransaction({
      remove: rowData,
    });
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

          <br></br>
          
          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllRecipes')} style={{ marginRight: '15px' }}>
            Get All Recipes
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getById')} style={{ marginRight: '15px' }}>
            Get Recipe By ID
          </button> 

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCategory')} style={{ marginRight: '15px' }}>
            Get Recipes By Category
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCookingTime')} style={{ marginRight: '15px' }}>
            Get Recipes By Cooking Time
          </button>

          <br></br>

          <br></br>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('InsertData')} style={{ marginRight: '15px', backgroundColor: 'magenta'}}>
            Insert Data
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('UpdateData')} style={{ marginRight: '15px', backgroundColor: 'green'}}>
            Update Data
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('DeleteData')} style={{ marginRight: '15px', backgroundColor: 'grey'}}>
            Delete Data
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('UploadData')} style={{ marginRight: '15px', backgroundColor: 'red'}}>
            Upload Data
          </button>

        </form>

        <br></br>

        <button type='button' className='btn btn-primary' onClick={() => addItems(undefined)} style={{ marginRight: '15px' }}>Add Items</button>
        
        <button type='button' className='btn btn-primary' onClick={onRemoveSelected} style={{ marginRight: '15px' }}>Remove Selected</button>
        
        <button type='button' className='btn btn-primary' onClick={clearData}>Clear Data</button>

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
