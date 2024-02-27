from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(docs_url='/')

@app.post('/v1/prediction')  # Added forward slash to the endpoint path
def make_model_prediction(request: PredictionRequest):
    prediction_result = get_prediction(request)
    return PredictionResponse(worldwide_gross=prediction_result)
