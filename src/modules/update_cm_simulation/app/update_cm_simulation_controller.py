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

            if simulation_id is None:
                raise MissingParameters('simulation_id')
            if isinstance(simulation_id, str) is False:
                raise WrongTypeParameter('simulation_id', 'str', type(simulation_id).__name__)

            float_fields = [
                'new_xcg', 'new_xac_w', 'new_sw', 'new_st', 
                'new_cw', 'new_ct', 'new_iw', 'new_it', 
                'new_lt', 'new_cm_ac', 'new_cl_0', 'new_cl_alpha'
            ]

            validated_data = {'simulation_id': simulation_id}

            for field in float_fields:
                val = request.data.get(field)
                
                # Só validamos e convertemos se o campo foi enviado no request
                if val is not None:
                    try:
                        validated_data[field] = float(val)
                    except (ValueError, TypeError):
                        raise WrongTypeParameter(field, 'float', type(val).__name__)
                else:
                    # Se for None, passamos None para o usecase (ou omitimos)
                    validated_data[field] = None

            simulation = self.UpdateCmSimulationUsecase(
                simulation_id=validated_data['simulation_id'],
                new_xcg=validated_data['new_xcg'],
                new_xac_w=validated_data['new_xac_w'],
                new_sw=validated_data['new_sw'],
                new_st=validated_data['new_st'],
                new_cw=validated_data['new_cw'],
                new_ct=validated_data['new_ct'],
                new_iw=validated_data['new_iw'],
                new_it=validated_data['new_it'],
                new_lt=validated_data['new_lt'],
                new_Cm_ac=validated_data['new_cm_ac'], # Ajustado para bater com seu usecase original
                new_Cl_0=validated_data['new_cl_0'],
                new_Cl_alpha=validated_data['new_cl_alpha']
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