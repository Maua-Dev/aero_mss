from .delete_simulation_usecase import DeleteSimulationUsecase
from .delete_simulation_viewmodel import DeleteSimulationViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest

class DeleteSimulationController:
    def __init__(self, delete_simulation_use_case):
        self.delete_simulation_use_case = delete_simulation_use_case

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('simulation_id') is None:
                raise MissingParameters('simulation_id')

            simulation_id = request.data.get('simulation_id')
            if type(simulation_id) != str:
                raise EntityError("simulation_id")

            simulation = self.delete_simulation_use_case(
                simulation_id=simulation_id
            )

            viewmodel = DeleteSimulationViewmodel(simulation)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            print(err)
            return InternalServerError(body=err.args[0])