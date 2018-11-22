import src.apiConnection as api
import json
import numpy as np

#Get data
api_connection = api.ApiConnection()

all_matches = api_connection.get_all_matches().get("matches")

for val in all_matches:
    print(val)