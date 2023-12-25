import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'

const App = () => {
  const [cookingdata, setCookingdata] = useState([]);
  const [formData, setFormData] = useState({
    ID: ''
  });

  // const fetchPosts = async () => {
  //   const response = await api.get('/posts/');
  //   setPosts(response.data);
  // }

  const fetchCookingdata = async (buttonValue) => {
    // try {
      // Add query parameter to the URL if 'id' is provided
      //const url = '/CookingData/GetData';
      //const response = await api.get(url);
      let response;
      if (buttonValue === 'getById') {
        response = await api.get(`/CookingData/GetID${formData.ID}`);
      }
      else if (buttonValue === 'getAllRecipes') {
        response = await api.get('/CookingData/GetData');
    }
      setCookingdata(response.data);
    // } catch (error) {
    //   setError(error);
    // }
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
  }
  

  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href="#">
            Cook Book - RECIEP BY ID
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

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getById')}>
            Get Recipe By ID
          </button> 

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllRecipes')}>
            Get All Recipes
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
