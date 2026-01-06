import pytest
from src.modules.create_cm_simulation.app.create_cm_simulation_usecase import CreateCmSimulationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import uuid

class Test_CreateCmSimulationUsecase:
    def test_create_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        usecase = CreateCmSimulationUsecase(repo)
        id_esperado = str(uuid.uuid4())
        simulation = usecase(
            simulation_id=id_esperado,
            xcg=0.4,
            xac_w=0.4,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.35,
            cl_0=0.45,
            cl_alpha=5.0
        )

        assert repo.simulations[-1] == simulation

    def test_create_cm_simulation_invalid_xcg(self):
        repo = CmSimulationRepositoryMock()
        usecase = CreateCmSimulationUsecase(repo)
        id_esperado = str(uuid.uuid4())
        with pytest.raises(EntityError):
            simulation = usecase(
                simulation_id=id_esperado,
                xcg='0.4',
                xac_w=0.4,
                sw=1.0,
                st=1.0,
                cw=1.0,
                ct=1.0,
                iw=1.0,
                it=1.0,
                lt=1.0,
                cm_ac=0.35,
                cl_0=0.45,
                cl_alpha=5.0
            )