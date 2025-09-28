from typing import List
import uuid

from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, DuplicatedItem


class CmSimulationRepositoryMock(ICmSimulationRepository):
    simulations: List[CmSimulation]
    simulation_counter: int

    def __init__(self):
        self.simulations = [
            CmSimulation(simulation_id=str(uuid.uuid4()), xcg=0.5, xac_w=0.5, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.3, cl_0=0.5, cl_alpha=5.0),
            CmSimulation(simulation_id=str(uuid.uuid4()), xcg=0.2, xac_w=0.3, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.4, cl_0=0.3, cl_alpha=5.0),
            CmSimulation(simulation_id=str(uuid.uuid4()), xcg=0.3, xac_w=0.4, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.2, cl_0=0.4, cl_alpha=5.0)
        ]
        self.simulation_counter = 3

    def get_cm_simulation(self, simulation_id: str) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.simulation_id == simulation_id:
                return simulation
        raise NoItemsFound("No simulation found with the given ID")
    
    def get_all_cm_simulations(self) -> List[CmSimulation]:
        return self.simulations
    
    def create_cm_simulation(self, new_simulation: CmSimulation) -> CmSimulation:    
        self.simulations.append(new_simulation)
        self.simulation_counter += 1
        return new_simulation

    def delete_cm_simulation(self, simulation_id: str) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.simulation_id == simulation_id:
                self.simulations.remove(simulation)
                self.simulation_counter -= 1
                return simulation
        raise NoItemsFound("No simulation found with the given ID")

    def update_cm_simulation(self, simulation_id: str, new_xcg: float, new_xac_w: float, new_sw: float, new_st: float, new_cw: float, new_ct: float, new_iw: float, new_it: float, new_lt: float, new_Cm_ac: float, new_Cl_0: float, new_Cl_alpha: float) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.simulation_id == simulation_id:
                simulation.xcg = new_xcg
                simulation.xac_w = new_xac_w
                simulation.sw = new_sw
                simulation.st = new_st
                simulation.cw = new_cw
                simulation.ct = new_ct
                simulation.iw = new_iw
                simulation.it = new_it
                simulation.lt = new_lt
                simulation.cm_ac = new_Cm_ac
                simulation.cl_0 = new_Cl_0
                simulation.cl_alpha = new_Cl_alpha
                return simulation
        raise NoItemsFound("No simulation found with the given ID")

    def get_cm_simulation_counter(self) -> int:
        return self.simulation_counter
    
