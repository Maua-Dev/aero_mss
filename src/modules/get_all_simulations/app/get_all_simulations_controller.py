from src.shared.domain.interfaces.controller import Controller
from src.shared.domain.interfaces.usecase import Usecase
from src.shared.domain.interfaces.http import IRequest, IResponse
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServer


class getAllSimulationsController(Controller):

    def __init__(self, usecase: Usecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            simulations = self.usecase()

            return OK(simulations)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:
            
            print(err)

            return InternalServerError(body=err.args[0]) 
