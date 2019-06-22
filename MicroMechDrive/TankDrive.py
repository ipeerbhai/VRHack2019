## This script is to shunt between REST and the jetson's Python API.
from flask import Flask
from flask import request
from jetbot import Robot
import time


app = Flask(__name__)
robot = Robot()

@app.route('/MoveTreads/', methods=['GET'])
def MoveTreads():
    leftThreadPower = request.args.get('left')
    rightThreadPower = request.args.get('right')
    impulseTime = request.args.get('impulse')
    robot.set_motors(leftThreadPower, rightThreadPower)
    time.sleep(impulseTime)
    robot.stop()


