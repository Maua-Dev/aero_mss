import pytest
from src.modules.get_cm_simulation.app.get_cm_simulation_usecase import GetCmSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock

class Test_GetCmSimulationUsecase:
    def test_get_cm_simulation_success(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)

        simulation_id = repo.simulations[0].simulation_id
        simulation = usecase(simulation_id)

        assert simulation.simulation_id == simulation_id
        assert simulation.xcg == repo.simulations[0].xcg

    def test_get_cm_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase("12345678-1234-1234-1234-123456789012")

    def test_get_cm_simulation_invalid_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = GetCmSimulationUsecase(repo)

        with pytest.raises(EntityError):
            usecase(123)
