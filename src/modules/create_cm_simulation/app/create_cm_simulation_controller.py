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
            
            if xcg is None:
                raise MissingParameters('xcg')
            if isinstance(xcg, float) is False:
                raise WrongTypeParameter('xcg', 'float', type(xcg).__name__)
            
            if xac_w is None:
                raise MissingParameters('xac_w')
            if isinstance(xac_w, float) is False:
                raise WrongTypeParameter('xac_w', 'float', type(xac_w).__name__)
            
            if sw is None:
                raise MissingParameters('sw')
            if isinstance(sw, float) is False:
                raise WrongTypeParameter('sw', 'float', type(sw).__name__)
            
            if st is None:
                raise MissingParameters('st')
            if isinstance(st, float) is False:
                raise WrongTypeParameter('st', 'float', type(st).__name__)
            
            if cw is None:
                raise MissingParameters('cw')
            if isinstance(cw, float) is False:
                raise WrongTypeParameter('cw', 'float', type(cw).__name__)
            
            if ct is None:
                raise MissingParameters('ct')
            if isinstance(ct, float) is False:
                raise WrongTypeParameter('ct', 'float', type(ct).__name__)
            
            if iw is None:
                raise MissingParameters('iw')
            if isinstance(iw, float) is False:
                raise WrongTypeParameter('iw', 'float', type(iw).__name__)
            
            if it is None:
                raise MissingParameters('it')
            if isinstance(it, float) is False:
                raise WrongTypeParameter('it', 'float', type(it).__name__)
            
            if lt is None:
                raise MissingParameters('lt')
            if isinstance(lt, float) is False:
                raise WrongTypeParameter('lt', 'float', type(lt).__name__)
            
            if cm_ac is None:
                raise MissingParameters('cm_ac')
            if isinstance(cm_ac, float) is False:
                raise WrongTypeParameter('cm_ac', 'float', type(cm_ac).__name__)
            
            if cl_0 is None:
                raise MissingParameters('cl_0')
            if isinstance(cl_0, float) is False:
                raise WrongTypeParameter('cl_0', 'float', type(cl_0).__name__)
            
            if cl_alpha is None:
                raise MissingParameters('cl_alpha')
            if isinstance(cl_alpha, float) is False:
                raise WrongTypeParameter('cl_alpha', 'float', type(cl_alpha).__name__)
            
            
            simulation = self.usecase(
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
