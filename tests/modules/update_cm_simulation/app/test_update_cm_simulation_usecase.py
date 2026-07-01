import pytest
from src.modules.update_cm_simulation.app.update_cm_simulation_usecase import UpdateCmSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import uuid

class Test_UpdateCmSimulationUsecase:
    def test_update_cm_simulation_usecase(self):
        repo = CmSimulationRepositoryMock()
        usecase = UpdateCmSimulationUsecase(repo=repo)
        simulation_to_update = repo.simulations[0]
        updated_simulation = usecase(
            simulation_id=simulation_to_update.simulation_id,
            new_xcg=0.6,
            new_xac_w=0.6,
            new_sw=1.1,
            new_st=1.1,
            new_cw=1.1,
            new_ct=1.1,
            new_iw=1.1,
            new_it=1.1,
            new_lt=1.1,
            new_Cm_ac=0.35,
            new_Cl_0=0.55,
            new_Cl_alpha=5.5
        )

        assert updated_simulation.xcg == 0.6
        assert updated_simulation.xac_w == 0.6
        assert updated_simulation.sw == 1.1
        assert updated_simulation.st == 1.1
        assert updated_simulation.cw == 1.1
        assert updated_simulation.ct == 1.1
        assert updated_simulation.iw == 1.1
        assert updated_simulation.it == 1.1
        assert updated_simulation.lt == 1.1
        assert updated_simulation.cm_ac == 0.35
        assert updated_simulation.cl_0 == 0.55
        assert updated_simulation.cl_alpha == 5.5

    def test_update_cm_simulation_usecase_wrong_simulation_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = UpdateCmSimulationUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                simulation_id=123,
                new_xcg=0.6,
                new_xac_w=0.6,
                new_sw=1.1,
                new_st=1.1,
                new_cw=1.1,
                new_ct=1.1,
                new_iw=1.1,
                new_it=1.1,
                new_lt=1.1,
                new_Cm_ac=0.35,
                new_Cl_0=0.55,
                new_Cl_alpha=5.5
            )