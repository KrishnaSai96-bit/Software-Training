#PyUnit Testing:

import pytest
from fastapi.testclient import TestClient
from KnowledgeHub import app  # Replace with the actual import statement for your FastAPI app

client = TestClient(app)

@pytest.mark.parametrize("data_payload", [
    {"title": "Message_ID", "content": "1"},
    {"title": "Technology_Type", "content": "JS"},
    {"title": "Exception_Type", "content": "Error"},
    {"title": "Exception_Title", "content": "Permission denied to access property ""x"""},
    {"title": "Description", "content": "The JavaScript exception ""Permission denied to access property"" occurs when there was an attempt to access an object for which you have no permission."},
    
])
def test_create_data(data_payload):
    response = client.post("/KnowledgeHub/CreateData", json=data_payload)
    assert response.status_code == 200
    assert response.json()["Message_ID"] == data_payload["Message_ID"]
    assert response.json()["Technology_Type"] == data_payload["Technology_Type"]
    assert response.json()["Exception_Type"] == data_payload["Exception_Type"]
    assert response.json()["Exception_Title"] == data_payload["Exception_Title"]
    assert response.json()["Description"] == data_payload["Description"]

def test_get_all_data():
    response = client.get("/KnowledgeHub/GetData")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  

def test_get_data_using_id():
    message_id = 1  
    response = client.get(f"/KnowledgeHub/GetData_Using_ID{message_id}")
    assert response.status_code == 200
    assert "title" in response.json()  
    assert "content" in response.json() 
    
def test_get_data_using_technology_type():
    technology_type = "JS" 
    response = client.get(f"/KnowledgeHub/GetData_Using_Technology_Type{technology_type}")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 