from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.infra.external.observability.observability_aws import ObservabilityAWS
from .get_cm_simulation_viewmodel import GetCmSimulationViewmodel
from src.modules.get_cm_simulation.app.get_cm_simulation_usecase import GetCmSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError

class GetCmSimulationController:
    def __init__(self, usecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            simulation_id = request.data.get('simulation_id')
            
            if request.data.get('simulation_id') is None:
                raise MissingParameters("simulation_id")
            
            if type(simulation_id) != str:
                raise WrongTypeParameter(
                    fieldName="simulation_id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=type(simulation_id).__name__
                )

            cm_simulation = self.usecase(simulation_id)
            viewmodel = GetCmSimulationViewmodel(cm_simulation)
            response = OK(viewmodel.to_dict())
            return response

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])