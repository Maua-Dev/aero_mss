from src.modules.get_cm_simulation.app.get_cm_simulation_viewmodel import GetCmSimulationViewmodel
from src.shared.domain.entities.cm_simulation import CmSimulation
import uuid

class Test_GetCmSimulationViewmodel:
    def test_get_cm_simulation_viewmodel(self):
        simulation_id = str(uuid.uuid4())
        simulation = CmSimulation(
            simulation_id=simulation_id,
            xcg=0.5,
            xac_w=0.5,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.3,
            cl_0=0.5,
            cl_alpha=5.0
        )

        viewmodel = GetCmSimulationViewmodel(simulation)
        result = viewmodel.to_dict()

        expected = {
            'cm_simulation': {
                'simulation_id': simulation_id,
                'xcg': 0.5,
                'xac_w': 0.5,
                'sw': 1.0,
                'st': 1.0,
                'cw': 1.0,
                'ct': 1.0,
                'iw': 1.0,
                'it': 1.0,
                'lt': 1.0,
                'cm_ac': 0.3,
                'cl_0': 0.5,
                'cl_alpha': 5.0,
            },
            'message': "the cm simulation was retrieved successfully"
        }

        assert result == expected

    def test_get_cm_simulation_viewmodel_values(self):
        simulation_id = str(uuid.uuid4())
        simulation = CmSimulation(
            simulation_id=simulation_id,
            xcg=0.5,
            xac_w=0.5,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.3,
            cl_0=0.5,
            cl_alpha=5.0
        )

        viewmodel = GetCmSimulationViewmodel(simulation)
        result = viewmodel.to_dict()

        assert result['cm_simulation']['xcg'] == 0.5
        assert result['cm_simulation']['cm_ac'] == 0.3

    def test_get_cm_simulation_viewmodel_message(self):
        simulation_id = str(uuid.uuid4())
        simulation = CmSimulation(
            simulation_id=simulation_id,
            xcg=0.5,
            xac_w=0.5,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.3,
            cl_0=0.5,
            cl_alpha=5.0
        )

        viewmodel = GetCmSimulationViewmodel(simulation)
        result = viewmodel.to_dict()

        assert result['message'] == "the cm simulation was retrieved successfully"
