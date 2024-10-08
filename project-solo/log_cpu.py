import os
import time

def get_cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").strip()

def log_cpu_temperature(log_file):
    with open(log_file, "a") as file:
        while True:
            temperature = get_cpu_temperature()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}, {temperature}\n")
            file.flush()
            time.sleep(10)  # Log temperature every 10 seconds

if __name__ == "__main__":
    log_file = "cpu_temperature_log.txt"
    log_cpu_temperature(log_file)
