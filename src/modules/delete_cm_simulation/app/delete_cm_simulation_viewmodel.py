from src.shared.domain.entities.cm_simulation import CmSimulation

class DeleteCmSimulationViewmodel:
    simulation_id: str

    def __init__(self, simulation: CmSimulation):
        self.simulation_id = simulation.simulation_id

    def to_dict(self):
        return {
            'simulation_id': self.simulation_id,
            'message': "the cm simulation was deleted successfully"
        }