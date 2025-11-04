from .create_cm_simulation_controller import CreateCmSimulationController
from .create_cm_simulation_usecase import CreateCmSimulationUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_cm_simulation_repo()()
usecase = CreateCmSimulationUsecase(repo)
controller = CreateCmSimulationController(usecase)

def lambda_handler(event, context):

    from pprint import pprint

    pprint(event)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()