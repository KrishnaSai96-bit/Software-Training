import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'
import { AgGridReact } from 'ag-grid-react'; // React Grid Logic
import "ag-grid-community/styles/ag-grid.css"; // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css"; // Theme

const App = () => {
  const [cookingdata, setCookingdata] = useState([]);
  const [formData, setFormData] = useState({
    ID: '',
    Category: ''
  });

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
    
      setCookingdata(response.data);
    }

  useEffect(() => {
    //fetchCookingdata();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  
  };

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

  }

  // const [rowData, setRowData] = useState([
  //   { ID: "Voyager", Title: "NASA", Ingredients: "Ingredients", CookingTime: "1977-09-05", Category: "Category", Steps: "Steps" },
  // ]);
  
  const [colDefs, setColDefs] = useState([
    { field: "ID", editable: true},
    { field: "Title", editable: true},
    { field: "Ingredients", editable: true},
    { field: "CookingTime", editable: true},
    { field: "Category", editable: true},
    { field: "Steps",editable: true}
  ]);

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

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('SaveData')} style={{ marginRight: '15px', backgroundColor: 'green'}}>
            Save Data
          </button>

        </form>

        <br></br>

        <div className="ag-theme-quartz" style={{ height: 300}}>
          <AgGridReact rowData={cookingdata} columnDefs={colDefs}/>
        </div>
      </div>
    </div>
  )
}


export default App;
