from flask import Flask, jsonify #imported all the requirements
import requests
from requests.auth import HTTPBasicAuth
Authorization_Key=HTTPBasicAuth('fe4c8fa7-c07c-422e-9573-4659750ab08b','') # Provided my API key for authentication
app = Flask('Flask')
@app.route("/")# Defined the root route for the Flask app
def reed_api():
    Reed_Api="https://www.reed.co.uk/api/1.0/search" # URL of the Reed.co.uk API
    Request_Params={# Parameters for the API request
    'keywords':'Software',# Search keyword
    'LocationName':'Staines Green',# Location name
    'resultsToTake':'50',# Maximum number of results to return
    'distanceFromLocation':'10'# Distance from the location (in miles)
    }
    # Additional parameters for filtering
    Request_Params['contract'] = 'True' # Contract type: True (contract) or False (permanent)
    Request_Params['minimumSalary']='60000' # Minimum salary for job listings
    Request_Params['distanceFromLocation'] = '5' # Updated distance from location to 5 miles
    Request_Params['employerId'] = '431258'# Employer ID for specific employer
    # Send the API request to Reed.co.uk and get the response
    result=requests.get(Reed_Api,params=Request_Params,auth=Authorization_Key)
    oneresult=result.json() # API response JSON
    # Printed the first two results (for demonstration purposes)
    print(oneresult['results'][0] )
    print(oneresult['results'][1] )
    # Extract job description and location name from the second result
    one=oneresult['results'][1]['jobDescription']
    two=oneresult['results'][1]['locationName']
    four=(one,two) # Created a tuple containing job description and location name
    if oneresult['results']:
    #  # If 'results' is not empty, return the first item in the listfirst item in the list
        three=oneresult['results'][0]
        return three
    else:
    # If 'results' is empty, returning the below statement
        return "No matching job listings found."
    
    


