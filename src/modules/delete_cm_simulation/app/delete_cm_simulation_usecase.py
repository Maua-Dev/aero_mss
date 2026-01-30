from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.domain_errors import EntityError

class DeleteCmSimulationUsecase:
    def __init__(self, repo: ICmSimulationRepository):
        self.repo = repo

    def __call__(self, simulation_id: str) -> CmSimulation:

        if type(simulation_id) != str:
            raise EntityError("simulation_id")
        
        if not CmSimulation.validate_simulation_id(simulation_id):
            raise EntityError("simulation_id")

        simulation = self.repo.delete_cm_simulation(simulation_id)

        return simulation