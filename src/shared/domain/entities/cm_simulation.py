from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.domain_errors import XcgError, XacWerror, SwError, StError, CwError, CtError, IwError, ItError, LtError, CmAcError, Cl0Error, ClAlphaError   
import uuid

class CmSimulation:
    #geometria 
    simulation_id: str #Identificador único da simulação
    Xcg: float #Posição do Centro de Gravidade (CG) / Positivo ou negativo (0,25 = 25% da corda)
    Xac_w: float #Posição do Centro Aerodinâmico (AC) / Valor positivo e fixo
    Sw: float #Área da Asa (m²) / Deve ser um valor positivo.
    St: float #Área da Empenagem Horizontal (Tail Area) / Deve ser um valor positivo
    cw: float #Corda Média Aerodinâmica da Asa (Wing Mean Aerodynamic Chord) / Deve ser um valor positivo. Medido em metros.
    ct: float #Corda Média Aerodinâmica da Empenagem Horizontal (Tail Mean Aerodynamic Chord) / Deve ser um valor positivo. Medido em metros.
    iw: float #Ângulo de Incidência da Asa (Wing Incidence Angle) / Pode ser positivo ou negativo ou zero. Medido em graus. No código, ele é fornecido em graus e convertido para radianos.
    it: float #Ângulo de Incidência da Empenagem Horizontal (Tail Incidence Angle) / Pode ser positivo ou negativo ou zero. Medido em graus.
    lt: float #Braço de Cauda (Tail Arm) / Deve ser um valor positivo. Quanto maior o braço de cauda, mais "autoridade" (capacidade de gerar momento) a empenagem tem.
    #aero
    Cm_ac: float #Coeficiente de Momento no Centro Aerodinâmico / Geralmente um valor pequeno, negativo ou zero.
    Cl_0: float #Coeficiente de Sustentação com Ângulo de Ataque Zero / Positivo ou zero.
    Cl_alpha: float #Inclinação da Curva de Sustentação (Lift Curve Slope) / É sempre positivo antes do estol(stall). Teoricamente, para um aerofólio 2D, é 2\pi por radiano. Para uma asa 3D finita, é sempre menor que 2\pi.
    
    def __init__(self, 
                 simulation_id: str,
                 xcg: float, 
                 xac_w: float, 
                 sw: float, 
                 st: float, 
                 cw: float, 
                 ct: float, 
                 iw: float, 
                 it: float, 
                 lt: float, 
                 cm_ac: float, 
                 cl_0: float, 
                 cl_alpha: float):
        
        if not CmSimulation.validate_simulation_id(simulation_id):
            raise EntityError("simulation_id")
        self.simulation_id = simulation_id
        
        if not CmSimulation.validate_xcg(xcg):
          raise EntityError("xcg")
        self.xcg = xcg

        if not CmSimulation.validate_xac_w(xac_w):
          raise EntityError("xac_w")
        self.xac_w = xac_w

        if not CmSimulation.validate_sw(sw):
          raise EntityError("sw")
        self.sw = sw

        if not CmSimulation.validate_st(st):
            raise EntityError("st")
        self.st = st

        if not CmSimulation.validate_cw(cw):
            raise EntityError("cw")
        self.cw = cw

        if not CmSimulation.validate_ct(ct):
            raise EntityError("ct")
        self.ct = ct

        if not CmSimulation.validate_iw(iw):
            raise EntityError("iw")
        self.iw = iw

        if not CmSimulation.validate_it(it):
            raise EntityError("it")
        self.it = it

        if not CmSimulation.validate_lt(lt):
            raise EntityError("lt")
        self.lt = lt

        if not CmSimulation.validate_cm_ac(cm_ac):
            raise EntityError("cm_ac")
        self.cm_ac = cm_ac

        if not CmSimulation.validate_cl_0(cl_0):
            raise EntityError("cl_0")
        self.cl_0 = cl_0

        if not CmSimulation.validate_cl_alpha(cl_alpha):
            raise EntityError("cl_alpha")
        self.cl_alpha = cl_alpha


# Validações

    @staticmethod
    def validate_simulation_id(simulation_id: str) -> bool:
        if simulation_id is None:
            return False
        elif type(simulation_id) != str:
            return False
        elif len(simulation_id) == 0:
            return False
        elif len(simulation_id) != 36:
            return False     
        return True
    
    @staticmethod
    def validate_xcg(xcg: float) -> bool:
        if xcg is None:
            return False
        elif type(xcg) != float:
            return False
        elif xcg < -1 or xcg > 1:
            return False
        return True
    
    @staticmethod
    def validate_xac_w(xac_w: float) -> bool:
        if xac_w is None:
            return False
        elif type(xac_w) != float:
            return False
        elif xac_w < 0 or xac_w > 1:
            return False
        return True
    
    @staticmethod
    def validate_sw(sw: float) -> bool:
        if sw is None:
            return False
        elif type(sw) != float:
            return False
        elif sw <= 0:
            return False
        return True
    
    @staticmethod
    def validate_st(st: float) -> bool:
        if st is None:
            return False
        elif type(st) != float:
            return False
        elif st <= 0:
            return False
        return True
    
    @staticmethod
    def validate_cw(cw: float) -> bool:
        if cw is None:
            return False
        elif type(cw) != float:
            return False
        elif cw <= 0:
            return False
        return True
    
    @staticmethod
    def validate_ct(ct: float) -> bool:
        if ct is None:
            return False
        elif type(ct) != float:
            return False
        elif ct <= 0:
            return False
        return True
    
    @staticmethod
    def validate_iw(iw: float) -> bool:
        if iw is None:
            return False
        elif type(iw) != float:
            return False
        elif iw < -10 or iw > 10:
            return False
        return True
    
    @staticmethod
    def validate_it(it: float) -> bool:
        if it is None:
            return False
        elif type(it) != float:
            return False
        elif it < -10 or it > 10:
            return False
        return True
    
    @staticmethod
    def validate_lt(lt: float) -> bool:
        if lt is None:
            return False
        elif type(lt) != float:
            return False
        elif lt <= 0:
            return False
        return True
    
    @staticmethod
    def validate_cm_ac(cm_ac: float) -> bool:
        if cm_ac is None:
            return False
        elif type(cm_ac) != float:
            return False
        elif cm_ac < -0.5 or cm_ac > 0.5:
            return False
        return True
    
    @staticmethod
    def validate_cl_0(cl_0: float) -> bool: 
        if cl_0 is None:
            return False
        elif type(cl_0) != float:
            return False
        elif cl_0 < -1 or cl_0 > 1:
            return False
        return True
    
    @staticmethod
    def validate_cl_alpha(cl_alpha: float) -> bool: 
        if cl_alpha is None:
            return False
        elif type(cl_alpha) != float:
            return False
        elif cl_alpha <= 0 or cl_alpha > 10:
            return False
        return True
    
    def __repr__(self):
        return f"CmSimulation(xcg={self.xcg}, xac_w={self.xac_w}, sw={self.sw}, st={self.st}, cw={self.cw}, ct={self.ct}, iw={self.iw}, it={self.it}, lt={self.lt}, cm_ac={self.cm_ac}, cl_0={self.cl_0}, cl_alpha={self.cl_alpha})"