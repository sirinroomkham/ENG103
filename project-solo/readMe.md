# Tutorial: CPU Temperature Logger and Web Display
**Author:** Sirin Roomkham
**Date:** October 2, 2024  
**Version:** v1.0

---

This project logs the CPU temperature of your device at regular intervals and displays the data on a website using Flask. The temperature data is also shown as a graph on the webpage.

## Requirements

- Python 3.x
- Flask
- Matplotlib

## Download the Project from GitHub

To get started, clone the repository from GitHub:

```bash
git clone https://github.com/sirinroomkham/ENG103
```

After cloning, navigate into the project directory:
`cd project-solo`

## Setup Instructions

### 1. Create and Activate a Virtual Environment

First, set up a Python virtual environment to manage the dependencies. Run the following commands in your terminal:


#### On Raspberry Pi:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 2. Install the Required Libraries

```bash
pip install flask matplotlib
```

### 3. Running the Project

You will need to open **two terminals**: one for logging the CPU temperature, and the other for running the web app.

#### Terminal 1: Run the CPU Logging Script

In the first terminal, run the script that logs the CPU temperature:

```bash
python log_cpu.py
```

This script will continuously log the CPU temperature to a text file (`cpu_temperature_log.txt`).

#### Terminal 2: Run the Flask Web App

In the second terminal, start the Flask web app:

```bash
python app.py
```

Once the Flask app is running, open a web browser and go to the following address:

Check ip address of the raspberry pi using `ifconfig` and it should produce ip address e.g., `10.1.1.116`.

```
http://10.1.1.116:5000/
```

You will see the CPU temperature data displayed in both a table and a graph.

### 4. Viewing the Data

- **Table View:** The webpage will display the CPU temperature data in a table format, showing the timestamp and temperature readings.
- **Graph View:** A graph will visualize the temperature changes over time.

## Stopping the App

To stop the logging and web server, simply press `Ctrl + C` in both terminals.

----
<p style="font-size:12px;">Copyright © 2024 Sirin Roomkham. Licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</p>
