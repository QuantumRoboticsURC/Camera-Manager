#!/usr/bin/env python
import rospy
from camera_manager.srv import camera_photo, camera_photoResponse
from sensor_msgs.msg import CompressedImage

d=CompressedImage()

def callback(data):
    print("callback")
    global d 
    d = data
   

def camPicture(req):
    global d
    print("service")
    return camera_photoResponse(d)

def server():
    print("Entering server ")
    rospy.init_node("camera_server")
    rospy.Subscriber("/usb_cam/image_raw/compressed",CompressedImage,callback)
    s = rospy.Service("camera_info",camera_photo, camPicture)
    rospy.spin()

server()