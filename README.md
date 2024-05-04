# Weather Forecast ETL with Apache Airflow

This project demonstrates an Extract, Transform, and Load (ETL) pipeline using Apache Airflow to fetch weather forecast data from the OpenWeatherMap API, transform it, and store it in a text file.

## Description
The ETL process consists of the following steps:

1- **Extract**: Weather forecast data is extracted from the OpenWeatherMap API using the requests library in Python.

2- **Transform**: The extracted data is transformed to aggregate weather information for each day and convert temperatures from Kelvin to Celsius.

3- **Load**: The transformed data is loaded into a text file, providing a summary of the weather forecast for the next five days for a specified city.


## Prerequisites
- Apache Airflow installed
- Python 3.x
- Requests library
  
## Instructions
## Getting Started

1- Clone this repository to your local machine.

2- Install Apache Airflow and its dependencies.

3- Sign up for an account on OpenWeatherMap and obtain an API key.

## Configuring the DAG
1- Replace "Vancouver" with the desired city name in the weather_forecast_dag.py file.

2- Update the API_KEY variable with your OpenWeatherMap API key.
## Running the DAG
1- Start the Apache Airflow scheduler and web server.

2- Access the Airflow web interface and enable the DAG named weather_forecast_dag.

3- Trigger the DAG manually or wait for it to run according to the specified schedule.

4- Check the logs and task instances for any errors or issues.

## Viewing Results
1- Once the DAG has run successfully, check the generated weather_forecast.txt file in the specified output directory.

2- Open the text file to view the weather forecast summary for the next five days.

## Repository Structure
- dags/openweathermap.py: Defines the Airflow DAG.
- README.md: Documentation and setup instructions.
- weather_forecast.txt: Output file for the weather forecast data.

## Example DAG Visualization
At the end, your DAG (Directed Acyclic Graph) graph in Apache Airflow should look similar to the following screenshot:

![DAG Screenshot](https://i.imgur.com/C3CCoDB.jpeg)


## Note
Make sure to adhere to the usage policy and terms of service of the OpenWeatherMap API when using their services.

Feel free to reach out if you have any questions or need further assistance!



