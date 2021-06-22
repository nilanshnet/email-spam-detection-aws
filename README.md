# Spam Detector

## About:
A spam detection system built on AWS cloud, that upon receipt of an email message, automatically flags it as spam or not. This is based on the prediction obtained from the machine learning model created using Amazon SageMaker. The definition and provision of the resources on AWS cloud is done through the AWS Cloudformation template. This template can also be used with AWS code pipeline to automate the resource stack formation.

## Working: 

1.  Send an email to the email address that is used by the spam detector.

![send](https://user-images.githubusercontent.com/26367904/122842287-ad989300-d31a-11eb-8ed1-22f2fdf48714.png)

2.  Reply that we get, if the email is a spam:

![spam](https://user-images.githubusercontent.com/26367904/122842469-154ede00-d31b-11eb-97ff-4e90f57d2995.png)

3.  Reply that we get, if the email is NOT a spam:

![notSpam](https://user-images.githubusercontent.com/26367904/122842516-2ef02580-d31b-11eb-963e-dec31962f2ae.png)

## Procedure:



### Prerequisites:
- AWS cloud subscription
- A custom domain 
- An email address for that domain (user1@example.com)



## References

- [Amazon SageMaker](https://aws.amazon.com/sagemaker)
- [Machine Learning model using Amazon SageMaker](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/)
- [Build and Train a spam filter Machine Learning Model](https://github.com/aws-samples/reinvent2018-srv404-lambda-sagemaker/blob/master/training/README.md)

