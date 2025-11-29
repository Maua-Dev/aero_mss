from src.modules.delete_simulation.app.delete_simulation_viewmodel import DeleteSimulationViewmodel
from src.shared.domain.entities.cm_simulation import CmSimulation
import uuid


class Test_DeleteSimulationViewmodel:
    def test_delete_simulation_viewmodel(self):
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

        delete_simulation_viewmodel = DeleteSimulationViewmodel(simulation)

        expected = {
            'simulation_id': simulation_id,
            'message': 'the simulation was deleted successfully'
        }

        assert expected == delete_simulation_viewmodel.to_dict()
