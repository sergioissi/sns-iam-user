# SNS-IAM-User

Created with Aws CDK in Python, the code will deploy resources for every environment. The resources deployed are:

* Sns Topic
* Iam User
* Iam Policy
* Iam Access key
* Iam Secret key

The policy grants Sns:Publish to the Iam User. You can find the Access Key and Secret Key of every user in the outputs of the
Cloudformation stack.

## Setup

### Installing the CDK CLI

```sh
$ npm install -g aws-cdk
$ cdk --version
```

### Create your python virtual env

If you don't already have, install virtualenv to isolate the Python environment for this project,
this can help when you have several packages with potential conflicting dependencies or you are
working on a shared computer.

```sh
$ pip install virtualenv
```

then you can set up your virtual environment:

```sh
$ virtualenv venv
$ source venv/bin/activate
$ install -r requirements
```

### Bootstrapping your AWS Environment
Before you can use the AWS CDK you must bootstrap your AWS environment to create the infrastructure that the AWS CDK CLI needs to deploy your AWS CDK app. Currently the bootstrap command creates only an Amazon S3 bucket.

```sh
$ cdk bootstrap
```

You incur any charges for what the AWS CDK stores in the bucket. Because the AWS CDK does not remove any objects from the bucket, the bucket can accumulate objects as you use the AWS CDK. You can get rid of the bucket by deleting the CDKToolkit stack from your account.

## Commands to manage and create/update infrastructure:

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
