from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.cm_simulation_dynamo_dto import CmSimulationDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource

class CMSimulationRepositoryDynamo(ICmSimulationRepository):
    @staticmethod
    def partition_key_format(simulation_id: str) -> str:
        return f"cm_simulation#{simulation_id}"

    @staticmethod
    def sort_key_format(simulation_id: str) -> str:
        return f"#{simulation_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_cm_simulation(self, simulation_id: str) -> CmSimulation:
        resp = self.dynamo.get_item(partition_key=self.partition_key_format(simulation_id), sort_key=self.sort_key_format(simulation_id))

        if resp.get('Item') is None:
            raise NoItemsFound("simulation_id")

        cm_simulation_dto = CmSimulationDynamoDTO.from_dynamo(resp["Item"])
        return cm_simulation_dto.to_entity()
    
    def get_all_cm_simulations(self) -> list[CmSimulation]:
        resp = self.dynamo.get_all_items()
        cm_simulations = []
        for item in resp['Items']:
            if item.get("entity") == 'cm_simulation':
                cm_simulations.append(CmSimulationDynamoDTO.from_dynamo(item).to_entity())

        return cm_simulations

    def create_cm_simulation(self, new_cm_simulation: CmSimulation) -> CmSimulation:
        cm_simulation_dto = CmSimulationDynamoDTO.from_entity(cm_simulation=new_cm_simulation)
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_cm_simulation.simulation_id),
                                    sort_key=self.sort_key_format(simulation_id=new_cm_simulation.simulation_id), item=cm_simulation_dto.to_dynamo(),
                                    is_decimal=True)
        return new_cm_simulation
    
    def delete_cm_simulation(self, simulation_id: str) -> CmSimulation:
        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(simulation_id), sort_key=self.sort_key_format(simulation_id))

        if "Attributes" not in resp:
            raise NoItemsFound("simulation_id")

        cm_simulation_dto = CmSimulationDynamoDTO.from_dynamo(resp["Attributes"])
        return cm_simulation_dto.to_entity()
    
    def update_cm_simulation(self, simulation_id: str, cm_simulation: CmSimulation) -> CmSimulation:
        cm_simulation_dto = CmSimulationDynamoDTO.from_entity(cm_simulation=cm_simulation)
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(simulation_id),
                                    sort_key=self.sort_key_format(simulation_id=simulation_id), item=cm_simulation_dto.to_dynamo(),
                                    is_decimal=True)
        return cm_simulation_dto.to_entity()
    
    def get_cm_simulation_counter(self) -> int:
        resp = self.dynamo.get_item(partition_key="counters", sort_key="#cm_simulation")

        if resp.get('Item') is None:
            return 0

        return int(resp['Item']['counter'])

    def update_cm_simulation_counter(self) -> int:
        current_counter = self.get_cm_simulation_counter()
        new_counter = current_counter + 1

        self.dynamo.put_item(partition_key="counters", sort_key="#cm_simulation", item={
            "entity": "counter",
            "counter": new_counter
        }, is_decimal=True)

        return new_counter
