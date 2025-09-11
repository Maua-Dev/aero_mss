from typing import List

from src.shared.domain.entities.CmSimulation import CmSimulation
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CmSimulationRepositoryMock(ICmSimulationRepository):
    simulations: List[CmSimulation]
    simulation_counter: int

    def __init__(self):
        self.simulations = [
            CmSimulation(simulation_id="1", xcg=0.5, xac_w=0.5, sw=1, st=1, cw=1, ct=1, iw=1, it=1, lt=1, Cm_ac=0.3, Cl_0=0.5, Cl_alpha=5),
            CmSimulation(simulation_id="2", xcg=0.2, xac_w=0.3, sw=1, st=1, cw=1, ct=1, iw=1, it=1, lt=1, Cm_ac=0.4, Cl_0=0.3, Cl_alpha=5),
            CmSimulation(simulation_id="3", xcg=0.3, xac_w=0.4, sw=1, st=1, cw=1, ct=1, iw=1, it=1, lt=1, Cm_ac=0.2, Cl_0=0.4, Cl_alpha=5)
        ]
        self.simulation_counter = 0

    def get_simulation(self, simulation_id: str) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.id == simulation_id:
                return simulation
        raise NoItemsFound("No simulation found with the given ID")
    
    def get_all_simulations(self) -> List[CmSimulation]:
        return self.simulations
    
    def create_simulation(self, new_simulation: CmSimulation) -> CmSimulation:
        self.simulations.append(new_simulation)
        self.simulation_counter += 1
        return new_simulation

    def delete_simulation(self, simulation_id: str) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.id == simulation_id:
                self.simulations.remove(simulation)
                self.simulation_counter -= 1
                return simulation
        raise NoItemsFound("No simulation found with the given ID")

    def update_simulation(self, simulation_id: str, new_name: str) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.id == simulation_id:
                simulation.name = new_name
                return simulation
        raise NoItemsFound("No simulation found with the given ID")

    def get_simulation_counter(self) -> int:
        return self.simulation_counter
