from typing import List
from src.shared.domain.entities.cm_simulation import CmSimulation


class CmSimulationViewModel:
    def __init__(self, cm_simulation: CmSimulation):
        self.simulation_id = cm_simulation.simulation_id
        self.xcg = cm_simulation.xcg
        self.xac_w = cm_simulation.xac_w
        self.sw = cm_simulation.sw
        self.st = cm_simulation.st
        self.cw = cm_simulation.cw
        self.ct = cm_simulation.ct
        self.iw = cm_simulation.iw
        self.it = cm_simulation.it
        self.lt = cm_simulation.lt
        self.cm_ac = cm_simulation.cm_ac
        self.cl_0 = cm_simulation.cl_0
        self.cl_alpha = cm_simulation.cl_alpha

    def to_dict(self):
        return {
            "simulation_id": self.simulation_id,
            "xcg": self.xcg,
            "xac_w": self.xac_w,
            "sw": self.sw,
            "st": self.st,
            "cw": self.cw,
            "ct": self.ct,
            "iw": self.iw,
            "it": self.it,
            "lt": self.lt,
            "cm_ac": self.cm_ac,
            "cl_0": self.cl_0,
            "cl_alpha": self.cl_alpha
        }

class GetAllCmSimulationViewModel:
    def __init__(self, simulations: List[CmSimulation]):
        self.simulations = [CmSimulationViewModel(simulation) for simulation in simulations]

    def to_dict(self):
        return {
            "simulations": [simulation.to_dict() for simulation in self.simulations],
            "message": "the simulations were retrieved successfully"
        }