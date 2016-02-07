from flask import Flask, render_template, Response
import cv2
import time
import sys
import numpy
import RPi.GPIO as GPIO

	
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/right')
def right():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.LOW)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	
	

	
	time.sleep(20)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)	
	
	GPIO.cleanup()
	return "right"
	##return "hello right"
@app.route('/left')
def left():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.LOW)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.LOW)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.HIGH)
	
	

	
	time.sleep(20)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)	
	
	GPIO.cleanup()
	#return render_template('index.html')
		
	return "hello left"
@app.route('/down')
def down():
	#return render_template('index.html')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.HIGH)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.LOW)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.HIGH)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	
	

	
	time.sleep(20)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)


	
	
	GPIO.cleanup()
	return "Down"

@app.route('/up')
def up():
	#return render_template('index.html')
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	

	GPIO.setup(11,GPIO.OUT)
	GPIO.output(11,GPIO.LOW)
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,GPIO.HIGH)
	
	

	
	time.sleep(20)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)

	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)


	
	GPIO.cleanup()
	return "up"

	

if __name__ == '__main__':
    app.run(host='192.168.0.102',port=7000,debug=True)
    #192.168.0.103