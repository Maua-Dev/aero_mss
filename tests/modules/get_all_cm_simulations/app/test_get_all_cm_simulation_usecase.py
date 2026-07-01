from src.modules.get_all_cm_simulation.app.get_all_cm_simulation_usecase import GetAllCmSimulationUsecase
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock


class Test_GetAllCmSimulationUsecase:

    def test_get_all_cm_simulation_usecase(self):
        repo_mock = CmSimulationRepositoryMock()
        usecase = GetAllCmSimulationUsecase(repo_mock)

        all_simulations_list_returned = usecase()

        assert all_simulations_list_returned == repo_mock.simulations
        assert len(all_simulations_list_returned) == 3
        assert len(all_simulations_list_returned) == len(repo_mock.simulations)

    def test_get_all_cm_simulation_usecase_empty_repository(self):
        repo_mock = CmSimulationRepositoryMock()
        repo_mock.simulations = []
        usecase = GetAllCmSimulationUsecase(repo_mock)

        all_simulations_list_returned = usecase()

        assert all_simulations_list_returned == []
        assert len(all_simulations_list_returned) == 0
