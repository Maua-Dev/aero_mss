import os
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaConstruct(Construct):
    functions_that_need_dynamo_permissions = []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, mss_student_api_resource: Resource,
                                              environment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_11,
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
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_11]
                                                 )

        self.update_user_function = self.create_lambda_api_gateway_integration(
            module_name="update_user",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.functions_that_need_dynamo_permissions = [
            self.update_user_function
        ]
