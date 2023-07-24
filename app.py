from flask import Flask, jsonify
import requests
from requests.auth import HTTPBasicAuth
Authorization_Key=HTTPBasicAuth('fe4c8fa7-c07c-422e-9573-4659750ab08b','')
app = Flask('Flask')
@app.route("/")
def reed_api():
    Reed_Api="https://www.reed.co.uk/api/1.0/search"
    Request_PARAMS={
    'keywords':'Software',
    'LocationName':'London'
    }
    result=requests.get(Reed_Api,params=Request_PARAMS,auth=Authorization_Key)
    return jsonify(result.json())
