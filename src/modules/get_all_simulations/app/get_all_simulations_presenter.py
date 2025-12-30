from .get_all_simulations_controller import GetAllSimulationsController
from .get_all_simulations_usecase import GetAllSimulationsUsecase
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo: ICmSimulationRepository = Environments.get_cm_simulation_repo()()
usecase = GetAllSimulationsUsecase(repo)
controller = GetAllSimulationsController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
