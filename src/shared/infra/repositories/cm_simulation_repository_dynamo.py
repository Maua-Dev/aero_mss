from typing import Optional
from src.shared.domain.entities.cm_simulation import CmSimulation
from src.shared.domain.repositories.cm_simulation_repository_interface import ICmSimulationRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.cm_simulation_dynamo_dto import CmSimulationDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource

class CmSimulationRepositoryDynamo(ICmSimulationRepository):
    @staticmethod
    def partition_key_format(simulation_id: str) -> str:
        return f"cm_simulation#{simulation_id}"

    @staticmethod
    def sort_key_format(simulation_id: str) -> str:
        return f"#{simulation_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_simulation_table_name,
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
    
    def update_cm_simulation(self, simulation_id: str, new_xcg: Optional[float] = None, new_xac_w: Optional[float] = None, new_sw: Optional[float] = None, new_st: Optional[float] = None, new_cw: Optional[float] = None, new_ct: Optional[float] = None, new_iw: Optional[float] = None, new_it: Optional[float] = None, new_lt: Optional[float] = None, new_Cm_ac: Optional[float] = None, new_Cl_0: Optional[float] = None, new_Cl_alpha: Optional[float] = None) -> CmSimulation:
        # Get current simulation
        current_simulation = self.get_cm_simulation(simulation_id)
        
        # Update fields if provided
        if new_xcg is not None:
            current_simulation.xcg = new_xcg
        if new_xac_w is not None:
            current_simulation.xac_w = new_xac_w
        if new_sw is not None:
            current_simulation.sw = new_sw
        if new_st is not None:
            current_simulation.st = new_st
        if new_cw is not None:
            current_simulation.cw = new_cw
        if new_ct is not None:
            current_simulation.ct = new_ct
        if new_iw is not None:
            current_simulation.iw = new_iw
        if new_it is not None:
            current_simulation.it = new_it
        if new_lt is not None:
            current_simulation.lt = new_lt
        if new_Cm_ac is not None:
            current_simulation.cm_ac = new_Cm_ac
        if new_Cl_0 is not None:
            current_simulation.cl_0 = new_Cl_0
        if new_Cl_alpha is not None:
            current_simulation.cl_alpha = new_Cl_alpha
        
        # Save updated simulation
        cm_simulation_dto = CmSimulationDynamoDTO.from_entity(cm_simulation=current_simulation)
        self.dynamo.put_item(partition_key=self.partition_key_format(simulation_id),
                             sort_key=self.sort_key_format(simulation_id=simulation_id), item=cm_simulation_dto.to_dynamo(),
                             is_decimal=True)
        return current_simulation
    
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
