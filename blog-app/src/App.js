import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'

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
    }
      setCookingdata(response.data);

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


//   const handle_GetRecipes_ByID = async (event) => {
//     //event.preventDefault();
//     fetchCookingdata('getById');
//   };

//   const handle_GetAllRecipes = async (event) => {
//     //event.preventDefault();
//     fetchCookingdata('getAllRecipes');
//   };

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
            <input type='text' className='form-control' ID='ID' name='ID' onChange={handleInputChange} value={formData.ID}/>
          </div>
          
          <div className='mb-3 mt-3'>
            <label htmlFor='Category' className='form-label'>
            Category
            </label>
            <input type='text' className='form-control' id='Category' name='Category' onChange={handleInputChange} value={formData.Category}/>
          </div>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getById')}>
            Get Recipe By ID
          </button> 

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllRecipes')}>
            Get All Recipes
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCategory')}>
            Get Recipes By Category
          </button>

        </form>

        <table className='table table-striped table-bordered table-hover'>
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Ingredients</th>
              <th>CookingTime</th>
              <th>Category</th>
              <th>Steps</th>

            </tr>
          </thead>
          <tbody>
            {cookingdata.map((CookingData) => (
              <tr key={CookingData.id}>
                <td>{CookingData.ID}</td>
                <td>{CookingData.Title}</td>
                <td>{CookingData.Ingredients}</td>
                <td>{CookingData.CookingTime}</td>
                <td>{CookingData.Category}</td>
                <td>{CookingData.Steps}</td>
              </tr>
            ))}
          </tbody>
        </table>

      </div>
    </div>
  )
}
export default App;
