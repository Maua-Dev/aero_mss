from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.cm_simulation import CmSimulation


class ICmSimulationRepository(ABC):

    @abstractmethod
    def get_cm_simulation(self, simulation_id: str) -> CmSimulation:
        """Retreives a CmSimulation entity querying by simulation_id

        Args:
            simulation_id (str): simulation's uuid

        Raises:
            NoItemsFound: If no simulation is found with the given ID

        Returns:
            CmSimulation entity
        """
        pass

    @abstractmethod
    def get_all_cm_simulations(self) -> List[CmSimulation]:
        """Retrieves all CmSimulation entities

        Raises:
            NoItemsFound: If no simulations are found

        Returns:
            List[CmSimulation]: List of all CmSimulation entities
        """
        pass

    @abstractmethod
    def create_cm_simulation(self, new_simulation: CmSimulation) -> CmSimulation:
        """Creates a new CmSimulation entity

        Args:
            new_simulation (CmSimulation): The CmSimulation entity to create

        Raises:
            DuplicatedItem: If simulation with the same ID already exists

        Returns:
            CmSimulation: The created CmSimulation entity
        """
        pass

    @abstractmethod
    def delete_cm_simulation(self, simulation_id: str) -> CmSimulation:
        """Deletes a CmSimulation entity

        Args:
            simulation_id (str): The ID of the simulation to delete

        Raises:
            NoItemsFound: If no simulation is found with the given ID

        Returns:
            CmSimulation: The deleted CmSimulation entity
        """
        pass

    @abstractmethod
    def update_cm_simulation(self, simulation_id: str, new_name: str) -> CmSimulation:
        """Updates a CmSimulation entity

        Args:
            simulation_id (str): The ID of the simulation to update
            new_name (str): The new name for the simulation

        Raises:
            NoItemsFound: If no simulation is found with the given ID

        Returns:
            CmSimulation: The updated CmSimulation entity
        """
        pass

    @abstractmethod
    def get_cm_simulation_counter(self) -> int:
        """Retrieves the total count of CmSimulation entities

        Returns:
            int: The total count of CmSimulation entities
        """
        pass

    