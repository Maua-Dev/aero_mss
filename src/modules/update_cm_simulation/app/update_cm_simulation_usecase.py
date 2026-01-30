from typing import Optional
from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.helpers.errors.domain_errors import EntityError

class UpdateCmSimulationUsecase:
    def __init__(self, repo: ICmSimulationRepository):
        self.repo = repo

    def __call__(self, 
                simulation_id: str, 
                new_xcg: Optional[float] = None, 
                new_xac_w: Optional[float] = None, 
                new_sw: Optional[float] = None, 
                new_st: Optional[float] = None, 
                new_cw: Optional[float] = None, 
                new_ct: Optional[float] = None, 
                new_iw: Optional[float] = None, 
                new_it: Optional[float] = None, 
                new_lt: Optional[float] = None, 
                new_Cm_ac: Optional[float] = None, 
                new_Cl_0: Optional[float] = None, 
                new_Cl_alpha: Optional[float] = None
            ) -> CmSimulation:

        if type(simulation_id) != str:
            raise EntityError("simulation_id")
        
        if new_xcg is not None and type(new_xcg) != float:
            raise EntityError("xcg")
        
        if new_xac_w is not None and type(new_xac_w) != float:
            raise EntityError("xac_w")
        
        if new_sw is not None and type(new_sw) != float:
            raise EntityError("sw")
        
        if new_st is not None and type(new_st) != float:
            raise EntityError("st")
        
        if new_cw is not None and type(new_cw) != float:
            raise EntityError("cw")
        
        if new_ct is not None and type(new_ct) != float:
            raise EntityError("ct")
        
        if new_iw is not None and type(new_iw) != float:
            raise EntityError("iw")
        
        if new_it is not None and type(new_it) != float:
            raise EntityError("it")
        
        if new_lt is not None and type(new_lt) != float:
            raise EntityError("lt")
        
        if new_Cm_ac is not None and type(new_Cm_ac) != float:
            raise EntityError("Cm_ac")
        
        if new_Cl_0 is not None and type(new_Cl_0) != float:
            raise EntityError("Cl_0")
        
        if new_Cl_alpha is not None and type(new_Cl_alpha) != float:
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