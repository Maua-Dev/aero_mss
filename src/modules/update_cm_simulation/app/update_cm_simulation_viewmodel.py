from src.shared.domain.entities.cm_simulation import CmSimulation

class UpdateCmSimulationViewmodel:
    simulation_id: int
    title: str
    description: str
    is_active: bool

    def __init__(self, cm_simulation: CmSimulation):
        self.simulation_id = cm_simulation.simulation_id
        self.title = cm_simulation.title
        self.description = cm_simulation.description
        self.is_active = cm_simulation.is_active

    def to_dict(self):
        return {
            'simulation_id': self.simulation_id,
            'title': self.title,
            'description': self.description,
            'is_active': self.is_active,
            'message': "the CM simulation was updated successfully"
        }