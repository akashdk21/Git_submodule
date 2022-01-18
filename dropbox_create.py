'''from unittest.mock import patch
import requests
import json
def create1():
    
    headers = {"Authorization": "Bearer sl.A_hdsvrhs6_7L_rNPJBJa6F8gybrWbBMvdrTFXadg6zh7UdAOUtbH8G8btBLStZ1iHRisqTvyoZ_qFHTkfP0xuoonBVaxSTOnDRA8STnpMd3L16TOfVAtyjWO0af2XgXlHqzQEjrKCLW" ,
           "Content-Type": "application/json" 
           }
    r = requests.post(
    "https://api.dropboxapi.com/2/file_requests/create",
        headers=headers,
        data="{\"title\": \"Homework submission\",\"destination\": \"/Home/Akash/\",\"open\": true}"
    )
    print(r.json().get("url"))
    return r.status_code
create1()'''

'''@patch('__main__.requests')
def test_is_valid_url(patched_requests):
    patched_requests.get.return_value = Mock(status_code=200)
    assert 200==create1()'''

    

import requests
import json

url = "https://api.dropboxapi.com/2/file_requests/create"

payload = "{\"title\": \"Homework submission\",\"destination\": \"/Home/Akash/\",\"open\": true}"
headers = {
  'Authorization': 'Bearer sl.A_0lxnVTaRv9Lo79WqbGontJ6LgakfFiZcAwBKBWs7MFddoKMHFGtBlS3ixJhHFltcDwt-oouTKr_-xSo6zvduA46X7fhg07TRS3bHO6A-x0jnvzSIJ2BJB-h0ytwwKP9TeVrqxKjf-v',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



