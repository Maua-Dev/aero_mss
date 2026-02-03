from .get_cm_simulation_controller import GetCmSimulationController
from .get_cm_simulation_usecase import GetCmSimulationUsecase   
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_cm_simulation_repo()()
usecase = GetCmSimulationUsecase(repo)
controller = GetCmSimulationController(usecase)

def get_cm_simulation_presenter(event):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = get_cm_simulation_presenter(event)
        
    return response