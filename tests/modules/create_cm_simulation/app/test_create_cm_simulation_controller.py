from src.modules.create_cm_simulation.app.create_cm_simulation_controller import CreateCmSimulationController
from src.modules.create_cm_simulation.app.create_cm_simulation_usecase import CreateCmSimulationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock
import uuid

class Test_CreateCmSimulationController:
    def test_create_cm_simulation_controller(self):
        repo = CmSimulationRepositoryMock()
        usecase = CreateCmSimulationUsecase(repo=repo)
        controller = CreateCmSimulationController(usecase=usecase)
        id_esperado = str(uuid.uuid4())
        request = HttpRequest(body={
            'simulation_id': id_esperado,
            'xcg':0.4,
            'xac_w':0.4,
            'sw':1.0,
            'st':1.0,
            'cw':1.0,
            'ct':1.0,
            'iw':1.0,
            'it':1.0,
            'lt':1.0,
            'cm_ac':0.35,
            'cl_0':0.45,
            'cl_alpha':5.0
            }
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['simulation']['simulation_id'] == repo.simulations[-1].simulation_id
        assert response.body['simulation']['xcg'] == repo.simulations[-1].xcg
        assert response.body['simulation']['xac_w'] == repo.simulations[-1].xac_w
        assert response.body['simulation']['sw'] == repo.simulations[-1].sw
        assert response.body['simulation']['st'] == repo.simulations[-1].st
        assert response.body['simulation']['cw'] == repo.simulations[-1].cw
        assert response.body['simulation']['ct'] == repo.simulations[-1].ct
        assert response.body['simulation']['iw'] == repo.simulations[-1].iw
        assert response.body['simulation']['it'] == repo.simulations[-1].it
        assert response.body['simulation']['lt'] == repo.simulations[-1].lt
        assert response.body['simulation']['cm_ac'] == repo.simulations[-1].cm_ac
        assert response.body['simulation']['cl_0'] == repo.simulations[-1].cl_0
        assert response.body['simulation']['cl_alpha'] == repo.simulations[-1].cl_alpha
        assert response.body['message'] == 'the CM simulation was created successfully'

    
    def test_create_cm_simulation_controller_invalid_simulation_id(self):
        repo = CmSimulationRepositoryMock()
        usecase = CreateCmSimulationUsecase(repo=repo)
        controller = CreateCmSimulationController(usecase=usecase)

        request = HttpRequest(body={
            'simulation_id': 43, 
            'xcg':0.4,
            'xac_w':0.4,
            'sw':1.0,
            'st':1.0,
            'cw':1.0,
            'ct':1.0,
            'iw':1.0,
            'it':1.0,
            'lt':1.0,
            'cm_ac':0.35,
            'cl_0':0.45,
            'cl_alpha':5.0
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field simulation_id is not valid'
        