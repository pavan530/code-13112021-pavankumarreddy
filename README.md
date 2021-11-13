#####################BMI Calculator########################
1. Added 3 extra columns along with existing data as per requirements mentioned in the tasks. 

How to Run in stand-alone machine:
---------------------------------
1.  python3 bmicalculator.py

Output looks like below:
-----------------------
   Gender  HeightCm  WeightKg        BMI BMI Range(kg/m2)     Health risk         BMI Category
0    Male       171        96  56.140351     40 and above  Very high risk  Very severely obese
1  Female       166        62  37.349398        35 - 39.9       High risk       Severely obese


####################### UNIT-TEST ####################
1. Write all unittests inside Testing class and run the following command :

python3 -m unittest Basic_Test.Testing

Which gives the report of failed tests and Ok tests and errors.

I have just put placeholders to write test cases but didn't test the code in BMI calculator dude to lack of time. Given in the job, I should be able to pick up and write test cases without a doubt.

########################## Infrastructure Deployment ####################################

1. Created Dockerfile for making the application to scale by deploying it in Kubernetes or AWS ECS by containerizing the application. Created sample Jenkinsfile also to push the container to AWS ECR.
2. Login to docker hub with credentails and build docker image : docker build -t test/image-name:latest
3. Docker image push to AWS ECR/public docker hub : docker push test/image-name:latest

