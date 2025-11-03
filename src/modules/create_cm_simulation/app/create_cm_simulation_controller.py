from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .create_cm_simulation_usecase import CreateCMSimulationUsecase
from .create_cm_simulation_viewmodel import CreateCMSimulationViewmodel 
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created

class CreateCMSimulationController:
    def __init__(self, usecase: CreateCMSimulationUsecase):
        self.CreateCMSimulationUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('simulation_id') is None:
                raise MissingParameters('simulation_id')
            if request.data.get('xcg') is None:
                raise MissingParameters('xcg')
            if request.data.get('xac_w') is None:
                raise MissingParameters('xac_w')
            if request.data.get('sw') is None:
                raise MissingParameters('sw')
            if request.data.get('st') is None:
                raise MissingParameters('st')
            if request.data.get('cw') is None:
                raise MissingParameters('cw')
            if request.data.get('ct') is None:
                raise MissingParameters('ct')
            if request.data.get('iw') is None:
                raise MissingParameters('iw')
            if request.data.get('it') is None:
                raise MissingParameters('it')
            if request.data.get('lt') is None:
                raise MissingParameters('lt')
            if request.data.get('cm_ac') is None:
                raise MissingParameters('cm_ac')
            if request.data.get('cl_0') is None:
                raise MissingParameters('cl_0')
            if request.data.get('cl_alpha') is None:
                raise MissingParameters('cl_alpha')
            
            simulation = self.CreateCMSimulationUsecase(
                simulation_id=request.data.get('simulation_id'),
                xcg=request.data.get('xcg'),
                xac_w=request.data.get('xac_w'),
                sw=request.data.get('sw'),
                st=request.data.get('st'), 
                cw=request.data.get('cw'),
                ct=request.data.get('ct'),
                iw=request.data.get('iw'),
                it=request.data.get('it'),
                lt=request.data.get('lt'),
                cm_ac=request.data.get('cm_ac'),
                cl_0=request.data.get('cl_0'),
                cl_alpha=request.data.get('cl_alpha')
            )
            
            viewmodel = CreateCMSimulationViewmodel(simulation)
            
            return Created(viewmodel.to_dict())

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:
            
            print(err)

            return InternalServerError(body=err.args[0])
        