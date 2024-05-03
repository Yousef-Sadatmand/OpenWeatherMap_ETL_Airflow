from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

#--------------------------------------------------------------------------------


default_args = {
    "owner": "Your Name",
    "depends_on_past": False,
    "start_date": datetime(2024, 05, 03),
    "email": ["your.email@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "openweathermap",
    default_args=default_args,
    schedule_interval="* * * * *",
    catchup=False
)

#------------------------------------Python-Functions---------------------------------------

# Define the extract function to fetch data from the API
def extract():
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
    API_KEY = "your-api-key"
    CITY = "Vancouver"  # Replace "Vancouver" with the desired city name

    url = f"{BASE_URL}q={CITY}&appid={API_KEY}"

    response = requests.get(url).json()
    return response

from collections import Counter

# Define the transform function to process the extracted data
def transform(response):
    weather_data = {}

    for forecast in response['list']:
        date = forecast['dt_txt'].split(' ')[0]
        temperature = round(forecast['main']['temp'] - 273.15, 2)  # Convert Kelvin to Celsius
        weather = forecast['weather'][0]['description']

        if date not in weather_data:
            weather_data[date] = {'temperature': temperature, 'weather': [weather]}
        else:
            # If the date already exists in the dictionary, append the weather description to the list
            weather_data[date]['weather'].append(weather)

    transformed_data = []
    for date, data in weather_data.items():
        # Count occurrences of each weather description for the current date
        weather_counter = Counter(data['weather'])
        # Select the most frequent weather description
        most_common_weather = weather_counter.most_common(1)[0][0]
        transformed_data.append(
            f"On {date}, the weather will be {most_common_weather} with a temperature of {data['temperature']}°C."
        )
    return transformed_data

# Define the load function to save the transformed data to a file
def load_data(transformed_data):
    with open('weather_forecast.txt', 'w') as file:
        file.write(f"Here is the weather forecast for Vancouver for the next five days:\n")
        for item in transformed_data:
            file.write(item + '\n')
#------------------------------------Operators---------------------------------------

# Define the tasks in the DAG
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    op_args=[extract_task.output],
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    op_args=[transform_task.output],
    dag=dag,
)


#----------------------- DAG Structure -------------------------------

# Define the task dependencies
extract_task >> transform_task >> load_task
