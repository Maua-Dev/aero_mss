from 

class GetAllSimulationsViewModel:
    def __init__(self, simulations):
        self.simulations = simulations

    def to_dict(self):
        return {
            "simulations": [simulation.to_dict() for simulation in self.simulations]
        }