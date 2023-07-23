from flask import Flask
import requests
Authorization_Key="fe4c8fa7-c07c-422e-9573-4659750ab08b"
app = Flask('Flask')
@app.route("/")
def reed_api():
    Reed_Api="https://www.reed.co.uk/api/1.0/search"
    Request_PARAMS={
    'keywords':'Software',
    'LocationName':'London'
    }
    result=requests.get(Reed_Api,params=Request_Params,auth=Authorization_Key)
    result.json() 
