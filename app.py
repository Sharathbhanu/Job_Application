from flask import Flask, jsonify
import requests
from requests.auth import HTTPBasicAuth
Authorization_Key=HTTPBasicAuth('fe4c8fa7-c07c-422e-9573-4659750ab08b','')
app = Flask('Flask')
@app.route("/")
def reed_api():
    Reed_Api="https://www.reed.co.uk/api/1.0/search"
    Request_Params={
    'keywords':'Software',# Search keyword
    'LocationName':'Staines Green',# Location name
    'resultsToTake':'50',# Maximum number of results to return
    'distanceFromLocation':'10'
    }
    Request_Params['contract'] = 'True'
    Request_Params['minimumSalary']='60000'
    Request_Params['distanceFromLocation'] = '5'
    Request_Params['employerId'] = '431258'
    result=requests.get(Reed_Api,params=Request_Params,auth=Authorization_Key)
    oneresult=result.json()
    print(oneresult['results'][0] )
    print(oneresult['results'][1] )
    one=oneresult['results'][1]['jobDescription']
    two=oneresult['results'][1]['locationName']
    return two
    
    


