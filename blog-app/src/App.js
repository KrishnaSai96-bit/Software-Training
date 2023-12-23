import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'

const App = () => {
  const [cookingdata, setCookingdata] = useState([]);
  const [formData, setFormData] = useState({
    ID: '',
    Title: '',
    Ingredients: '',
    CookingTime: '',
    Category: '',
    Steps: '',
  });

  // const fetchPosts = async () => {
  //   const response = await api.get('/posts/');
  //   setPosts(response.data);
  // }

  const fetchCookingdata = async () => {
    // try {
      // Add query parameter to the URL if 'id' is provided
      //const url = ID ? `/CookingData/?ID=${ID}` : '/CookingData/';
      const url = '/CookingData/GetData';
      const response = await api.get(url);
      setCookingdata(response.data);
    // } catch (error) {
    //   setError(error);
    // }
  }

  useEffect(() => {
    fetchCookingdata();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };


  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/CookingData/CreateData', formData);
    fetchCookingdata(); // re-call all posts from db
    setFormData({
      ID: '',
      Title: '',
      Ingredients: '',
      CookingTime: '',
      Category: '',
      Steps: '',
    });
  };


  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href="#">
            Cook Book
          </a>
        </div>
      </nav>

      <div className='container'>
        <form onSubmit={handleFormSubmit}>

          <div className='mb-3 mt-3'>
            <label htmlFor='ID' className='form-label'>
              ID
            </label>
            <input type='text' className='form-control' ID='ID' name='ID' onChange={handleInputChange} value={formData.ID}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Title' className='form-label'>
              Title
            </label>
            <input type='text' className='form-control' id='Title' name='Title' onChange={handleInputChange} value={formData.Title}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Ingredients' className='form-label'>
            Ingredients
            </label>
            <input type='text' className='form-control' id='Ingredients' name='Ingredients' onChange={handleInputChange} value={formData.Ingredients}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='CookingTime' className='form-label'>
            CookingTime
            </label>
            <input type='text' className='form-control' id='CookingTime' name='CookingTime' onChange={handleInputChange} value={formData.CookingTime}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Category' className='form-label'>
            Category
            </label>
            <input type='text' className='form-control' id='Category' name='Category' onChange={handleInputChange} value={formData.Category}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='Steps' className='form-label'>
            Steps
            </label>
            <input type='text' className='form-control' id='Steps' name='Steps' onChange={handleInputChange} value={formData.Steps}/>
          </div>

          <button type='submit' className='btn btn-primary'>
            Submit
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
