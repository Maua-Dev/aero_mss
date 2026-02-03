import os
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk.aws_apigateway import RestApi, Cors

from components.lambda_construct import LambdaConstruct
from components.dynamo_construct import DynamoConstruct


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        stage = kwargs['tags']['stage']

        self.rest_api = RestApi(self, "AeroMss_RestApi",
                                    rest_api_name="AeroMss_RestApi",
                                    description="This is the AeroMss RestApi",
                                    default_cors_preflight_options=
                                    {
                                        "allow_origins": Cors.ALL_ORIGINS,
                                        "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                        "allow_headers": ["*"]
                                    },
                                    deploy_options={
                                        "stage_name": stage.lower()
                                    }
                                )

        api_gateway_resource = self.rest_api.root.add_resource("mss-aero", default_cors_preflight_options=
        {
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
                                                               )

        self.dynamo_table = DynamoConstruct(self, "AeroMss_DynamoDB")

        ENVIRONMENT_VARIABLES = {
            "STAGE": stage,
            # "DYNAMO_USER_TABLE_NAME": self.dynamo_table.user_table.table_name , # user table will not be used for now
            "DYNAMO_SIMULATION_TABLE_NAME": self.dynamo_table.simulation_table.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "REGION": self.region,
        }



        self.lambda_stack = LambdaConstruct(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES)
        
        # grant read and write for user table
        # for function in self.lambda_stack.functions_that_need_dynamo_user_table_permissions:
        #     self.dynamo_table.user_table.grant_read_write_data(function)


        # grant read and write for simulation table
        for function in self.lambda_stack.functions_that_need_dynamo_simulation_table_permissions:
            self.dynamo_table.simulation_table.grant_read_write_data(function)

        

        