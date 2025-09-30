from src.shared.domain.entities.cm_simulation import CMSimulation

class CMSimulationDynamoDTO:
    simulation_id: str
    Xcg: float
    Xac_w: float
    Sw: float
    St: float
    Cw: float
    Ct: float
    Iw: float
    It: float
    Lt: float
    Cm_ac: float
    Cl_0: float
    Cl_alpha: float
    
    def __init__(self, simulation_id: str, xcg: float, xac_w: float, sw: float, st: float, cw: float, ct: float, iw: float, it: float, lt: float, cm_ac: float, cl_0: float, cl_alpha: float):
        self.simulation_id = simulation_id
        self.xcg = xcg
        self.xac_w = xac_w
        self.sw = sw
        self.st = st
        self.cw = cw
        self.ct = ct
        self.iw = iw
        self.it = it
        self.lt = lt
        self.cm_ac = cm_ac
        self.cl_0 = cl_0
        self.cl_alpha = cl_alpha

    @staticmethod
    def from_entity(cm_simulation: CMSimulation) -> "CMSimulationDynamoDTO":
        """
        Parse data from CMSimulation to CMSimulationDynamoDTO
        """
        return CMSimulationDynamoDTO(
            simulation_id=cm_simulation.simulation_id,
            xcg=cm_simulation.xcg,
            xac_w=cm_simulation.xac_w,
            sw=cm_simulation.sw,
            st=cm_simulation.st,
            cw=cm_simulation.cw,
            ct=cm_simulation.ct,
            iw=cm_simulation.iw,
            it=cm_simulation.it,
            lt=cm_simulation.lt,
            cm_ac=cm_simulation.cm_ac,
            cl_0=cm_simulation.cl_0,
            cl_alpha=cm_simulation.cl_alpha
        )
    
    def to_dynamo(self) -> dict:
        """
        Parse data from CMSimulationDynamoDTO to dict
        """
        return {
            "entity": "cm_simulation",
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
    
    @staticmethod
    def from_dynamo(cm_simulation_data: dict) -> "CMSimulationDynamoDTO ":
        """
        Parse data from DynamoDB to CMSimulationDynamoDTO
        @param cm_simulation_data: dict from DynamoDB
        """
        return CMSimulationDynamoDTO(
            simulation_id=str(cm_simulation_data["simulation_id"]),
            xcg=float(cm_simulation_data["xcg"]),
            xac_w=float(cm_simulation_data["xac_w"]),
            sw=float(cm_simulation_data["sw"]),
            st=float(cm_simulation_data["st"]),
            cw=float(cm_simulation_data["cw"]),
            ct=float(cm_simulation_data["ct"]),
            iw=float(cm_simulation_data["iw"]),
            it=float(cm_simulation_data["it"]),
            lt=float(cm_simulation_data["lt"]),
            cm_ac=float(cm_simulation_data["cm_ac"]),
            cl_0=float(cm_simulation_data["cl_0"]),
            cl_alpha=float(cm_simulation_data["cl_alpha"])
        )
    
    def to_entity(self) -> CMSimulation:
        """
        Parse data from CMSimulationDynamoDTO to CMSimulation
        """
        return CMSimulation(
            simulation_id=self.simulation_id,
            xcg=self.xcg,
            xac_w=self.xac_w,
            sw=self.sw,
            st=self.st,
            cw=self.cw,
            ct=self.ct,
            iw=self.iw,
            it=self.it,
            lt=self.lt,
            cm_ac=self.cm_ac,
            cl_0=self.cl_0,
            cl_alpha=self.cl_alpha
        )
    
    def __repr__(self):
        return f"CMSimulationDynamoDTO(simulation_id={self.simulation_id}, xcg={self.xcg}, xac_w={self.xac_w}, sw={self.sw}, st={self.st}, cw={self.cw}, ct={self.ct}, iw={self.iw}, it={self.it}, lt={self.lt}, cm_ac={self.cm_ac}, cl_0={self.cl_0}, cl_alpha={self.cl_alpha})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__