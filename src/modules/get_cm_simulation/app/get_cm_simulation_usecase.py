from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.external.observability.observability_aws import ObservabilityAWS

class GetCmSimulationUsecase:
    def __init__(
        self, repo: ICmSimulationRepository
        # observability: ObservabilityAWS
    ):
        self.repo = repo
        # self.observability = observability

    def __call__(self, simulation_id: str) -> CmSimulation:
        # self.observability.log_usecase_in()
        
        if not CmSimulation.validate_simulation_id(simulation_id):
            raise EntityError("simulation_id")
        
        cm_simulation = self.repo.get_cm_simulation(simulation_id)
        # self.observability.log_usecase_out()
        return cm_simulation