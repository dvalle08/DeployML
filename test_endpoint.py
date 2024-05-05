import requests

url = "http://deploy-ml.southcentralus.azurecontainer.io:8000/v1/prediction"

json= {"opening_gross": 8330681,
        "screens" : 2271,
        "production_budget": 13000000,
        "title_year": 1999,
        "aspect_ratio": 1.85,
        "duration": 97,
        "cast_total_facebook_likes": 37907,
        "budget": 16000000,
        "imdb_score": 7.2}

response = requests.post(url, json=json)
print(response)
print(response.json())
breakpoint()
