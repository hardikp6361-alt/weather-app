# India Weather Predictor

A simple first-year Python project that displays weather information and makes a basic next-day temperature prediction for 10 major Indian cities.

## Cities
Delhi, Mumbai, Bengaluru, Chennai, Kolkata, Hyderabad, Pune, Ahmedabad, Jaipur, Lucknow

## Main Features

1. Select an Indian city.
2. Get recent weather data from Open-Meteo.
3. Calculate a simple prediction using recent average temperature.
4. Display temperature, rainfall and prediction in a Tkinter GUI.
5. Save the last prediction in a simple text history file.
6. Handle invalid input and internet errors.

## Technologies

- Python
- Tkinter
- Requests
- Open-Meteo API
- Basic Python lists, dictionaries, functions and file handling

## How to Run

Install Python 3.10 or newer.

Open the project folder in VS Code and run:

```bash
pip install -r requirements.txt
python main.py
```

The application needs an internet connection.

## How the Prediction Works

This is intentionally a simple beginner-level prediction method.

The program gets recent daily temperatures and calculates their average:

Prediction = (Temperature 1 + Temperature 2 + ... + Temperature 7) / 7

The average is then used as the predicted temperature for the next day.

This is an educational project, not a professional weather forecasting system.

## Testing

Run:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
India_Weather_Predictor_Simple/
│
├── main.py
├── requirements.txt
├── README.md
├── statement.md
│
├── weather_app/
│   ├── __init__.py
│   ├── cities.py
│   ├── weather_api.py
│   ├── predictor.py
│   ├── history.py
│   ├── validation.py
│   └── ui.py
│
├── tests/
│   └── test_project.py
│
└── docs/
    ├── diagrams.md
    └── project_report.md
```
