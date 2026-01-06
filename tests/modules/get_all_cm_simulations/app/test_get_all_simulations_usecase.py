from src.modules.get_all_simulations.app.get_all_simulations_usecase import GetAllSimulationsUsecase
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock


class Test_GetAllSimulationsUsecase:

    def test_get_all_simulations_usecase(self):
        repo_mock = CmSimulationRepositoryMock()
        usecase = GetAllSimulationsUsecase(repo_mock)

        all_simulations_list_returned = usecase()

        assert all_simulations_list_returned == repo_mock.simulations
        assert len(all_simulations_list_returned) == 3
        assert len(all_simulations_list_returned) == len(repo_mock.simulations)

    def test_get_all_simulations_usecase_empty_repository(self):
        repo_mock = CmSimulationRepositoryMock()
        repo_mock.simulations = []
        usecase = GetAllSimulationsUsecase(repo_mock)

        all_simulations_list_returned = usecase()

        assert all_simulations_list_returned == []
        assert len(all_simulations_list_returned) == 0
