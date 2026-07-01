import os

import pytest
from src.shared.infra.repositories.cm_simulation_repository_dynamo import CmSimulationRepositoryDynamo
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock

class Test_CmSimulationRepositoryDynamo:
    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_cm_simulation(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        cm_simulation_repository_mock = CmSimulationRepositoryMock()
        resp = cm_simulation_repository.create_cm_simulation(cm_simulation_repository_mock.simulations[0])

        assert cm_simulation_repository_mock.simulations[0].simulation_id == resp.simulation_id
        assert cm_simulation_repository_mock.simulations[0].xcg == resp.xcg

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_cm_simulation(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        cm_simulation_repository_mock = CmSimulationRepositoryMock()
        resp = cm_simulation_repository.get_cm_simulation(cm_simulation_repository_mock.simulations[0].simulation_id)

        assert cm_simulation_repository_mock.simulations[0].simulation_id == resp.simulation_id
        assert cm_simulation_repository_mock.simulations[0].xcg == resp.xcg

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_cm_simulation(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        cm_simulation_repository_mock = CmSimulationRepositoryMock()
        resp = cm_simulation_repository.delete_cm_simulation(cm_simulation_repository_mock.simulations[0].simulation_id)

        assert cm_simulation_repository_mock.simulations[0].simulation_id == resp.simulation_id
        assert cm_simulation_repository_mock.simulations[0].xcg == resp.xcg

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_cm_simulation(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        cm_simulation_repository_mock = CmSimulationRepositoryMock()
        resp = cm_simulation_repository.get_all_cm_simulations()

        assert len(cm_simulation_repository_mock.simulations) == len(resp)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_cm_simulation(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        cm_simulation_repository_mock = CmSimulationRepositoryMock()

        original_simulation = cm_simulation_repository_mock.simulations[0]
        updated_simulation = cm_simulation_repository_mock.simulations[0]
        updated_simulation.xcg = 0.8  
        
        resp = cm_simulation_repository.update_cm_simulation(
            simulation_id=original_simulation.simulation_id, 
            cm_simulation=updated_simulation
        )

        assert resp.simulation_id == original_simulation.simulation_id
        assert resp.xcg == 0.8

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_cm_simulation_counter(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        resp = cm_simulation_repository.get_cm_simulation_counter()

        assert isinstance(resp, int)
        assert resp >= 0

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_cm_simulation_counter(self):
        os.environ["STAGE"] = "TEST"

        cm_simulation_repository = CmSimulationRepositoryDynamo()
        initial_counter = cm_simulation_repository.get_cm_simulation_counter()
        resp = cm_simulation_repository.update_cm_simulation_counter()

        assert isinstance(resp, int)
        assert resp == initial_counter + 1