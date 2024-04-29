from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/prediction',json={"opening_gross": 0,
                                                "screens" : 0,
                                                "production_budget": 0,
                                                "title_year": 0,
                                                "aspect_ratio": 0,
                                                "duration": 0,
                                                "cast_total_facebook_likes": 0,
                                                "budget": 0,
                                                "imdb_score": 0})
    
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] == 0

def test_random_prediction():
    response = client.post('/v1/prediction', json={"opening_gross": 8330681,
                                                    "screens" : 2271,
                                                    "production_budget": 13000000,
                                                    "title_year": 1999,
                                                    "aspect_ratio": 1.85,
                                                    "duration": 97,
                                                    "cast_total_facebook_likes": 37907,
                                                    "budget": 16000000,
                                                    "imdb_score": 7.2})

    assert response.status_code == 200
    assert response.json()['worldwide_gross'] > 0

#? 1.
#La mejor práctica llamar a los test con alguno de estos dos patrones: test_*.py o *_test.py. Así solo corriendo el comando pytest les detectará todos los tests del proyecto.
#Fuente: https://docs.pytest.org/en/7.1.x/getting-started.html#run-multiple-tests

#? 2.
#Se podría crear el archivo de test de esta forma: tests/test_api.py, y así pueden agregarse más tests a futuro para otras cosas como los sets de datos. También se tendría que agregar un __init__.py para que el test corra como si estuviera desde el root del proyecto. 
#Esta sería la estructura:
    #tests
    #├── __init__.py
    #└── test_api.py