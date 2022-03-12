#AUTHOR: DIVYA N
#DATE: 03.06.2022

#import libraries
import time
import os
import board
import busio
import adafruit_bno055
#from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()

"""
#bonus: function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge')
        #PATH TO YOUR GITHUB REPO
        repo.git.add('folder path')
        #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')
"""
  
#SET THRESHOLD
threshold = 4

#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration

    #CHECK IF READINGS ARE ABOVE THRESHOLD

    if abs(int(accelX or 0)) > threshold and abs(int(accelY or 0)) > threshold and abs(int(accelZ or 0)) > threshold:
        #PAUSE
        #TAKE/SAVE/UPLOAD A PICTURE 
      name = "NarayananD"     #Last Name, First Initial  ex. FoxJ
        
      if name:
        t = time.strftime("_%H%M%S")      # current time string
        imgname = ('/home/pi/FlatSat/Images/%s%s' % (name,t)) #change directory to your folder
        camera.capture(imgname);
    #PAUSE