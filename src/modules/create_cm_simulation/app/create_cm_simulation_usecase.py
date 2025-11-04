from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.domain_errors import EntityError

class CreateCmSimulationUsecase:
    def __init__(self, repo: ICmSimulationRepository):
        self.repo = repo

    def __call__(self, 
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
                 cl_alpha: float
                 ) -> CmSimulation:

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

        cm_simulation = CmSimulation(
            simulation_id=simulation_id,
            xcg=xcg,
            xac_w=xac_w,
            sw=sw,
            st=st,
            cw=cw,
            ct=ct,
            iw=iw,
            it=it,
            lt=lt,
            cm_ac=cm_ac,
            cl_0=cl_0,
            cl_alpha=cl_alpha
        )

        return self.repo.create_cm_simulation(cm_simulation)