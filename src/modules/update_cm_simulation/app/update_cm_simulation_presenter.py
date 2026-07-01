from .update_cm_simulation_controller import UpdateCmSimulationController
from .update_cm_simulation_usecase import UpdateCmSimulationUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_cm_simulation_repo()()
usecase = UpdateCmSimulationUsecase(repo)
controller = UpdateCmSimulationController(usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()