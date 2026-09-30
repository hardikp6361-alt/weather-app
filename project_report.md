# India Weather Predictor — Project Report

## 1. Cover Page

**Project:** India Weather Predictor  
**Student Name:** ____________________  
**Registration Number:** ____________________  
**Course:** ____________________  
**Faculty:** ____________________  
**Academic Year:** 2026–27

---

## 2. Introduction

Weather information is useful for everyday activities. This project creates a simple Python application that provides recent weather information and makes a basic next-day temperature prediction for ten major Indian cities.

The project is designed as a first-year programming project. It uses basic Python concepts such as functions, dictionaries, lists, file handling, API requests and a graphical user interface.

## 3. Problem Statement

Many users want a simple way to check weather information for different cities. The objective is to create a small application where the user can select an Indian city and receive a simple prediction based on recent temperature data.

## 4. Objectives

- Learn how to work with an online API.
- Use Python dictionaries and lists to store information.
- Build a simple graphical interface.
- Perform a basic mathematical prediction.
- Save prediction results.
- Practice modular programming and testing.

## 5. Functional Requirements

### FR1 — City Selection
The user can select one of ten Indian cities.

### FR2 — Weather Data
The application retrieves recent temperature and rainfall information.

### FR3 — Prediction
The application calculates the average of recent temperatures and uses it as a simple next-day prediction.

### FR4 — Result Display
The prediction and recent rainfall information are displayed in the GUI.

### FR5 — History
The application saves predictions in a text file.

### FR6 — Error Handling
The application displays an error message if weather data cannot be retrieved.

## 6. Non-Functional Requirements

### Usability
The GUI is simple and easy to understand.

### Performance
Only a small amount of recent weather data is retrieved.

### Reliability
Errors from the weather service are caught and displayed.

### Maintainability
The project is divided into small Python modules.

### Portability
The application can run on a computer with Python installed.

## 7. System Architecture

The application follows a simple structure:

User → Tkinter GUI → Weather API → Prediction Function → History File

## 8. Design Diagrams

The project contains architecture, workflow, use-case, sequence and module diagrams in `docs/diagrams.md`.

## 9. Design Decisions and Rationale

### Why Python?
Python is beginner-friendly and was suitable for implementing the project using simple programming concepts.

### Why Tkinter?
Tkinter is included with standard Python installations and makes it possible to create a desktop GUI without learning a large framework.

### Why Open-Meteo?
It provides weather data through an online API and does not require a complicated setup for this student project.

### Why use an average?
A simple average is easy to understand and demonstrates mathematical processing of real-world data. It also keeps the project appropriate for a first-semester programming course.

### Why a text file?
A text file is sufficient for this small project and demonstrates basic file handling without introducing unnecessary database complexity.

## 10. Implementation Details

The application is divided into modules:

- `main.py` — starts the application.
- `cities.py` — stores city names and coordinates.
- `weather_api.py` — retrieves weather data.
- `predictor.py` — performs the average-based prediction.
- `history.py` — saves and reads prediction history.
- `validation.py` — checks user input.
- `ui.py` — creates the Tkinter interface.
- `test_project.py` — tests basic functions.

## 11. Prediction Method

The application retrieves recent daily temperatures.

If the temperatures are:

```text
28, 29, 30, 27, 28, 29, 30
```

the prediction is:

```text
(28 + 29 + 30 + 27 + 28 + 29 + 30) / 7
= 28.71 °C
```

The application displays approximately:

```text
Predicted temperature for tomorrow: 28.7 °C
```

This is a simple educational prediction and should not be treated as an official weather forecast.

## 12. Screenshots / Results

Add screenshots of:

1. Main application window.
2. City selection.
3. Prediction result.
4. Prediction history.
5. Optional terminal showing successful tests.

## 13. Testing Approach

The project uses Python's `unittest` module.

Tests verify:

- exactly ten cities are available;
- valid and invalid cities are handled;
- average temperature is calculated correctly;
- prediction uses the average;
- rainfall messages work.

Run:

```bash
python -m unittest discover -s tests -v
```

## 14. Challenges Faced

- Understanding how an API returns JSON data.
- Connecting API data to a GUI.
- Handling internet errors.
- Organizing the project into separate files.
- Learning how to save results using file handling.

## 15. Learnings

Through this project I learned:

- how Python functions work together;
- how dictionaries can store real-world information;
- how to make API requests;
- how JSON data can be processed;
- how to create a basic GUI;
- how to use files for storing results;
- how to write simple unit tests;
- how modular programming makes a project easier to understand.

## 16. Future Enhancements

- Add humidity and wind speed.
- Add weather icons.
- Add graphs.
- Add more cities.
- Add a seven-day forecast.
- Improve the prediction method.
- Add a database when the project becomes larger.

## 17. References

1. VITyarthi — Build Your Own Project guidelines.
2. Open-Meteo weather API.
3. Python documentation.
4. Tkinter documentation.
