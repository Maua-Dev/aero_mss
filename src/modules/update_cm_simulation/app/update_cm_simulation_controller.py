from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .update_cm_simulation_usecase import UpdateCmSimulationUsecase
from .update_cm_simulation_viewmodel import UpdateCmSimulationViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError

class UpdateCmSimulationController:

    def __init__(self, usecase: UpdateCmSimulationUsecase):
        self.UpdateCmSimulationUsecase = usecase

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

            if request.data.get('simulation_id') is None:
                raise MissingParameters('simulation_id')
            if isinstance(request.data.get('simulation_id'), str) is False:
                raise WrongTypeParameter('simulation_id', 'str', type(request.data.get('simulation_id')).__name__)

            if request.data.get('xcg') is None:
                raise MissingParameters('xcg')
            if isinstance(request.data.get('xcg'), float) is False:
                raise WrongTypeParameter('xcg', 'float', type(request.data.get('xcg')).__name__)
            
            if request.data.get('xac_w') is None:
                raise MissingParameters('xac_w')
            if isinstance(request.data.get('xac_w'), float) is False:
                raise WrongTypeParameter('xac_w', 'float', type(request.data.get('xac_w')).__name__)
            
            if request.data.get('sw') is None:
                raise MissingParameters('sw')
            if isinstance(request.data.get('sw'), float) is False:
                raise WrongTypeParameter('sw', 'float', type(request.data.get('sw')).__name__)
            
            if request.data.get('st') is None:
                raise MissingParameters('st')
            if isinstance(request.data.get('st'), float) is False:
                raise WrongTypeParameter('st', 'float', type(request.data.get('st')).__name__)
            
            if request.data.get('cw') is None:
                raise MissingParameters('cw')
            if isinstance(request.data.get('cw'), float) is False:
                raise WrongTypeParameter('cw', 'float', type(request.data.get('cw')).__name__)
            
            if request.data.get('ct') is None:
                raise MissingParameters('ct')
            if isinstance(request.data.get('ct'), float) is False:
                raise WrongTypeParameter('ct', 'float', type(request.data.get('ct')).__name__)
            
            if request.data.get('iw') is None:
                raise MissingParameters('iw')
            if isinstance(request.data.get('iw'), float) is False:
                raise WrongTypeParameter('iw', 'float', type(request.data.get('iw')).__name__)
            
            if request.data.get('it') is None:
                raise MissingParameters('it')
            if isinstance(request.data.get('it'), float) is False:
                raise WrongTypeParameter('it', 'float', type(request.data.get('it')).__name__)
            
            if request.data.get('lt') is None:
                raise MissingParameters('lt')
            if isinstance(request.data.get('lt'), float) is False:
                raise WrongTypeParameter('lt', 'float', type(request.data.get('lt')).__name__)
            
            if request.data.get('cm_ac') is None:
                raise MissingParameters('cm_ac')
            if isinstance(request.data.get('cm_ac'), float) is False:
                raise WrongTypeParameter('cm_ac', 'float', type(request.data.get('cm_ac')).__name__)
            
            if request.data.get('cl_0') is None:
                raise MissingParameters('cl_0')
            if isinstance(request.data.get('cl_0'), float) is False:
                raise WrongTypeParameter('cl_0', 'float', type(request.data.get('cl_0')).__name__)
            
            if request.data.get('cl_alpha') is None:
                raise MissingParameters('cl_alpha')
            if isinstance(request.data.get('cl_alpha'), float) is False:
                raise WrongTypeParameter('cl_alpha', 'float', type(request.data.get('cl_alpha')).__name__)

            simulation = self.UpdateCmSimulationUsecase(
                simulation_id=simulation_id,
                new_xcg=xcg,
                new_xac_w=xac_w,
                new_sw=sw,
                new_st=st, 
                new_cw=cw,
                new_ct=ct,
                new_iw=iw,
                new_it=it,
                new_lt=lt,
                new_Cm_ac=cm_ac,
                new_Cl_0=cl_0,
                new_Cl_alpha=cl_alpha
            )

            viewmodel = UpdateCmSimulationViewmodel(cm_simulation=simulation)

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