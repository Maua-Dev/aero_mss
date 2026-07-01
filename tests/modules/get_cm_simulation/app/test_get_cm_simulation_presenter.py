import json
from src.modules.get_cm_simulation.app.get_cm_simulation_presenter import lambda_handler
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock

class Test_GetCmSimulationPresenter:
    def test_get_cm_simulation_presenter_success(self):
        repo = CmSimulationRepositoryMock()
        simulation_id = repo.simulations[0].simulation_id

        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/get_cm_simulation",
            "rawQueryString": f"simulation_id={simulation_id}",
            "queryStringParameters": {
                "simulation_id": simulation_id
            },
            "requestContext": {
                "http": {
                    "method": "GET" 
                }
            }
        }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body['cm_simulation']["simulation_id"] == simulation_id

    def test_get_cm_simulation_presenter_not_found(self):
        event = {
            "version": "2.0",
            "queryStringParameters": {
                "simulation_id": "12345678-1234-1234-1234-123456789012"
            },
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 404
        assert "No items found" in response["body"]

    def test_get_cm_simulation_presenter_missing_param(self):
        event = {
            "version": "2.0",
            "queryStringParameters": {},
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert "Field simulation_id is missing" in response["body"]
