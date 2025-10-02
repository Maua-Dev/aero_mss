from src.shared.infra.dto.cm_simulation_dynamo_dto import CmSimulationDynamoDTO
from src.shared.infra.repositories.cm_simulation_repository_mock import CmSimulationRepositoryMock

class Test_CMSimulationDynamoDto:
    def test_from_entity(self):
        repo = CmSimulationRepositoryMock()

        cm_simulation_dto = CmSimulationDynamoDTO.from_entity(cm_simulation=repo.simulations[0])

        expected_cm_simulation_dto = CmSimulationDynamoDTO(
            simulation_id=repo.simulations[0].simulation_id,
            xcg=repo.simulations[0].xcg,
            xac_w=repo.simulations[0].xac_w,
            sw=repo.simulations[0].sw,
            st=repo.simulations[0].st,
            cw=repo.simulations[0].cw,
            ct=repo.simulations[0].ct,
            iw=repo.simulations[0].iw,
            it=repo.simulations[0].it,
            lt=repo.simulations[0].lt,
            cm_ac=repo.simulations[0].cm_ac,
            cl_0=repo.simulations[0].cl_0,
            cl_alpha=repo.simulations[0].cl_alpha
        )

        assert cm_simulation_dto == expected_cm_simulation_dto

    def test_to_dynamo(self):
        repo = CmSimulationRepositoryMock()

        cm_simulation_dto = CmSimulationDynamoDTO(
            simulation_id=repo.simulations[0].simulation_id,
            xcg=repo.simulations[0].xcg,
            xac_w=repo.simulations[0].xac_w,
            sw=repo.simulations[0].sw,
            st=repo.simulations[0].st,
            cw=repo.simulations[0].cw,
            ct=repo.simulations[0].ct,
            iw=repo.simulations[0].iw,
            it=repo.simulations[0].it,
            lt=repo.simulations[0].lt,
            cm_ac=repo.simulations[0].cm_ac,
            cl_0=repo.simulations[0].cl_0,
            cl_alpha=repo.simulations[0].cl_alpha
        )

        cm_simulation_dynamo = cm_simulation_dto.to_dynamo()

        expected_dict = {
            "entity": "cm_simulation",
            "simulation_id": repo.simulations[0].simulation_id,
            "xcg": repo.simulations[0].xcg,
            "xac_w": repo.simulations[0].xac_w,
            "sw": repo.simulations[0].sw,
            "st": repo.simulations[0].st,
            "cw": repo.simulations[0].cw,
            "ct": repo.simulations[0].ct,
            "iw": repo.simulations[0].iw,
            "it": repo.simulations[0].it,
            "lt": repo.simulations[0].lt,
            "cm_ac": repo.simulations[0].cm_ac,
            "cl_0": repo.simulations[0].cl_0,
            "cl_alpha": repo.simulations[0].cl_alpha
        }

        assert cm_simulation_dto.to_dynamo() == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'simulation_id': 'sim_1',
                                'xcg': 0.25,
                                'xac_w': 0.2,
                                'sw': 1.0,
                                'st': 0.33,
                                'cw': 0.5,
                                'ct': 0.33,
                                'iw': 0.03490658503988659,
                                'it': -0.05235987755982989,
                                'lt': 0.75,
                                'cm_ac': -0.27,
                                'cl_0': 0.743,
                                'cl_alpha': 3.558,
                                'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}}

        cm_simulation_dto = CmSimulationDynamoDTO.from_dynamo(cm_simulation_data=dynamo_dict["Item"])

        expected_cm_simulation_dto = CmSimulationDynamoDTO(
            simulation_id="sim_1",
            xcg=0.25,
            xac_w=0.2,
            sw=1.0,
            st=0.33,
            cw=0.5,
            ct=0.33,
            iw=0.03490658503988659,
            it=-0.05235987755982989,
            lt=0.75,
            cm_ac=-0.27,
            cl_0=0.743,
            cl_alpha=3.558
        )

        assert cm_simulation_dto == expected_cm_simulation_dto

    def test_to_entity(self):
        repo = CmSimulationRepositoryMock()

        cm_simulation_dto = CmSimulationDynamoDTO(
            simulation_id=repo.simulations[0].simulation_id,
            xcg=repo.simulations[0].xcg,
            xac_w=repo.simulations[0].xac_w,
            sw=repo.simulations[0].sw,
            st=repo.simulations[0].st,
            cw=repo.simulations[0].cw,
            ct=repo.simulations[0].ct,
            iw=repo.simulations[0].iw,
            it=repo.simulations[0].it,
            lt=repo.simulations[0].lt,
            cm_ac=repo.simulations[0].cm_ac,
            cl_0=repo.simulations[0].cl_0,
            cl_alpha=repo.simulations[0].cl_alpha
        )
        
        cm_simulation = cm_simulation_dto.to_entity()

        assert cm_simulation.simulation_id == repo.simulations[0].simulation_id
        assert cm_simulation.xcg == repo.simulations[0].xcg
        assert cm_simulation.xac_w == repo.simulations[0].xac_w
        assert cm_simulation.sw == repo.simulations[0].sw
        assert cm_simulation.st == repo.simulations[0].st
        assert cm_simulation.cw == repo.simulations[0].cw
        assert cm_simulation.ct == repo.simulations[0].ct
        assert cm_simulation.iw == repo.simulations[0].iw
        assert cm_simulation.it == repo.simulations[0].it
        assert cm_simulation.lt == repo.simulations[0].lt
        assert cm_simulation.cm_ac == repo.simulations[0].cm_ac
        assert cm_simulation.cl_0 == repo.simulations[0].cl_0
        assert cm_simulation.cl_alpha == repo.simulations[0].cl_alpha

        