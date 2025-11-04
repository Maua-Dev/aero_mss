from src.shared.domain.entities.cm_simulation import Simulation
from src.shared.domain.enums.state_enum import STATE 

class DeleteSimulationViewmodel:
    simulation_id: int
    state: STATE

    def __init__(self, simulation: Simulation):
        self.simulation_id = simulation.simulation_id
        self.state = simulation.state

    def to_dict(self):
        return {
            'simulation_id': self.simulation_id,
            'state': self.state.value,
            'message': "the simulation was deleted successfully"
        }