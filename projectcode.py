import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "8RA1eP2OEQqN1olxwACaKd20usMbFfqOK13JOX1jM2XW"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
# payload_scoring = {"input_data": [{"field": [array_of_input_field], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data": [ {"field": [[ "age","blood_pressure","specific_gravity","albumin",
              "sugar","red_blood_cells","pus_cell","pus_cell_clumps","bacteria",
              "blood glucose random","blood_urea","serum_creatinine","sodium","potassium",
              "hemoglobin","packed_cell_volume","white_blood_cell_count","red_blood_cell_count",
              "hypertension","diabetesmellitus","coronary_artery_disease","appetite",
              "pedal_edema","anemia"]],
              "values": [[ 63,70,1.01,3,0,0,0,0,1,380,60,2.7,131,4.2,10.8,32,4500,3.8,1,1,0,1,1,0,]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/580d542b-147b-4b4e-817f-007c5eefade5/predictions?version=2021-06-08', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]  

if(pred == 0):
    print("he will not get")
    
else:
        print("he will get")