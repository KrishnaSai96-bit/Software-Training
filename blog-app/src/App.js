import React, {useState, useEffect} from 'react' //useState and useEffect are hooks used to call api endpoints
import api from './api'

const App = () => {
  const [posts, setPosts] = useState([]);
  const [formData, setFormData] = useState({
    id: '',
    title: '',
    content: '',
    user_id: '',
  });

  // const fetchPosts = async () => {
  //   const response = await api.get('/posts/');
  //   setPosts(response.data);
  // }

  const fetchPosts = async (post_id = null) => {
    // try {
      // Add query parameter to the URL if 'id' is provided
      const url = post_id ? `/posts/?post_id=${post_id}` : '/posts/';
      const response = await api.get(url);
      setPosts(response.data);
    // } catch (error) {
    //   setError(error);
    // }
  }

  useEffect(() => {
    fetchPosts();
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
    await api.post('/posts/', formData);
    fetchPosts(); // re-call all posts from db
    setFormData({
      id: '',
      title: '',
      content: '',
      user_id: '',
    });
  };


  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href="#">
            Blog Application
          </a>
        </div>
      </nav>

      <div className='container'>
        <form onSubmit={handleFormSubmit}>

          <div className='mb-3 mt-3'>
            <label htmlFor='post_id' className='form-label'>
              id
            </label>
            <input type='text' className='form-control' id='id' name='id' onChange={handleInputChange} value={formData.id}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='title' className='form-label'>
              title
            </label>
            <input type='text' className='form-control' id='title' name='title' onChange={handleInputChange} value={formData.title}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='content' className='form-label'>
              content
            </label>
            <input type='text' className='form-control' id='content' name='content' onChange={handleInputChange} value={formData.content}/>
          </div>

          <div className='mb-3 mt-3'>
            <label htmlFor='user_id' className='form-label'>
              user_id
            </label>
            <input type='text' className='form-control' id='user_id' name='user_id' onChange={handleInputChange} value={formData.user_id}/>
          </div>

          <button type='submit' className='btn btn-primary'>
            Submit
          </button>

        </form>

        <table className='table table-striped table-bordered table-hover'>
          <thead>
            <tr>
              <th>id</th>
              <th>title</th>
              <th>content</th>
              <th>user_id</th>
            </tr>
          </thead>
          <tbody>
            {posts.map((post) => (
              <tr key={post.id}>
                <td>{post.id}</td>
                <td>{post.title}</td>
                <td>{post.content}</td>
                <td>{post.user_id}</td>
              </tr>
            ))}
          </tbody>
        </table>

      </div>
    </div>
  )

}

export default App;
