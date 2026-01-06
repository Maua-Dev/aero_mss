from src.modules.delete_simulation.app.delete_simulation_controller import DeleteSimulationController
from src.modules.delete_simulation.app.delete_simulation_usecase import DeleteSimulationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock


class Test_DeleteSimulationController:
    def test_delete_simulation_controller(self):
            repo = CmSimulationRepositoryMock()
            usecase = DeleteSimulationUsecase(repo=repo)
            controller = DeleteSimulationController(delete_simulation_use_case=usecase)

            simulation_id = repo.simulations[0].simulation_id

            request = HttpRequest(body={
                'simulation_id': simulation_id
            })

            response = controller(request=request)

            assert response.status_code == 200
            assert response.body['message'] == 'the simulation was deleted successfully'

    def test_delete_simulation_controller_wrong_type(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo=repo)
        controller = DeleteSimulationController(delete_simulation_use_case=usecase)

        request = HttpRequest(body={
            'simulation_id': 'a'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field simulation_id is not valid"
            

    def test_delete_simulation_controller_missing_parameter(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo=repo)
        controller = DeleteSimulationController(delete_simulation_use_case=usecase)

        request = HttpRequest(body={})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field simulation_id is missing"

    def test_delete_simulation_controller_invalid_simulation_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo=repo)
        controller = DeleteSimulationController(delete_simulation_use_case=usecase)

        request = HttpRequest(body={
            'simulation_id': 999
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field simulation_id is not valid"    
        
    def test_delete_simulation_controller_no_items_found(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo=repo)
        controller = DeleteSimulationController(delete_simulation_use_case=usecase)

        request = HttpRequest(body={
            'simulation_id': '12345678-1234-1234-1234-123456789012'
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == 'No items found for No simulation found with the given ID'


