from flask import Flask, render_template, send_file
import os
import matplotlib.pyplot as plt
import io
import datetime

app = Flask(__name__)

def read_temperature_log(log_file):
    if not os.path.exists(log_file):
        return [], []
    
    with open(log_file, "r") as file:
        lines = file.readlines()
    
    timestamps = []
    temperatures = []
    for line in lines:
        timestamp, temperature = line.strip().split(", ")
        cleaned_temperature = temperature.replace("C", "").replace("'", "").strip()  # Clean up extra characters
        temperatures.append(float(cleaned_temperature))  # Convert to float
        timestamps.append(timestamp)
    
    return timestamps, temperatures

@app.route("/")
def index():
    log_file = "cpu_temperature_log.txt"
    timestamps, temperatures = read_temperature_log(log_file)
    
    # Check if data is being passed properly
    if timestamps and temperatures:
        temperature_data = zip(timestamps, temperatures)
    else:
        temperature_data = []
    
    return render_template("index.html", data=temperature_data)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/plot.png")
def plot_temperature():
    log_file = "cpu_temperature_log.txt"
    timestamps, temperatures = read_temperature_log(log_file)

    # Plot the temperature data
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('CPU Temperature Over Time')
    plt.tight_layout()

    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    #can change port as you wish
    app.run(host="0.0.0.0", port=5000, debug=True)
