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
            
            # implementing a new concept called DRY
            
            expected_fields = [
                'xcg', 'xac_w', 'sw', 'st', 'cw', 'ct',
                'iw', 'it', 'lt',  'cm_ac', 'cl_0', 'cl_alpha'
            ]
            
            params = {}
            
            for field in expected_fields:
                val = request.data.get(field)
                
                if val is None:
                    raise MissingParameters(field)
                
                try:
                    params[field] = float(val)
                except (ValueError, TypeError):
                    raise WrongTypeParameter(field, 'float', type(val).__name__)
                
            simulation = self.usecase(**params)
        
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
