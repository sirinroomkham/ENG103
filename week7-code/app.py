from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)

led = LED(17)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<state>')
def led_control(state):
    if state == 'on':
        led.on()
        message = "LED is ON"
    elif state == 'off':
        led.off()
        message = "LED is OFF"
    else:
        message = "Invalid state"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
