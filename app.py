from aws_cdk import core
from infrastructure.snsresources import SnsResourcesContruct


class SnSStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        SnsResourcesContruct(self, "SnsConstruct", environments=["dev", "staging", "production"])

app = core.App()
SnSStack(app, "sns-resources", env={'region': 'eu-west-1'})
app.synth()
