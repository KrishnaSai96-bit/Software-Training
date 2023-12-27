import { AgGridReact } from 'ag-grid-react'; // React Grid Logic
import "ag-grid-community/styles/ag-grid.css"; // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css"; // Theme

const  [colDefs, setColDefs] = useState([
    { field: "ID", editable: true, filter: true, pinned: 'left', cellDataType: 'number'},
    { field: "Title", editable: true, filter: true, pinned: 'left', cellDataType: 'text'},
    { field: "Ingredients", editable: true, filter: true, cellDataType: 'text'},
    { field: "CookingTime", editable: true, filter: true, cellDataType: 'number'},
    { field: "Category", editable: true, filter: true, cellDataType: 'text'},
    { field: "Steps",editable: true, filter: true, cellDataType: 'text'}
  ]);