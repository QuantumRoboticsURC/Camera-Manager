#!/usr/bin/env python
import rospy
from camera_manager.srv import camera_photo, camera_photoResponse
from sensor_msgs.msg import CompressedImage


def callback(data):
    global d 
    d= data

def camPicture():
    return camera_photoResponse(d)

def server():
    print("Entering server")
    rospy.init_node("camera_server")
    rospy.Subscriber("/usb_camera/image_raw/compressed",CompressedImage,callback)
    s = rospy.Service("camera_info",camera_photo, camPicture)
    rospy.spin()

server()