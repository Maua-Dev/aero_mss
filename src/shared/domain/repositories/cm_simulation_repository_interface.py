from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.cm_simulation import CmSimulation


class ICmSimulationRepository(ABC):

    @abstractmethod
    def get_simulation(self, simulation_id: str) -> CmSimulation:
        """
        If simulation not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_simulations(self) -> List[CmSimulation]:
        """
        If simulations not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def create_simulation(self, new_simulation: CmSimulation) -> CmSimulation:
        """
        Creates a new simulation
        """
        pass

    @abstractmethod
    def delete_simulation(self, simulation_id: str) -> CmSimulation:
        """
        If simulation not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_simulation(self, simulation_id: str, new_name: str) -> CmSimulation:
        """
        If user not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_simulation_counter(self) -> int:
        """
        Returns the number of all simulations that have ever been created
        """
        pass

    