from .delete_cm_simulation_controller import DeleteCmSimulationController
from .delete_cm_simulation_usecase import DeleteCmSimulationUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_cm_simulation_repo()()
usecase = DeleteCmSimulationUsecase(repo)
controller = DeleteCmSimulationController(usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()