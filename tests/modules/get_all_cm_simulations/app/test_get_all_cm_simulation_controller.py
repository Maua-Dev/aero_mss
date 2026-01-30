from src.modules.get_all_cm_simulation.app.get_all_cm_simulation_controller import GetAllCmSimulationController
from src.modules.get_all_cm_simulation.app.get_all_cm_simulation_usecase import GetAllCmSimulationUsecase
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest


class Test_GetAllCmSimulationController:

    def test_get_all_cm_simulation_controller(self):
        repo_mock = CmSimulationRepositoryMock()
        get_all_cm_simulation_usecase = GetAllCmSimulationUsecase(repo_mock)
        controller = GetAllCmSimulationController(get_all_cm_simulation_usecase)

        response = controller(HttpRequest())

        assert response.status_code == 200
        assert response.body['message'] == 'the simulations were retrieved successfully'
        assert len(response.body['simulations']) == 3
        assert response.body['simulations'][0]['simulation_id'] == repo_mock.simulations[0].simulation_id
        assert response.body['simulations'][0]['xcg'] == repo_mock.simulations[0].xcg
        assert response.body['simulations'][0]['xac_w'] == repo_mock.simulations[0].xac_w
        assert response.body['simulations'][0]['sw'] == repo_mock.simulations[0].sw
        assert response.body['simulations'][0]['st'] == repo_mock.simulations[0].st
        assert response.body['simulations'][0]['cw'] == repo_mock.simulations[0].cw
        assert response.body['simulations'][0]['ct'] == repo_mock.simulations[0].ct
        assert response.body['simulations'][0]['iw'] == repo_mock.simulations[0].iw
        assert response.body['simulations'][0]['it'] == repo_mock.simulations[0].it
        assert response.body['simulations'][0]['lt'] == repo_mock.simulations[0].lt
        assert response.body['simulations'][0]['cm_ac'] == repo_mock.simulations[0].cm_ac
        assert response.body['simulations'][0]['cl_0'] == repo_mock.simulations[0].cl_0
        assert response.body['simulations'][0]['cl_alpha'] == repo_mock.simulations[0].cl_alpha

    def test_get_all_cm_simulation_controller_no_items(self):
        repo_mock = CmSimulationRepositoryMock()
        repo_mock.simulations = []
        get_all_cm_simulation_usecase = GetAllCmSimulationUsecase(repo_mock)
        controller = GetAllCmSimulationController(get_all_cm_simulation_usecase)

        response = controller(HttpRequest())

        assert response.status_code == 200
        assert response.body['message'] == 'the simulations were retrieved successfully'
        assert len(response.body['simulations']) == 0
