from abc import ABC, abstractmethod
from typing import List, Optional

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
    def update_cm_simulation(self, simulation_id: str, new_xcg: Optional[float] = None, new_xac_w: Optional[float] = None, new_sw: Optional[float] = None, new_st: Optional[float] = None, new_cw: Optional[float] = None, new_ct: Optional[float] = None, new_iw: Optional[float] = None, new_it: Optional[float] = None, new_lt: Optional[float] = None, new_Cm_ac: Optional[float] = None, new_Cl_0: Optional[float] = None, new_Cl_alpha: Optional[float] = None) -> CmSimulation:
        """Updates a CmSimulation entity

        Args:
            simulation_id (str): The ID of the simulation to update
            new_xcg (Optional[float]): New xcg value
            new_xac_w (Optional[float]): New xac_w value
            new_sw (Optional[float]): New sw value
            new_st (Optional[float]): New st value
            new_cw (Optional[float]): New cw value
            new_ct (Optional[float]): New ct value
            new_iw (Optional[float]): New iw value
            new_it (Optional[float]): New it value
            new_lt (Optional[float]): New lt value
            new_Cm_ac (Optional[float]): New Cm_ac value
            new_Cl_0 (Optional[float]): New Cl_0 value
            new_Cl_alpha (Optional[float]): New Cl_alpha value

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

    