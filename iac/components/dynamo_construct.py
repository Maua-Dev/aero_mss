from decimal import Decimal
from aws_cdk import (
    aws_dynamodb as dynamodb, RemovalPolicy,
)
from constructs import Construct
import os


class DynamoConstruct(Construct):
    
    user_table: dynamodb.Table
    simulation_table: dynamodb.Table


    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.stack_name = os.environ.get("STACK_NAME")
        stage = ''
        
        if 'prod' in self.github_ref_name.lower():
            stage = 'PROD'            
        elif 'homolog' in self.github_ref_name.lower():
            stage = 'HOMOLOG'
        else:
            stage = 'DEV'
            
        removal_policy = RemovalPolicy.RETAIN if stage=="PROD" else RemovalPolicy.DESTROY

        # self.user_table = dynamodb.Table(
        #     self, "AeroMss_DynamoDB_User_Table",
        #     partition_key=dynamodb.Attribute(
        #         name="PK",
        #         type=dynamodb.AttributeType.STRING
        #     ),
        #     sort_key=dynamodb.Attribute(
        #         name="SK",
        #         type=dynamodb.AttributeType.STRING
        #     ), 
        #     billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        #     removal_policy=removal_policy,

        #     table_name=f"AeroMss_DynamoDB_User_Table-{stage.upper()}",
        #     point_in_time_recovery=True if stage=="PROD" else False
        # )

        self.simulation_table= dynamodb.Table(
            self,
            "AeroMss_DynamoDB_Simulation_Table",
            partition_key=dynamodb.Attribute(
                name="PK",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="SK",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=removal_policy,

            table_name=f"AeroMss_DynamoDB_Simulation_Table-{stage.upper()}",
            point_in_time_recovery=True if stage=="PROD" else False
        )
        
    