import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'

const App = () => {
  const [cookingdata, setCookingdata] = useState([]);
  const [formData, setFormData] = useState({
    ID: '',
    Category: ''
  });
  const [cookingdataform4insert, setCookingdataform4insert] = useState({
    ID: '',
    Title: '',
    Ingredients: '',
    CookingTime: '',
    Category: '',
    Steps: ''
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
      else if (buttonValue === 'insertRecipe') {
        await api.post('/CookingData/CreateData', cookingdataform4insert);
        response = await api.get(`/CookingData/GetID${cookingdataform4insert.ID}`);
        setCookingdataform4insert({
          ID: '',
          Title: '',
          Ingredients: '',
          CookingTime: '',
          Category: '',
          Steps: ''
        });
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
    setCookingdataform4insert({
      ...cookingdataform4insert,
      [event.target.name]: value,
    });
  };

  // const handleFormSubmit = async (event) => {
  //   event.preventDefault();
  //   console.log('bunnu');
  //   console.log(cookingdataform4insert);
  //   await api.post('/CookingData/CreateData', cookingdataform4insert);
  //   fetchCookingdata();
  //   setCookingdataform4insert({
  //     ID: '',
  //     Title: '',
  //     Ingredients: '',
  //     CookingTime: '',
  //     Category: '',
  //     Steps: ''
  //   });
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

      else if (buttonValue === 'insertRecipe') {
        fetchCookingdata('insertRecipe');
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
            <input type='text' className='form-control' ID='ID' name='ID' onChange={handleInputChange} value={formData.ID} style={{ width: '100px' }}/>
          </div>
          
          <div className='mb-3 mt-3'>
            <label htmlFor='Category' className='form-label'>
            Category
            </label>
            <input type='text' className='form-control' id='Category' name='Category' onChange={handleInputChange} value={formData.Category} style={{ width: '100px' }}/>
          </div>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getById')} style={{ marginRight: '15px' }}>
            Get Recipe By ID
          </button> 

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getAllRecipes')} style={{ marginRight: '15px' }}>
            Get All Recipes
          </button>

          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('getByCategory')} style={{ marginRight: '15px' }}>
            Get Recipes By Category
          </button>

        </form>

        <br></br>

        <form>

          <a className='navbar-brand'>
            Insert New Recipe
          </a>

          <div className='mb-3 mt-3'>
            <label htmlFor='ID' className='form-label'>
              New ID
            </label>
            <input type='text' className='form-control' ID='ID' name='ID' onChange={handleInputChange} value={cookingdataform4insert.ID}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Title' className='form-label'>
              New Title
            </label>
            <input type='text' className='form-control' id='Title' name='Title' onChange={handleInputChange} value={cookingdataform4insert.Title}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Ingredients' className='form-label'>
            New Ingredients
            </label>
            <input type='text' className='form-control' id='Ingredients' name='Ingredients' onChange={handleInputChange} value={cookingdataform4insert.Ingredients}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='CookingTime' className='form-label'>
            New CookingTime
            </label>
            <input type='text' className='form-control' id='CookingTime' name='CookingTime' onChange={handleInputChange} value={cookingdataform4insert.CookingTime}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Category' className='form-label'>
            New Category
            </label>
            <input type='text' className='form-control' id='Category' name='Category' onChange={handleInputChange} value={cookingdataform4insert.Category}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Steps' className='form-label'>
            New Steps
            </label>
            <input type='text' className='form-control' id='Steps' name='Steps' onChange={handleInputChange} value={cookingdataform4insert.Steps}/>
          </div>
          
          <button type='button' className='btn btn-primary' onClick={() => handleButtonClick('insertRecipe')}>
           Insert Recipe
          </button>

        <br></br>

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
