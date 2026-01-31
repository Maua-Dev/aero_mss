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
    def __init__(self, usecase, observability: ObservabilityAWS):
        self.usecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            simulation_id = request.data.get('simulation_id')
            if type(simulation_id) != str:
                raise EntityError("simulation_id")
            if request.data.get('simulation_id') is None:
                raise MissingParameters("simulation_id")

            cm_simulation = self.usecase(simulation_id)
            viewmodel = GetCmSimulationViewmodel(cm_simulation)
            response = OK(viewmodel.to_dict())
            self.observability.log_controller_out(input=simulation_id)
            return response

        except NoItemsFound as err:
            self.observability.log_exception(message=err.message)
            return NotFound(body=err.message)

        except MissingParameters as err:
            self.observability.log_exception(message=err.message)
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            self.observability.log_exception(message=err.message)
            return BadRequest(body=err.message)

        except EntityError as err:
            self.observability.log_exception(message=err.message)
            return BadRequest(body=err.message)

        except Exception as err:
            self.observability.log_exception(message=err.args[0])
            return InternalServerError(body=err.args[0])