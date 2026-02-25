# IoT API Simulation Dashboard Control by Flask

A lightweight, real-time web application built with **Flask** and **Vanilla JavaScript**. This project features a 12-box grid system designed to simulate IoT environments with Sensor (Read) and Actuator (Write) capabilities via RESTful APIs.

---

## 📂 Project Structure


- **`app.py`**: The Flask backend containing the data store and API routes.
- **`requirements.txt`**: Lists the necessary Python libraries (Flask, Flask-CORS).
- **`templates/`**: Contains `index.html` (Main Dashboard) and `test.html` (API Debugger).
- **`static/`**: Holds image assets (`v0-v3.png`, `vx.png`, and `fan.png`).

---

## 🚀 Features

### 📊 Dashboard Layout
The UI is organized into a 2-column by 6-row table:

1. **Boxes 1-6 (Sensor Group)**: 
   - **Type**: UI-to-API.
   - **Interaction**: Managed via UI inputs (Text, Range, Radio).
   - **Logic**: User changes the UI -> Data is written to server -> **External APIs Read** this state.

2. **Boxes 7-10 (Actuator Group)**: 
   - **Type**: API-to-UI.
   - **Interaction**: Display boxes and Logic-based Images.
   - **Logic**: **External API Writes** value -> UI updates immediately (0, 1, 2, 3 maps to `v{n}.png`, others map to `vx.png`).

3. **Boxes 11-12 (Fan Actuators)**: 
   - **Type**: API-to-UI.
   - **Interaction**: Animated Fans.
   - **Logic**: Write speed **1-5** to trigger CSS rotation. 1 is slow, 5 is fast. 0 stops the fan.

---

## 📡 API Endpoints

| Action | Endpoint | Method | Description |
| :--- | :--- | :--- | :--- |
| **Read** | `http://localhost:5050/box{id}/read` | `GET` | Returns current JSON data for the box. |
| **Write** | `http://localhost:5050/box{id}/write/{val}` | `GET/POST` | Updates the value for the specific box. |

---

## 🏃 How to Run

Follow these steps to set up and launch the application locally.

### 1. Setup Virtual Environment
It is highly recommended to use a virtual environment to isolate project dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**

```Bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
While the virtual environment is active, install the required packages:

```bash
pip install -r requirements.txt
```
### 3. Start the Server
```
Run the Flask application:
```
```bash
python app.py
```
The server will start by default on http://127.0.0.1:5050.

### 4. Open in Browser
Main Dashboard: http://localhost:5050

API Test Bench: http://localhost:5050/test

### 🤝 Credits
- Coded by AI
- Directed by Rathachai C


### Final Setup Tips:
1. **The Images**: Ensure you have `v0.png`, `v1.png`, `v2.png`, `v3.png`, `vx.png`, and `fan.png` inside the `static` folder.
2. **CORS**: Ensure `app.py` has `CORS(app)` enabled so the `test.html` page can communicate with the APIs without browser blocks.
