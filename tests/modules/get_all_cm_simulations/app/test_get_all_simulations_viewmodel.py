from src.modules.get_all_simulations.app.get_all__simulations_viewmodel import GetAllSimulationsViewModel, SimulationViewModel
from src.shared.domain.entities.cm_simulation import CmSimulation
import uuid


class Test_GetAllSimulationsViewModel:
    all_simulations_list = [
        CmSimulation(
            simulation_id=str(uuid.uuid4()),
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
        ),
        CmSimulation(
            simulation_id=str(uuid.uuid4()),
            xcg=0.2,
            xac_w=0.3,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.4,
            cl_0=0.3,
            cl_alpha=5.0
        ),
    ]

    def test_get_all_simulations_viewmodel(self):
        viewmodel = GetAllSimulationsViewModel(self.all_simulations_list)

        response = viewmodel.to_dict()

        assert response["message"] == "the simulations were retrieved successfully"
        assert len(response["simulations"]) == 2
        assert response["simulations"][0]["simulation_id"] == self.all_simulations_list[0].simulation_id
        assert response["simulations"][0]["xcg"] == self.all_simulations_list[0].xcg
        assert response["simulations"][0]["xac_w"] == self.all_simulations_list[0].xac_w
        assert response["simulations"][0]["sw"] == self.all_simulations_list[0].sw
        assert response["simulations"][0]["st"] == self.all_simulations_list[0].st
        assert response["simulations"][0]["cw"] == self.all_simulations_list[0].cw
        assert response["simulations"][0]["ct"] == self.all_simulations_list[0].ct
        assert response["simulations"][0]["iw"] == self.all_simulations_list[0].iw
        assert response["simulations"][0]["it"] == self.all_simulations_list[0].it
        assert response["simulations"][0]["lt"] == self.all_simulations_list[0].lt
        assert response["simulations"][0]["cm_ac"] == self.all_simulations_list[0].cm_ac
        assert response["simulations"][0]["cl_0"] == self.all_simulations_list[0].cl_0
        assert response["simulations"][0]["cl_alpha"] == self.all_simulations_list[0].cl_alpha
        assert response["simulations"][1]["simulation_id"] == self.all_simulations_list[1].simulation_id
        assert response["simulations"][1]["xcg"] == self.all_simulations_list[1].xcg

    def test_simulation_viewmodel(self):
        simulation_id = str(uuid.uuid4())
        simulation = CmSimulation(
            simulation_id=simulation_id,
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
        viewmodel = SimulationViewModel(simulation)

        response = viewmodel.to_dict()

        expected = {
            'simulation_id': simulation_id,
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
            'cl_alpha': 3.5
        }

        assert response == expected

    def test_get_all_simulations_viewmodel_empty_list(self):
        viewmodel = GetAllSimulationsViewModel([])

        response = viewmodel.to_dict()

        assert response["message"] == "the simulations were retrieved successfully"
        assert len(response["simulations"]) == 0
        assert response["simulations"] == []
