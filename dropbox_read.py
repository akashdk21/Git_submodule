"""Reading Files from dropbox"""
import requests
import json

headers = {"Authorization": "Bearer sl.A_BLmwgbC7pbSgQfC8_3hdM_7fDAcEwgkCeiKf2AmzQlBPwEQCQ2I8CFpYYRpDR4HQxBGdAEkjDcUXrjS4MruUlAJk8pAYF6C5NliUNu85lhCWZnkOlN-ysH4xbQlZv86GRtSYkhEEQh" ,
           "Dropbox-API-Arg": "{\"path\": \"/Home/Akash/File1.txt\"}"
           }
r = requests.post(
    "https://content.dropboxapi.com/2/files/download",
    headers=headers
)
print(r.text)
#print(r.get("id"))
'''file1=open("File1.txt","w")
content=r.text+"File is updated\n"
file1.write(content)
file1.close()'''

#get_id

'''headers = {"Authorization": "Bearer sl.A_BLmwgbC7pbSgQfC8_3hdM_7fDAcEwgkCeiKf2AmzQlBPwEQCQ2I8CFpYYRpDR4HQxBGdAEkjDcUXrjS4MruUlAJk8pAYF6C5NliUNu85lhCWZnkOlN-ysH4xbQlZv86GRtSYkhEEQh" ,
           "Content-Type": "application/json" }

r = requests.post(
    "https://api.dropboxapi.com/2/files/get_metadata",
    headers=headers,
    data="{\"path\": \"/Home/Akash/file1.txt\",\"include_media_info\": false,\"include_deleted\": false,\"include_has_explicit_shared_members\": false}"
)
print(r.text)'''
