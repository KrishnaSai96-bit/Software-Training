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
    let add_index;