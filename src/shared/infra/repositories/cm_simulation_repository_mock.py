from typing import List, Optional
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
            CmSimulation(simulation_id="d1e1e1e1-1111-4111-a111-111111111111", xcg=0.5, xac_w=0.5, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.3, cl_0=0.5, cl_alpha=5.0),
            CmSimulation(simulation_id="d2e2e2e2-2222-4222-a222-222222222222", xcg=0.2, xac_w=0.3, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.4, cl_0=0.3, cl_alpha=5.0),
            CmSimulation(simulation_id="d3e3e3e3-3333-4333-a333-333333333333", xcg=0.3, xac_w=0.4, sw=1.0, st=1.0, cw=1.0, ct=1.0, iw=1.0, it=1.0, lt=1.0, cm_ac=0.2, cl_0=0.4, cl_alpha=5.0)
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
        for simulation in self.simulations:
            if simulation.simulation_id == new_simulation.simulation_id:
                raise DuplicatedItem("Simulation ID")
        
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

    def update_cm_simulation(self, simulation_id: str, new_xcg: Optional[float] = None, new_xac_w: Optional[float] = None, new_sw: Optional[float] = None, new_st: Optional[float] = None, new_cw: Optional[float] = None, new_ct: Optional[float] = None, new_iw: Optional[float] = None, new_it: Optional[float] = None, new_lt: Optional[float] = None, new_Cm_ac: Optional[float] = None, new_Cl_0: Optional[float] = None, new_Cl_alpha: Optional[float] = None) -> CmSimulation:
        for simulation in self.simulations:
            if simulation.simulation_id == simulation_id:
                if new_xcg is not None:
                    simulation.xcg = new_xcg
                if new_xac_w is not None:
                    simulation.xac_w = new_xac_w
                if new_sw is not None:
                    simulation.sw = new_sw
                if new_st is not None:
                    simulation.st = new_st
                if new_cw is not None:
                    simulation.cw = new_cw
                if new_ct is not None:
                    simulation.ct = new_ct
                if new_iw is not None:
                    simulation.iw = new_iw
                if new_it is not None:
                    simulation.it = new_it
                if new_lt is not None:
                    simulation.lt = new_lt
                if new_Cm_ac is not None:
                    simulation.cm_ac = new_Cm_ac
                if new_Cl_0 is not None:
                    simulation.cl_0 = new_Cl_0
                if new_Cl_alpha is not None:
                    simulation.cl_alpha = new_Cl_alpha
                return simulation
        raise NoItemsFound("No simulation found with the given ID")

    def get_cm_simulation_counter(self) -> int:
        return self.simulation_counter
    
