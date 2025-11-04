from src.modules.create_cm_simulation.app.create_cm_simulation_viewmodel import CreateCmSimulationViewmodel
from src.shared.domain.entities.cm_simulation import CmSimulation
import uuid

class Test_CreateCmSimulationViewModel:
    def test_create_cm_simulation_viewmodel(self):
        id_esperado = str(uuid.uuid4())
        cm_simulation = CmSimulation(
            simulation_id=id_esperado,
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
        cmSimulationViewmodel = CreateCmSimulationViewmodel(cm_simulation=cm_simulation).to_dict()

        expected = {
            'simulation_id': id_esperado,
            'xcg': 0.25,
            'xac_w': 0.9,
            'sw': 0.5,
            'st': 0.5,
            'cw': 2.0,
            'ct': 1.0,
            'iw': 1.0,
            'it': 2.0,
            'lt': 3.0,
            'cm_ac': -0.05,
            'cl_0': 0.0,
            'cl_alpha': 3.5,
            'message': 'the CM simulation was created successfully'
        }

        assert expected == cmSimulationViewmodel