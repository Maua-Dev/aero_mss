from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.domain_errors import EntityError

class UpdateCmSimulationUsecase:
    def __init__(self, repo: ICmSimulationRepository):
        self.repo = repo

    def __call__(self, 
                simulation_id: str, 
                new_xcg: float, 
                new_xac_w: float, 
                new_sw: float, 
                new_st: float, 
                new_cw: float, 
                new_ct: float, 
                new_iw: float, 
                new_it: float, 
                new_lt: float, 
                new_Cm_ac: float, 
                new_Cl_0: float, 
                new_Cl_alpha: float
            ) -> CmSimulation:

        if type(simulation_id) != str:
            raise EntityError("simulation_id")
        
        if type(new_xcg) != float:
            raise EntityError("xcg")
        
        if type(new_xac_w) != float:
            raise EntityError("xac_w")
        
        if type(new_sw) != float:
            raise EntityError("sw")
        
        if type(new_st) != float:
            raise EntityError("st")
        
        if type(new_cw) != float:
            raise EntityError("cw")
        
        if type(new_ct) != float:
            raise EntityError("ct")
        
        if type(new_iw) != float:
            raise EntityError("iw")
        
        if type(new_it) != float:
            raise EntityError("it")
        
        if type(new_lt) != float:
            raise EntityError("lt")
        
        if type(new_Cm_ac) != float:
            raise EntityError("Cm_ac")
        
        if type(new_Cl_0) != float:
            raise EntityError("Cl_0")
        
        if type(new_Cl_alpha) != float:
            raise EntityError("Cl_alpha")

        updated_simulation = self.repo.update_cm_simulation(
            simulation_id=simulation_id, 
            new_xcg=new_xcg, 
            new_xac_w=new_xac_w, 
            new_sw=new_sw, 
            new_st=new_st, 
            new_cw=new_cw, 
            new_ct=new_ct, 
            new_iw=new_iw, 
            new_it=new_it, 
            new_lt=new_lt, 
            new_Cm_ac=new_Cm_ac, 
            new_Cl_0=new_Cl_0, 
            new_Cl_alpha=new_Cl_alpha
        )

        return updated_simulation