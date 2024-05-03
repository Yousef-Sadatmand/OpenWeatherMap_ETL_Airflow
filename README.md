# Weather Forecast ETL with Apache Airflow

An Apache Airflow project for extracting weather forecast data from the OpenWeatherMap API, transforming it, and loading it into a text file. Includes instructions on obtaining an API key from OpenWeatherMap


## Overview
This project demonstrates an Extract, Transform, and Load (ETL) pipeline using Apache Airflow to fetch weather forecast data from the OpenWeatherMap API, transform it, and store it in a text file.

## Prerequisites
- Apache Airflow installed
- Python 3.x
- Requests library
## Setup
- Clone this repository.
- Create an account on OpenWeatherMap.
- Navigate to the "My API Keys" section to obtain your unique API key.
- Replace "YOUR_API_KEY" in the openweathermap.py file with your API key.
- Replace "Vancouver" with the desired city name in the openweathermap.py file.
- Ensure the requests library is installed. If not, install it using pip install requests.
## Usage
- Start the Airflow webserver: http://localhost:8080/
- Access the Airflow UI and enable the openweathermap DAG.
- Trigger the DAG to execute manually or set it to run on a schedule.
## Repository Structure
- dags/openweathermap.py: Defines the Airflow DAG.
- README.md: Documentation and setup instructions.
- weather_forecast.txt: Output file for the weather forecast data.
