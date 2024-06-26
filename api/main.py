from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(docs_url='/')

@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross=get_prediction(request))

{
"opening_gross": 8330681,
"screens" : 2271,
"production_budget": 13000000,
"title_year": 1999,
"aspect_ratio": 1.85,
"duration": 97,
"cast_total_facebook_likes": 37907,
"budget": 16000000,
"imdb_score": 7.2
}