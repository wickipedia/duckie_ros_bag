#!/usr/bin/env python

import rosbag
import os
import numpy as np

bag = rosbag.Bag('/data/example_rosbag_H3.bag')
print("read bag file")
topics = []
for topic, msg, t in bag.read_messages():
    if topic not in topics:
        topics.append(topic)

for topic in topics:
    messageCount = bag.get_message_count(topic_filters=topic)
    timestamps = []
    timestampPrev = None
    timestampsArray = []

    for topic, msg, t in bag.read_messages(topics = topic):
        timestamp = t
        if timestampPrev != None:
            time_diff = timestamp - timestampPrev
            timestamps.append(time_diff)    
            timestampPrev = t
        else:
            timestampPrev = t
    timestampsArray = np.array(timestamps)
    
    minTime = timestampsArray.min()
    maxTime = timestampsArray.max()
    avgTime = timestampsArray.mean()
    medTime = np.median(timestampsArray)
    print(' ')
    print(topic + ':')
    print('num_messages: ' + str(messageCount))
    print('min: ' + str(minTime))
    print('max: ' + str(maxTime))
    print('average: ' + str(avgTime))
    print('median: ' + str(medTime))
    print(' ')
bag.close()
