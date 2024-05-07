# Garden Buddy

Garden Buddy is an innovative self-cultivating garden system designed to streamline and automate the challenges typically encountered in traditional plant cultivation. Serving as both an indoor, portable greenhouse and a gardening solution, the Smart Garden enables users to easily establish their own garden, regardless of their living environment. 

## garden-buddy-backend

This repository hosts the code for the API server, which manages requests from both Garden Buddies and the mobile app. The server offers two primary functions: serving as a data access layer for the integrated database and facilitating the training and utilization of machine learning models.

## Setup Instructions

1. You will need this repository, [garden-mobile-rasp-hub](https://github.com/ireneliee/garden-mobile-rasp-hub), and [garden-buddy-mobile](https://github.com/ireneliee/garden-buddy-mobile) installed locally into your computer
2. Create a MySQL database named `garden_buddy_database`
3. Create a new virtual environment for this repository and install all the required packages using 
```
pip install -r requirements.txt
```
4. To run the server, use 
```
python -m flask --app root run --host=0.0.0.0
```
5. To complete the set up of Garden Buddy system, you may visit [garden-mobile-rasp-hub](https://github.com/ireneliee/garden-mobile-rasp-hub) and [garden-buddy-mobile](https://github.com/ireneliee/garden-buddy-mobile)
