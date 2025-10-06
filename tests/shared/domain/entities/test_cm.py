from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.helpers.errors.domain_errors import EntityError
import pytest
import uuid

class Test_CmSimulation:
    def test_cm_simulation(self):
        CmSimulation(
            simulation_id=str(uuid.uuid4()),
            xcg=0.25,
            xac_w=0.9,
            sw=0.5,
            st=0.5,
            cw=2.0,
            ct=1.0,
            iw=1.0,
            it=2.0,
            lt=3.0,
            cm_ac=-0.05,
            cl_0=0.0,
            cl_alpha=3.5
        )

    def test_cm_simulation_simulation_id_is_none(self):
        with pytest.raises(EntityError):
            CmSimulation(
                simulation_id=None,
                xcg=0.25,
                xac_w=0.9,
                sw=0.5,
                st=0.5,
                cw=2.0,
                ct=1.0,
                iw=1.0,
                it=2.0,
                lt=3.0,
                cm_ac=-0.05,
                cl_0=0.0,
                cl_alpha=3.5
            )

    def test_cm_simulation_simulation_id_is_not_str(self):
        with pytest.raises(EntityError):
            CmSimulation(
                simulation_id=1,
                xcg=0.25,
                xac_w=0.9,
                sw=0.5,
                st=0.5,
                cw=2.0,
                ct=1.0,
                iw=1.0,
                it=2.0,
                lt=3.0,
                cm_ac=-0.05,
                cl_0=0.0,
                cl_alpha=3.5
            )

    def test_cm_simulation_xcg_is_none(self):
        with pytest.raises(EntityError):
            CmSimulation(
                simulation_id=str(uuid.uuid4()),
                xcg=None,
                xac_w=0.9,
                sw=0.5,
                st=0.5,
                cw=2.0,
                ct=1.0,
                iw=1.0,
                it=2.0,
                lt=3.0,
                cm_ac=-0.05,
                cl_0=0.0,
                cl_alpha=3.5
            )

    def test_cm_simulation_xcg_is_not_float(self):
        with pytest.raises(EntityError):
            CmSimulation(
                simulation_id=str(uuid.uuid4()),
                xcg="0.25",
                xac_w=0.9,
                sw=0.5,
                st=0.5,
                cw=2.0,
                ct=1.0,
                iw=1.0,
                it=2.0,
                lt=3.0,
                cm_ac=-0.05,
                cl_0=0.0,
                cl_alpha=3.5
            )