from typing import List

from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .get_all_simulations_usecase import GetAllSimulationsUsecase
from .get_all__simulations_viewmodel import GetAllSimulationsViewModel
from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetAllSimulationsController:

    def __init__(self, usecase: GetAllSimulationsUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            all_simulations_list: List[CmSimulation] = self.usecase()

            viewmodel = GetAllSimulationsViewModel(all_simulations_list)

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

            return InternalServerError(body=err.args[0]) 
