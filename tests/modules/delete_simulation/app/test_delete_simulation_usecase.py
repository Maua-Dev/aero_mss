import pytest

from src.modules.delete_simulation.app.delete_simulation_usecase import DeleteSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock


class Test_DeleteUserUsecase:
    def test_delete_simulation(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo)

        lenBefore = len(repo.simulations)
        
        simulation_id = repo.simulations[0].simulation_id
        simulation = usecase(simulation_id)

        assert len(repo.simulations) == lenBefore - 1

    def test_delete_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo)

        with pytest.raises(NoItemsFound):
            # Using a valid UUID format that doesn't exist in the repository
            simulation = usecase("12345678-1234-1234-1234-123456789012")

    def test_delete_simulation_invalid_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteSimulationUsecase(repo)

        with pytest.raises(EntityError):
            simulation = usecase("invalid-id-not-uuid-format")
