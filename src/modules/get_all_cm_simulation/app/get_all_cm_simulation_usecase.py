from src.shared.domain.entities.cm_simulation import CmSimulation
from typing import List
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository


class GetAllCmSimulationUsecase:
    def __init__(self, repo: ICmSimulationRepository):
        self.repo = repo

    def __call__(self) -> List[CmSimulation]:
        all_simulations_list = self.repo.get_all_cm_simulations()

        return all_simulations_list