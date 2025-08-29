# APIs in Data Pipelines & ETL

APIs are often the source (Extract) in data pipelines, or sometimes the destination (Load). They can even provide transformation logic via external services.

* Extract	Pull data from public or private APIs (e.g. weather, CRM, finance, ERP)
* Transform	Validate/clean/filter API data
* Load	Push data to APIs (e.g. upload results to Google Sheets, update CRM)

## Architecture Overview

```
+--------------------+
|   External API     |  <-- (GET, POST, etc.)
+--------------------+
         |
         ▼
+--------------------+
|    Extract Logic    |  ← requests, Airflow operator, etc.
+--------------------+
         |
         ▼
+--------------------+
|  Transform (Clean,  |
|  Normalize, Enrich) |
+--------------------+
         |
         ▼
+--------------------+
|    Load Target      |  ← Database, Data Lake, or API
+--------------------+
```

## Python Examples
Extract data from an API:
```
import requests

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_KEY"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
```

Transform and clean it:
```
def transform(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
```

Load into PostgreSQL:
```
import psycopg2

def load_to_db(clean_data):
    conn = psycopg2.connect("dbname=mydb user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO weather (city, temperature, condition)
        VALUES (%s, %s, %s)
    """, (clean_data["city"], clean_data["temperature"], clean_data["condition"]))
    conn.commit()
```

## Automating API Calls in ETL Workflows
* Apache Airflow	Schedule & monitor API ETL jobs
* Luigi	Lightweight task orchestration
* Azure Data Factory	Cloud-based ETL with REST support
* n8n / Zapier	No-code automation of API calls

Example Airflow DAG Task:
```
from airflow.operators.python_operator import PythonOperator

fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather,
    dag=dag
)
```

## Handling API Pagination

```
def fetch_all():
    page = 1
    all_data = []

    while True:
        res = requests.get(f"https://api.example.com/data?page={page}")
        data = res.json()
        if not data:
            break
        all_data.extend(data)
        page += 1
```

## Error Handling & Logging
* Log all API requests and responses
* Retry failed requests (429, 503, etc.)
* Catch & record unexpected formats or missing fields

```
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    log_error(e)
```

## Pushing Data to APIs
Some APIs let you load or update data, e.g.:
* Update inventory in an ERP system
* Send user info to an analytics tool
* Report metrics to a logging API

```
requests.post("https://api.example.com/track", json=payload, headers=headers)
```
