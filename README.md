# MachineLearning-InCommercialRealEstate
## 1. Vision and Goals Of The Project:

Our goal is to help the BLDUP create a machine learning platform to analyze housing and construction project data. We will be adding several different machine learning models and deploying them as independent microservices exposed by a simple API interface.

Goals:
- Identify BLDUPs data analysis main shortcomings
- Create and train 2-4 machine learning models
- Create web API to expose the models functionality
- Deploy all models as microservices that can be used by BLDUP to improve their platform

** **

## 2. Users/Personas Of The Project:

The BLDUP is a B2B platform for users who want to trade properties directly to the business owner or look for recent information about certain properties or construction projects.

It does target:
- Individuals looking for new opportunities to trade/buy properties
- Companies looking for new opportunities to trade/buy properties
- Individuals who are employed by companies within the construction industry
- Individuals looking to understand housing and construction data

** **

## 3.   Scope and Features Of The Project:
This project will be scoped to the following:
- Identifying several machine learning classification and estimation use cases with BLDUPs currently acquired data.
- Training, testing and deploying at least 2-4 learning models.
- Design and develop an API interface in order to extract data from the trained models.
- Develop a microservice framework that can be used to deploy and maintain each of the machine learning models.

** **

## 4. Solution Concept
High-level outline of the solution:
There are two main shortcomings of the current BLDUP service. First, it does not classify different types of construction work well using the current data processing pipeline. Second, blank images are used as placeholders whenever the service isn’t able to find suitable images of the construction project. Machine learning can be used to mitigate these shortcomings. We plan to explore state of the art models (classification (regression, CNN, MLP)) to address the first project categorization problem. For the image generation goal, we plan to explore generative adversarial networks (GANs) to generate arbitrary images related to each individual type of real estate construction project.

![image](https://user-images.githubusercontent.com/13989262/134755362-64c80dae-68f2-41ce-995f-9d406209824e.png)
![image](https://user-images.githubusercontent.com/13989262/134755377-f13799d8-ee25-4ac5-9c58-3b55bb7cabb0.png)


** **
## 5. Acceptance criteria

Research, architecture, train, and develop at least 2 machine learning models to enhance the BLDUP data processing pipeline. These models will serve as microservices that will interact with the current BLDUP framework. The machine learning models will enhance the BLDUP data processing pipeline by classifying public real estate transactions by different types of work. Additionally, the models will generate arbitrary images to be used as placeholders in the case that construction images are absent in the public database.
In general, we are going to use machine learning to finalize the BLDUP web platform. Currently, some of properties’ information is manually inputted and we want to train the models to reduce the labor during adding or updating new properties’ information to the website.

** **

## 6.  Release Planning:
Sprint #1 (20 Sep 2021 to 03 Oct 2021):
- Explore BLDUPs platform
- Understand the data acquired by BLDUP
- Investigate and research classification algorithms
- Identify at least 2 ML algorithms to implement

Sprint #2 (04 Oct 2021 to 17 Oct 2021) - Subject to change:
- Define design of API used to communicate with ML learning models
- Create a simple initial skeleton of an API interface
- Initial analysis of a least one machine learning model

- Demo2 Link: https://drive.google.com/file/d/1wfLV-DiJDwQIxkG1ziCiuqr1edmJ4VoB/view?usp=sharing

Sprint #3 (18 Oct 2021 to 31 Oct 2021):
- Create DevOps/CI Framework in Github
- Tune BERT model parameters
- Formalize API implementation
- Formalize and deploy ML microservice

- Demo3 Link: https://www.youtube.com/watch?v=P2m0KtebSH0

Sprint #4 (1 Nov 2021 to 14 Nov 2021):
- Create DevOps/CI bash script
- Make API route more robust by handling user inputs
- Image generation task research
- Multi-city data collection
- Retrain model

- Demo4 Link: https://www.youtube.com/watch?v=jZrKYecOzNI&t=8s&ab_channel=KhoaTran

Sprint #5 (15 Nov 2021 to 28 Nov 2021):
- Demo5 Link: https://youtu.be/2IhgkDtn_vY

Sprint #6 (29 Nov 2021 to 14 Dec 2021):
Final Product

** **

## Mentor
Andrey Turovsky
andrey@bldup.com

Professor Orran Krieger:
okrieg@bu.edu

Professor Peter Desnoyers:
pjd-nu or pjd@ccs.neu.edu

Anqi Guo:
anqianqi1

# Running App in Docker Container
For manual setup
- From within the directory containing the Dockerfile run the following to build the docker image:

  - `docker build -t webapp-build:latest . `

- You should see the image listed when running:
  - `docker image ls`

- Finally, in order to run the app:
  - `docker run --name nameofcontainer -d webapp-build`

- Now, the app should be availble at (use Postman or a browset to verify):
  - `docker exec -it nameofcontainer /bin/bash`
- Once you are in the container:
  - `python api.py`

Automatically setup
- Run the get.sh script
  - `get.sh nameofcontainer`
