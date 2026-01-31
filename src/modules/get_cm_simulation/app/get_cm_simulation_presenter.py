from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.infra.external import observability
from .get_cm_simulation_controller import GetCmSimulationController
from src.shared.infra.external.observability.observability_aws import ObservabilityAWS
from .get_cm_simulation_usecase import GetCmSimulationUsecase   
from src.shared.environments import Environments

observability = Environments.get_observability()(module_name="get_cm_simulation")

repo = Environments.get_cm_simulation_repo()()
usecase = GetCmSimulationUsecase(repo, observability=observability)
controller = GetCmSimulationController(usecase, observability=observability)

@observability.presenter_decorators
def get_cm_simulation_presenter(event):
    from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_cm_simulation_presenter(event)
    
    observability.add_metric(name="ErrorCount", unit="Count", value=1) if response["statusCode"] != 200 else None # ErrorCount metrics
    
    return response