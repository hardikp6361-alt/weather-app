# Simple Project Diagrams

These diagrams are intentionally simple because this is a first-year, first-semester project.

## 1. System Architecture

```text
+----------------+
|      User      |
+-------+--------+
        |
        v
+----------------+
|  Tkinter GUI   |
+-------+--------+
        |
        v
+----------------+
| Weather API    |
+-------+--------+
        |
        v
+----------------+
| Simple Python  |
| Prediction     |
+-------+--------+
        |
        v
+----------------+
| History File   |
+----------------+
```

## 2. Workflow

```text
Start
  |
  v
Select City
  |
  v
Get Weather Data
  |
  v
Calculate Average
  |
  v
Predict Tomorrow
  |
  v
Display Result
  |
  v
Save History
  |
  v
End
```

## 3. Use Case

```text
             +-------------------------+
             | India Weather Predictor |
             +-------------------------+
              /        |        \
             /         |         \
          Select     Predict     View
           City      Weather    History
             \         |         /
              \        |        /
                   [User]
```

## 4. Simple Sequence

```text
User -> GUI: Select city
User -> GUI: Click Predict
GUI -> API: Request weather
API -> GUI: Return data
GUI -> Predictor: Calculate average
Predictor -> GUI: Return prediction
GUI -> History: Save result
GUI -> User: Display result
```

## 5. Simple Module Diagram

```text
main.py
   |
   v
ui.py
 |  |  |  |  \
 |  |  |  |   \
 v  v  v  v    v
API Predictor History Validation Cities
```

## 6. Storage Design

The project uses a simple text file instead of a database.

```text
prediction_history.txt

Mumbai - Predicted temperature: 28.5 °C
Delhi - Predicted temperature: 31.2 °C
Pune - Predicted temperature: 26.8 °C
```
