#!/usr/bin/env python                                                                            
 
import rosbag
import os
import numpy as np
from cv_bridge import CvBridge
import cv2

bag_write = rosbag.Bag('/data/processedImg.bag','w')

topics_cam = '/queenmary2/camera_node/image/compressed'

print("Start conversion image")
with rosbag.Bag('/data/2019-10-07-14-50-10.bag', 'r') as bag:
    for topic, CamMsg, t in bag.read_messages(topics= topics_cam):
        cv_image = CvBridge().compressed_imgmsg_to_cv2(CamMsg, desired_encoding="passthrough")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cv_image, str(t),(10,10),font,3,(255,255,255),4)
        ConvertedCamMsg = CvBridge().cv2_to_compressed_imgmsg(cv_image)
        bag_write.write(topics_cam, ConvertedCamMsg, t = t)

bag_write.close()        
