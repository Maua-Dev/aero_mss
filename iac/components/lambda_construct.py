import os
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaConstruct(Construct):
    functions_that_need_dynamo_user_table_permissions= []
    functions_that_need_dynamo_simulation_table_permissions= []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, mss_student_api_resource: Resource,
                                              environment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_13,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )

        mss_student_api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                                        integration=LambdaIntegration(
                                                                                            function))

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict) -> None:
        super().__init__(scope, "AeroMss_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "AeroMss_Lambda_Layer",
                                                 code=lambda_.Code.from_asset("./build"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_13]
                                                 )

        # self.create_user_function= self.create_lambda_api_gateway_integration(
        #     module_name="create_user",
        #     method="POST",
        #     mss_student_api_resource=api_gateway_resource,
        #     environment_variables=environment_variables
        # )

        # self.get_all_users_function= self.create_lambda_api_gateway_integration(
        #     module_name="get_all_users",
        #     method="GET",
        #     mss_student_api_resource=api_gateway_resource,
        #     environment_variables=environment_variables
        # )

        # self.update_user_function= self.create_lambda_api_gateway_integration(
        #     module_name="update_user",
        #     method="PUT",
        #     mss_student_api_resource=api_gateway_resource,
        #     environment_variables=environment_variables
        # )

        # self.delete_user_function= self.create_lambda_api_gateway_integration(
        #     module_name="delete_user",
        #     method="DELETE",
        #     mss_student_api_resource=api_gateway_resource,
        #     environment_variables=environment_variables
        # )

        self.create_cm_simulation_function= self.create_lambda_api_gateway_integration(
            module_name="create_cm_simulation",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.get_all_simulations_function= self.create_lambda_api_gateway_integration(
            module_name="get_all_simulations",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.delete_simulation_function= self.create_lambda_api_gateway_integration(
            module_name="delete_simulation",
            method="DELETE",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        # self.functions_that_need_dynamo_user_table_permissions = [
        #     self.create_user_function,
        #     self.get_all_users_function,
        #     self.delete_user_function,
        #     self.update_user_function
        # ]

        self.functions_that_need_dynamo_simulation_table_permissions=[
            self.create_cm_simulation_function,
            self.get_all_simulations_function,
            self.delete_simulation_function
        ]
