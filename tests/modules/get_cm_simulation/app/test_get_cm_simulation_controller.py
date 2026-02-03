from src.modules.get_cm_simulation.app.get_cm_simulation_controller import GetCmSimulationController
from src.modules.get_cm_simulation.app.get_cm_simulation_usecase import GetCmSimulationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock

class Test_GetCmSimulationController:
    def test_get_cm_simulation_controller_success(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)
        controller = GetCmSimulationController(usecase)

        simulation_id = repo.simulations[0].simulation_id

        request = HttpRequest(body={'simulation_id': simulation_id})
        
        response = controller(request)

        assert response.status_code == 200
        assert response.body['cm_simulation']['simulation_id'] == simulation_id
        assert response.body['message'] == "the cm simulation was retrieved successfully"

    def test_get_cm_simulation_controller_missing_parameter(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)
        controller = GetCmSimulationController(usecase)

        request = HttpRequest(body={})
        
        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field simulation_id is missing"

    def test_get_cm_simulation_controller_not_found(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)
        controller = GetCmSimulationController(usecase)

        request = HttpRequest(body={'simulation_id': "12345678-1234-1234-1234-123456789012"})

        response = controller(request)

        assert response.status_code == 404
        assert "No items found" in response.body

    def test_get_cm_simulation_controller_wrong_type(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)
        controller = GetCmSimulationController(usecase)

        request = HttpRequest(body={'simulation_id': 123})

        response = controller(request)

        assert response.status_code == 400
        assert "Field simulation_id isn't in the right type" in response.body
