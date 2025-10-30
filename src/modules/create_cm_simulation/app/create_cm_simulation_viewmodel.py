from src.shared.domain.entities.cm_simulation import CMSimulation

class CreateCMSimulationViewmodel:
    simulation_id: str
    xcg: float
    xac_w: float
    sw: float
    st: float
    cw: float
    ct: float
    iw: float
    it: float
    lt: float
    cm_ac: float
    cl_0: float
    cl_alpha: float

    def __init__(self, cm_simulation: CMSimulation):
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
            'simulation_id': self.simulation_id,
            'xcg': self.xcg,
            'xac_w': self.xac_w,
            'sw': self.sw,
            'st': self.st,
            'cw': self.cw,
            'ct': self.ct,
            'iw': self.iw,
            'it': self.it,
            'lt': self.lt,
            'cm_ac': self.cm_ac,
            'cl_0': self.cl_0,
            'cl_alpha': self.cl_alpha,
            'message': "the CM simulation was created successfully"
        }