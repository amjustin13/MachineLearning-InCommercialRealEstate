# MachineLearning-InCommercialRealEstate
## 1. Vision and Goals Of The Project:

Our main goal is to help the BLDUP create a machine learning platform to analyze housing and construction project data.

### Our Client: [BLDUP](https://www.bldup.com/)
- BLDUP is a Saas platform that provides valuable data for real estate investment and development.

### Project Description
- **Background**: some permit data sources lack permit classifications that BLDUP depends on to automate status updates site-wide
- **Goal**: to architecture, train, and deploy a machine learning model as a microservice integrated to the BLDUP platform that enables permit classification prediction to allow BLDUP to achieve a greater level of automation

### Project Motivation
- Enhance real estate data for BLDUP clients
- Reduce BLDUPs cost by automating data labeling

![image](https://user-images.githubusercontent.com/13989262/145156306-e9cf8fdb-7c66-4aaf-8127-e2456821a974.png)

### MVP
To implement and deploy a trained model that can accurately predict the classification of a permit based on its description, and deployed as an endpoint of an API that can be called repeatedly within the BLDUP infrastructure.

Goals:
- Identify BLDUPs data analysis main shortcomings
- Create and train best identified machine learning model
- Create web API to expose the model's functionality
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
- Identifying a machine learning classification and estimation use cases with BLDUPs currently acquired data.
- Training, testing and deploying identified machine learning models.
- Design and develop an API interface in order to extract data from the trained model.
- Develop a microservice framework that can be used to deploy and maintain the machine learning model.

** **

## 4. Solution Concept
High-level outline of the solution:
The main shortcoming of the current BLDUP service that we will be creating a solution for this semester . First, it does not classify different types of construction work well using the current data processing pipeline. Second, blank images are used as placeholders whenever the service isn’t able to find suitable images of the construction project. Machine learning can be used to mitigate these shortcomings. We plan to explore state of the art models (classification (regression, CNN, MLP)) to address the first project categorization problem. For the image generation goal, we plan to explore generative adversarial networks (GANs) to generate arbitrary images related to each individual type of real estate construction project.

![image](https://user-images.githubusercontent.com/13989262/134755362-64c80dae-68f2-41ce-995f-9d406209824e.png)

![image](https://user-images.githubusercontent.com/13989262/145156407-bb2b5bf5-f64b-4e45-9681-a1a1c016f34d.png)

** **
## 5. Acceptance criteria

Research and train a machine learning model to enhance the BLDUP data processing pipeline. This model will serve as microservices that will interact with the current BLDUP framework. The machine learning model will enhance the BLDUP data processing pipeline by classifying public construction permit data by different types of permit. Additionally, the model will be exposed through an API and integrated into the BLDUP platform.
In general, we are going to use machine learning to enhance the BLDUP web platform. Currently, some of properties’ information is manually inputted and we want to train the models to reduce the labor during adding or updating new properties’ information to the website.

** **

## 6.  Release Planning:
### Sprint #1 (20 Sep 2021 to 03 Oct 2021):
- Learn the demands and requirements from mentor
- Explore BLDUPs platform to familiarize ourselves with the scope and implications of the project
- Understand the data acquired by BLDUP
- Investigate and research classification algorithms
- Identify at least 2 ML algorithms to implement

### Sprint #2 (04 Oct 2021 to 17 Oct 2021):
- Initial model explotation and paper discussion: https://www.ashrae.org/file%20library/conferences/specialty%20conferences/2020%20building%20performance/papers/d-bsc20-c083.pdf
![image](https://user-images.githubusercontent.com/13989262/145156893-09bf39ce-0545-41af-b852-a589889d6aa9.png)
  - The paper tackles a similar problem we are trying to solve
  - Provides excellent methods to devise a solution to our project
  - Paper results serve as a baseline for our work
- Cleaning the Boston dataset
![image](https://user-images.githubusercontent.com/13989262/145157127-560b2e50-1089-433f-a7a4-0c3a84e57d17.png)
- Create a simple initial skeleton of an API interface
![py_gif](https://user-images.githubusercontent.com/13989262/145157614-805e8ea3-0017-4344-bfcb-c12e1454ad9c.gif)
- Initial analysis of the BERT machine learning model

- Demo2 Link: https://drive.google.com/file/d/1wfLV-DiJDwQIxkG1ziCiuqr1edmJ4VoB/view?usp=sharing

### Sprint #3 (18 Oct 2021 to 31 Oct 2021):
- Train the first BERT model on Boston data without permit IDs
![image](https://user-images.githubusercontent.com/13989262/145157282-dfdeddf6-bb98-443e-a2d5-0d4c89a81a95.png)
- Tune BERT model parameters
- Formalize API implementation and deploy

![api_gif](https://user-images.githubusercontent.com/13989262/145158252-919f0ef9-8965-4941-acc3-ede6d7c7daab.gif)

- Demo3 Link: https://www.youtube.com/watch?v=P2m0KtebSH0

### Sprint #4 (1 Nov 2021 to 14 Nov 2021):
- Make API route more robust
  - Endpoint error checking for invalid inputs
  - Docker containerize endpoint and resources
- Investigate implementation for DevOps/CI framework
  - Server vs. serverless
    - After consultation with our mentor, server deployment is best 
    - Serverless offers no real cost reduction in our case
    - Serverless latency is a huge detriment to the functionality of the model
![image](https://user-images.githubusercontent.com/13989262/145158648-c245e8d6-f50b-4572-93b4-7e6f868b30dd.png)

- Regroup output categories of the costruction permit types to 4 general types (Building, Mechanical, Plumbing, Electrical)
  - Permit labels must be the same across different cities when aggregating nationwide data for model training
  - Collected data from: Boston, Austin, and San Francisco
![image](https://user-images.githubusercontent.com/13989262/145158526-58e773e9-75be-4c08-828d-909f8549c089.png)


### Sprint #5 (15 Nov 2021 to 28 Nov 2021):
- Retrain model on heterogenous data to make a generalized model
![image](https://user-images.githubusercontent.com/13989262/145158936-4888bb93-2834-4f7f-a2c8-e300123c7c5a.png)
- Divide data into pre-construction and post-construction sets
![image](https://user-images.githubusercontent.com/13989262/145159028-e5ed7057-062d-41ea-89d5-3e8f4e31c306.png)
- Finalize deployment automation through bash script
![image](https://user-images.githubusercontent.com/13989262/145158985-46ca44fa-301a-4ae4-a7af-33af9147f906.png)


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

- From within the directory containing the Dockerfile run the following to build the docker image:

  - `docker build -t webapp-build:latest . `

- You should see the image listed when running:
  - `docker image ls`

- Finally, in order to run the app:
  - `docker run -d -p 5000:5000 webapp-build`

- Now, the app should be availble at (use Postman or a browset to verify):
  - `http://127.0.0.1:5000/`
