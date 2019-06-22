## This script is to shunt between REST and the jetson's Python API.
from flask import Flask
from flask import request
from jetbot import Robot
import time


app = Flask(__name__)
robot = Robot()

print('Semi-ready')
print('http://10.19.67.180:5000/MoveTreads/?left=0.3&right=0.3&impulse=10')
print(' or')
print('http://127.0.0.1:5000/MoveTreads/?left=0.3&right=-0.3&impulse=10')
print('')

@app.route('/MoveTreads/', methods=['GET'])
def MoveTreads():
    leftTread = float(request.args.get('left'))
    rightTread = float(request.args.get('right'))
    impulse = float(request.args.get('impulse'))
    robot.set_motors(leftTread, rightTread)
    time.sleep(impulse)
    robot.stop()
    return('OK')

app.run(host='0.0.0.0')

