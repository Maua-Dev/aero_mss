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
            new_xcg = request.data.get('new_xcg')
            new_xac_w = request.data.get('new_xac_w')
            new_sw = request.data.get('new_sw')
            new_st = request.data.get('new_st')
            new_cw = request.data.get('new_cw')
            new_ct = request.data.get('new_ct')
            new_iw = request.data.get('new_iw')
            new_it = request.data.get('new_it')
            new_lt = request.data.get('new_lt')
            new_cm_ac = request.data.get('new_cm_ac')
            new_cl_0 = request.data.get('new_cl_0')
            new_cl_alpha = request.data.get('new_cl_alpha')

            if simulation_id is None:
                raise MissingParameters('simulation_id')
            if isinstance(simulation_id, str) is False:
                raise WrongTypeParameter('simulation_id', 'str', type(simulation_id).__name__)

            if new_xcg is not None and isinstance(new_xcg, float) is False:
                raise WrongTypeParameter('new_xcg', 'float', type(new_xcg).__name__)

            if new_xac_w is not None and isinstance(new_xac_w, float) is False:
                raise WrongTypeParameter('new_xac_w', 'float', type(new_xac_w).__name__)

            if new_sw is not None and isinstance(new_sw, float) is False:
                raise WrongTypeParameter('new_sw', 'float', type(new_sw).__name__)

            if new_st is not None and isinstance(new_st, float) is False:
                raise WrongTypeParameter('new_st', 'float', type(new_st).__name__)

            if new_cw is not None and isinstance(new_cw, float) is False:
                raise WrongTypeParameter('new_cw', 'float', type(new_cw).__name__)

            if new_ct is not None and isinstance(new_ct, float) is False:
                raise WrongTypeParameter('new_ct', 'float', type(new_ct).__name__)

            if new_iw is not None and isinstance(new_iw, float) is False:
                raise WrongTypeParameter('new_iw', 'float', type(new_iw).__name__)

            if new_it is not None and isinstance(new_it, float) is False:
                raise WrongTypeParameter('new_it', 'float', type(new_it).__name__)

            if new_lt is not None and isinstance(new_lt, float) is False:
                raise WrongTypeParameter('new_lt', 'float', type(new_lt).__name__)

            if new_cm_ac is not None and isinstance(new_cm_ac, float) is False:
                raise WrongTypeParameter('new_cm_ac', 'float', type(new_cm_ac).__name__)

            if new_cl_0 is not None and isinstance(new_cl_0, float) is False:
                raise WrongTypeParameter('new_cl_0', 'float', type(new_cl_0).__name__)

            if new_cl_alpha is not None and isinstance(new_cl_alpha, float) is False:
                raise WrongTypeParameter('new_cl_alpha', 'float', type(new_cl_alpha).__name__)

            simulation = self.UpdateCmSimulationUsecase(
                simulation_id=simulation_id,
                new_xcg=new_xcg,
                new_xac_w=new_xac_w,
                new_sw=new_sw,
                new_st=new_st, 
                new_cw=new_cw,
                new_ct=new_ct,
                new_iw=new_iw,
                new_it=new_it,
                new_lt=new_lt,
                new_Cm_ac=new_cm_ac,
                new_Cl_0=new_cl_0,
                new_Cl_alpha=new_cl_alpha
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