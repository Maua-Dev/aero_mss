from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .create_cm_simulation_usecase import CreateCmSimulationUsecase
from .create_cm_simulation_viewmodel import CreateCmSimulationViewmodel 
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created

class CreateCmSimulationController:
    def __init__(self, usecase: CreateCmSimulationUsecase):
        # store usecase with a simple name and use it consistently
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            simulation_id = request.data.get('simulation_id')
            xcg = request.data.get('xcg', None)
            xac_w = request.data.get('xac_w', None)
            sw = request.data.get('sw', None)
            st = request.data.get('st', None)
            cw = request.data.get('cw', None)
            ct = request.data.get('ct', None)
            iw = request.data.get('iw', None)
            it = request.data.get('it', None)
            lt = request.data.get('lt', None)
            cm_ac = request.data.get('cm_ac', None)
            cl_0 = request.data.get('cl_0', None)
            cl_alpha = request.data.get('cl_alpha', None)

            if simulation_id is None:
                raise MissingParameters('simulation_id')
            if xcg is None:
                raise MissingParameters('xcg')
            if xac_w is None:
                raise MissingParameters('xac_w')
            if sw is None:
                raise MissingParameters('sw')
            if st is None:
                raise MissingParameters('st')
            if cw is None:
                raise MissingParameters('cw')
            if ct is None:
                raise MissingParameters('ct')
            if iw is None:
                raise MissingParameters('iw')
            if it is None:
                raise MissingParameters('it')
            if lt is None:
                raise MissingParameters('lt')
            if cm_ac is None:
                raise MissingParameters('cm_ac')
            if cl_0 is None:
                raise MissingParameters('cl_0')
            if cl_alpha is None:
                raise MissingParameters('cl_alpha')
            
            simulation = self.usecase(
                simulation_id=simulation_id,
                xcg=xcg,
                xac_w=xac_w,
                sw=sw,
                st=st, 
                cw=cw,
                ct=ct,
                iw=iw,
                it=it,
                lt=lt,
                cm_ac=cm_ac,
                cl_0=cl_0,
                cl_alpha=cl_alpha
            )
            
            viewmodel = CreateCmSimulationViewmodel(simulation)
            
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
