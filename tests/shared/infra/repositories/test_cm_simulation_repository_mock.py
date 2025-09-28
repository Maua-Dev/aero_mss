from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.helpers.errors.usecase_errors import NoItemsFound, DuplicatedItem
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import pytest
import uuid


class Test_CmSimulationRepositoryMock:
    def test_get_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        first_simulation_id = repo.simulations[0].simulation_id
        simulation = repo.get_cm_simulation(first_simulation_id)

        assert simulation.simulation_id == first_simulation_id
        assert simulation.xcg == 0.5
        assert simulation.xac_w == 0.5
        assert simulation.sw == 1.0
        assert simulation.st == 1.0
        assert simulation.cw == 1.0
        assert simulation.ct == 1.0
        assert simulation.iw == 1.0
        assert simulation.it == 1.0
        assert simulation.lt == 1.0
        assert simulation.cm_ac == 0.3
        assert simulation.cl_0 == 0.5
        assert simulation.cl_alpha == 5.0

    def test_get_cm_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        non_existent_id = str(uuid.uuid4())
        with pytest.raises(NoItemsFound):
            simulation = repo.get_cm_simulation(non_existent_id)

    def test_get_all_cm_simulations(self):
        repo = CmSimulationRepositoryMock()
        simulations = repo.get_all_cm_simulations()
        assert len(simulations) == 3

    def test_create_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        simulation = CmSimulation(
            simulation_id=str(uuid.uuid4()),
            xcg=0.48,
            xac_w=0.42,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.31,
            cl_0=0.43,
            cl_alpha=5.0
        )

        repo.create_cm_simulation(simulation)

        assert repo.simulations[3].simulation_id == simulation.simulation_id
        assert repo.simulations[3].xcg == 0.48
        assert repo.simulations[3].xac_w == 0.42
        assert repo.simulations[3].sw == 1.0
        assert repo.simulations[3].st == 1.0
        assert repo.simulations[3].cw == 1.0
        assert repo.simulations[3].ct == 1.0
        assert repo.simulations[3].iw == 1.0
        assert repo.simulations[3].it == 1.0
        assert repo.simulations[3].lt == 1.0
        assert repo.simulations[3].cm_ac == 0.31
        assert repo.simulations[3].cl_0 == 0.43
        assert repo.simulations[3].cl_alpha == 5.0

        assert repo.simulation_counter == 4

    def test_delete_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        first_simulation_id = repo.simulations[0].simulation_id
        simulation = repo.delete_cm_simulation(first_simulation_id)
        assert simulation.simulation_id == first_simulation_id
        assert simulation.xcg == 0.5
        assert simulation.xac_w == 0.5
        assert simulation.sw == 1.0
        assert simulation.st == 1.0
        assert simulation.cw == 1.0
        assert simulation.ct == 1.0
        assert simulation.iw == 1.0
        assert simulation.it == 1.0
        assert simulation.lt == 1.0
        assert simulation.cm_ac == 0.3
        assert simulation.cl_0 == 0.5
        assert simulation.cl_alpha == 5.0

    def test_delete_cm_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        non_existent_id = str(uuid.uuid4())
        with pytest.raises(NoItemsFound):
            simulation = repo.delete_cm_simulation(non_existent_id)

    def test_update_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        first_simulation_id = repo.simulations[0].simulation_id
        simulation = repo.update_cm_simulation(first_simulation_id, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 0.6, 6.0)

        assert simulation.xcg == 0.6
        assert simulation.xac_w == 0.6
        assert simulation.sw == 1.0
        assert simulation.st == 1.0
        assert simulation.cw == 1.0
        assert simulation.ct == 1.0
        assert simulation.iw == 1.0
        assert simulation.it == 1.0
        assert simulation.lt == 1.0
        assert simulation.cm_ac == 0.4
        assert simulation.cl_0 == 0.6
        assert simulation.cl_alpha == 6.0

    def test_update_cm_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        non_existent_id = str(uuid.uuid4())
        with pytest.raises(NoItemsFound):
            simulation = repo.update_cm_simulation(non_existent_id, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 0.6, 6.0)

    def test_get_cm_simulations_counter(self):
        repo = CmSimulationRepositoryMock()

        assert repo.get_cm_simulation_counter() == 3

    def test_create_duplicated_cm_simulation(self):
        repo = CmSimulationRepositoryMock()
        existing_simulation_id = repo.simulations[0].simulation_id
        simulation = CmSimulation(
            simulation_id=existing_simulation_id,  
            xcg=0.48,
            xac_w=0.42,
            sw=1.0,
            st=1.0,
            cw=1.0,
            ct=1.0,
            iw=1.0,
            it=1.0,
            lt=1.0,
            cm_ac=0.31,
            cl_0=0.43,
            cl_alpha=5.0
        )

        with pytest.raises(DuplicatedItem):
            repo.create_cm_simulation(simulation)