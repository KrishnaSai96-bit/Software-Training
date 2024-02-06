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
    const [exceptionsdata, setExceptionsdata] = useState([]);
    const [formData, setFormData] = useState({
      Message_ID: '',
      Technology_Type: '',
      FileName: ''
    });
    
  let updated_data = null;
  let selected_row_data = null;
  let add_index;const fetchExceptionsdata = async (buttonValue) => {
    let response;
    if (buttonValue === 'GetData') {
      // add code here to call the appropriate get method based on the form value
    } 
    else if (buttonValue === 'getByMessageID') {
      response = await api.get(`/KnowledgeHub/GetData_Using_ID/${formData.Message_ID}`);
    } 
    else if (buttonValue === 'getByTechnologyType') {
      response = await api.get(`/KnowledgeHub/GetData_Using_Technology_Type/${formData.Technology_Type}`);
    } 
    else if (buttonValue === 'getAllData') {
      response = await api.get('/KnowledgeHub/GetData/');
    }
    else if (buttonValue === 'SaveData') {
      const selectedData = gridRef.current.api.getSelectedRows();
      for (var i = 0; i < selectedData.length; i++){
        selected_row_data = selectedData[i];
        console.log(selected_row_data);
        await api.put(`/KnowledgeHub/Update_ExceptionsData/${selected_row_data.Message_ID}`, selected_row_data);
      }
      return;
    } 
    else if (buttonValue === 'UploadData') {
      response = await api.post(`/KnowledgeHub/InsertFileData/${formData.FileName}`);
      response = await api.get('/KnowledgeHub/GetData/');
    }
    else{
      response = await api.get(`/KnowledgeHub/GetData_Using_ID/${formData.Message_ID}`);
    }
    setExceptionsdata(response.data);
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
    const handleButtonClick = async (buttonValue)  => {
      if (buttonValue === 'getByMessageID'){
          fetchExceptionsdata('getByMessageID');;
        }
        else if (buttonValue === 'getAllData') {
          fetchExceptionsdata('getAllData');
        }
        else if (buttonValue === 'getByTechnologyType') {
          fetchExceptionsdata('getByTechnologyType');
        }
        else if (buttonValue === 'UploadData') {
          fetchExceptionsdata('UploadData');
        }
        else if (buttonValue === 'SaveData') {
          fetchExceptionsdata('SaveData');
        }
    }       
    
    const [colDefs, setColDefs] = useState([
      { field: "Message_ID", editable: true, filter: true, cellDataType: 'number'},
      { field: "Technology_Type", editable: true, filter: true, cellDataType: 'string'},
      { field: "Exception_Type", editable: true, filter: true, cellDataType: 'string'},
      { field: "Exception_Title", editable: true, filter: true, cellDataType: 'string'},
      { field: "Description", editable: true, filter: true, cellDataType: 'string'},
    ]);

    const createNewRowData = () => {
      const newData = {
        Message_ID: 'ID',
        Technology_Type: 'Technology',
        Exception_Type: 'Type',
        Exception_Title: 'Title',
        Description: 'Description',
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
              Knowledge Hub
            </a>
          </div>
        </nav>
  
        <div className='container'>
          <form>

            <div className='mb-3 mt-3'>
              <label htmlFor='Message_ID' className='form-label'>
                Message_ID
              </label>
              <input type='text' className='form-control' id='Message_ID' name='Message_ID' onChange={handleInputChange} value={formData.Message_ID} style={{ width: '100px' }}/>
            </div>
            
            <div className='mb-3 mt-3'>
              <label htmlFor='Technology_Type' className='form-label'>
                Technology_Type
              </label>
              <input type='text' className='form-control' id='Technology_Type' name='Technology_Type' onChange={handleInputChange} value={formData.Technology_Type} style={{ width: '100px' }}/>
            </div>

            <div className='mb-3 mt-3'>
              <label htmlFor='FileName' className='form-label'>
                File Name
              </label>
              <input type='text' className='form-control' id='FileName' name='FileName' onChange={handleInputChange} value={formData.FileName} style={{ width: '100px' }}/>
            </div>

            <br></br>
            <br></br>
  
            <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllData')} style={{ marginRight: '15px', backgroundColor: 'Green'}}>
              Get All Data
            </button>
  
            <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByMessageID')} style={{ marginRight: '15px', backgroundColor: 'blue' }}>
              Get Data By Message_ID
            </button> 
  
            <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByTechnologyType')} style={{ marginRight: '15px', backgroundColor: 'blue' }}>
              Get Data By Technology_Type
            </button>

            <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('UploadData')} style={{ marginRight: '15px', backgroundColor: 'magenta' }}>
              Upload Data
            </button>

            <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('SaveData')} style={{ marginRight: '15px', backgroundColor: 'green'}}>
              Save Data
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
            rowData={exceptionsdata} 
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