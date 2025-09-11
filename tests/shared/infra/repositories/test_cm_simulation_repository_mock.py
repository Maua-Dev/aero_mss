from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import pytest


class Test_CmSimulationRepositoryMock:
    def test_get_simulation(self):
        repo = CmSimulationRepositoryMock()
        simulation = repo.get_simulation(1)

        assert simulation.simulation_id == 1
        assert simulation.xcg == 0.5
        assert simulation.xac_w == 0.5
        assert simulation.sw == 1
        assert simulation.st == 1
        assert simulation.cw == 1
        assert simulation.ct == 1
        assert simulation.iw == 1
        assert simulation.it == 1
        assert simulation.lt == 1
        assert simulation.Cm_ac == 0.3
        assert simulation.Cl_0 == 0.5
        assert simulation.Cl_alpha == 5

    def test_get_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        with pytest.raises(NoItemsFound):
            simulation = repo.get_simulation(69)

    def test_get_all_simulations(self):
        repo = CmSimulationRepositoryMock()
        simulations = repo.get_all_simulations()
        assert len(simulations) == 3

    def test_create_simulation(self):
        repo = CmSimulationRepositoryMock()
        simulation = CmSimulation(
            simulation_id=4,
            xcg=0.48,
            xac_w=0.42,
            sw=1,
            st=1,
            cw=1,
            ct=1,
            iw=1,
            it=1,
            lt=1,
            Cm_ac=0.31,
            Cl_0=0.43,
            Cl_alpha=5
        )

        repo.create_simulation(simulation)

        assert repo.simulations[3].simulation_id == 4
        assert repo.simulations[3].xcg == 0.48
        assert repo.simulations[3].xac_w == 0.42
        assert repo.simulations[3].sw == 1
        assert repo.simulations[3].st == 1
        assert repo.simulations[3].cw == 1
        assert repo.simulations[3].ct == 1
        assert repo.simulations[3].iw == 1
        assert repo.simulations[3].it == 1
        assert repo.simulations[3].lt == 1
        assert repo.simulations[3].Cm_ac == 0.31
        assert repo.simulations[3].Cl_0 == 0.43
        assert repo.simulations[3].Cl_alpha == 5

        assert repo.simulation_counter == 4

    def test_delete_simulation(self):
        repo = CmSimulationRepositoryMock()
        simulation = repo.delete_simulation(1)
        assert simulation.simulation_id == 1
        assert simulation.xcg == 0.5
        assert simulation.xac_w == 0.5
        assert simulation.sw == 1
        assert simulation.st == 1
        assert simulation.cw == 1
        assert simulation.ct == 1
        assert simulation.iw == 1
        assert simulation.it == 1
        assert simulation.lt == 1
        assert simulation.Cm_ac == 0.3
        assert simulation.Cl_0 == 0.5
        assert simulation.Cl_alpha == 5

    def test_delete_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        with pytest.raises(NoItemsFound):
            simulation = repo.delete_simulation(69)

    def test_update_simulation(self):
        repo = CmSimulationRepositoryMock()
        simulation = repo.update_simulation(1, 0.6, 0.6, 1, 1, 1, 1, 1, 1, 1, 1, 0.4, 0.6, 6)

        assert simulation.xcg == 0.6
        assert simulation.xac_w == 0.6
        assert simulation.sw == 1
        assert simulation.st == 1
        assert simulation.cw == 1
        assert simulation.ct == 1
        assert simulation.iw == 1
        assert simulation.it == 1
        assert simulation.lt == 1
        assert simulation.Cm_ac == 0.4
        assert simulation.Cl_0 == 0.6
        assert simulation.Cl_alpha == 6

    def test_update_simulation_not_found(self):
        repo = CmSimulationRepositoryMock()
        with pytest.raises(NoItemsFound):
            simulation = repo.update_simulation(69, 0.6, 0.6, 1, 1, 1, 1, 1, 1, 1, 1, 0.4, 0.6, 6)

    def test_get_simulations_counter(self):
        repo = CmSimulationRepositoryMock()

        assert repo.get_simulation_counter() == 3

