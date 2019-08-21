from aws_cdk import (
    aws_iam as iam,
    aws_sns as sns,
    core,
)


class SnsResourcesContruct(core.Construct):
    """
    For every environment create a Sns Topic, an Iam user (with access_key
    and secret_key) and grant publish to the user on the topic.
    """

    @property
    def topics(self):
        """
        Creates and returns a property object.
        """
        return tuple(self._topics)

    @property
    def users(self):
        """
        Creates and returns a property object.
        """
        return tuple(self._users)

    def create_topic(self, id):
        """
        A new SNS topic.
        """
        topic = sns.Topic(self, id, topic_name=id)
        return topic

    def create_user(self, id):
        """
        A new IAM User.
        """
        user = iam.User(self, id, user_name=id)
        return user

    def grant_publish(self, topic, principal: iam.IPrincipal):
        """
        Grant topic publishing permissions to the given identity.
        """
        grant = topic.grant_publish(principal)
        return grant

    def create_key(self, id, user: iam.User):
        """
        A CloudFormation AWS::IAM::AccessKey.
        """
        key = iam.CfnAccessKey(self, id, user_name=user.user_name)
        return key

    def __init__(self, scope: core.Construct, id: str, environments: int) -> None:
        super().__init__(scope, id)
        self._topics = []
        self._users = []
        for env in environments:
            topics = self.create_topic(f"sns-events-{env}")
            users = self.create_user(f"sns-publisher-{env}")
            access_key = self.create_key(f"UserAccessKey-{env}", users)

            self.grant_publish(topics, users)

            core.CfnOutput(
                self,
                f"UserAccessKeyOutput-{env}",
                value=access_key.ref)

            core.CfnOutput(
                self,
                f"UserSecreyKeyOutput-{env}",
                value=access_key.attr_secret_access_key)
