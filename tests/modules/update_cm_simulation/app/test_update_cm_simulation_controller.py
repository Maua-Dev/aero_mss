from src.modules.update_cm_simulation.app.update_cm_simulation_controller import UpdateCmSimulationController
from src.modules.update_cm_simulation.app.update_cm_simulation_usecase import UpdateCmSimulationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import uuid

class Test_UpdateCmSimulationController:
    def test_update_cm_simulation_controller(self):
        repo = CmSimulationRepositoryMock()
        usecase = UpdateCmSimulationUsecase(repo=repo)
        controller = UpdateCmSimulationController(usecase=usecase)
        simulation_id = repo.simulations[0].simulation_id
        request = HttpRequest(body={
            'simulation_id': simulation_id,
            'new_xcg': 25.0,
            'new_xac_w': 30.0,
            'new_sw': 150.0,
            'new_st': 40.0,
            'new_cw': 20.0,
            'new_ct': 15.0,
            'new_iw': 10.0,
            'new_it': 5.0,
            'new_lt': 12.0,
            'new_cm_ac': -2.5,
            'new_cl_0': 0.3,
            'new_cl_alpha': 5.5
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['cm_simulation']['simulation_id'] == simulation_id
        assert response.body['cm_simulation']['xcg'] == 25.0
        assert response.body['cm_simulation']['xac_w'] == 30.0
        assert response.body['cm_simulation']['sw'] == 150.0
        assert response.body['cm_simulation']['st'] == 40.0
        assert response.body['cm_simulation']['cw'] == 20.0
        assert response.body['cm_simulation']['ct'] == 15.0
        assert response.body['cm_simulation']['iw'] == 10.0
        assert response.body['cm_simulation']['it'] == 5.0
        assert response.body['cm_simulation']['lt'] == 12.0
        assert response.body['cm_simulation']['cm_ac'] == -2.5
        assert response.body['cm_simulation']['cl_0'] == 0.3
        assert response.body['cm_simulation']['cl_alpha'] == 5.5
        assert response.body['message'] == 'the cm simulation was updated successfully'