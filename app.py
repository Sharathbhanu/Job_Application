from flask import Flask,render_template, jsonify,request #imported all the requirements
import requests
from requests.auth import HTTPBasicAuth
Authorization_Key=HTTPBasicAuth('fe4c8fa7-c07c-422e-9573-4659750ab08b','') # Provided my API key for authentication
app = Flask(__name__)
# Set the static folder to serve static files (styles.css and scripts.js)
app.static_folder = 'static'

@app.route("/")# Defined the root route for the Flask app
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_jobs():
    Reed_Api="https://www.reed.co.uk/api/1.0/search" # URL of the Reed.co.uk API
    Request_Params={   # Parameters for the API request
    'keywords': request.json['keywords'],# Search keyword
    'LocationName': request.json['location'],# Location name
    'distanceFromLocation':request.json['distanceFromLocation'],# Distance from the location (in miles)
    # Additional parameters for filtering
    'contract' : request.json['contract'], # Contract type: True (contract) or False (permanent)
    'minimumSalary': request.json['minimumSalary'], # Minimum salary for job listings
    'employerId' : request.json['employerId']# Employer ID for specific employer
    # Send the API request to Reed.co.uk and get the response
    }
    result=requests.get(Reed_Api,params=Request_Params,auth=Authorization_Key)
    return result.json() # API response JSON
   
if __name__ == "__main__":
    app.run()

    
    


