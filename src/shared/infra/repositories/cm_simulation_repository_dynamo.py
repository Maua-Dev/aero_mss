from src.shared.domain.entities.cm_simulation import CMSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICMSimulationRepository
from src.shared.environments import Environments
from src.shared.infra.dto.cm_simulation_dynamo_dto import CMSimulationDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource

class CMSimulationRepositoryDynamo(ICMSimulationRepository):
    pass