import pytest

from src.modules.delete_cm_simulation.app.delete_cm_simulation_usecase import DeleteCmSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock


class Test_DeleteCmSimulationUsecase:
    def test_delete_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteCmSimulationUsecase(repo)

        lenBefore = len(repo.simulations)
        
        simulation_id = repo.simulations[0].simulation_id
        simulation = usecase(simulation_id)

        assert len(repo.simulations) == lenBefore - 1

    def test_delete_cm_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteCmSimulationUsecase(repo)

        with pytest.raises(NoItemsFound):
            # Using a valid UUID format that doesn't exist in the repository
            simulation = usecase("12345678-1234-1234-1234-123456789012")

    def test_delete_cm_simulation_invalid_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = DeleteCmSimulationUsecase(repo)

        with pytest.raises(EntityError):
            simulation = usecase("invalid-id-not-uuid-format")
