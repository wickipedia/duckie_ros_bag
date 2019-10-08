#!/usr/bin/env python

import rosbag
import os
import numpy as np

bag = rosbag.Bag('/data/example_rosbag_H3.bag')

topics = []
for topic, msg, t in bag.read_messages():
    if topic not in topics:
        topics.append(topic)

for entry in topics:
    messageCount = bag.get_message_count(topic_filters=entry)
    timestamps = []
    timeStampBefore = None
    for topic, msg, t in bag.read_messages(topics = entry):
        timeStampNow = t
	if timeStampBefore is None:
		timeStampBefore = t
		continue
        duration = t - timeStampBefore
	timestamps.append(duration.to_sec())
        timeStampBefore = t
    
    timestampsArray = np.array(timestamps)
    minTime = timestampsArray.min()
    maxTime = timestampsArray.max()
    avgTime = timestampsArray.mean()
    medTime = np.median(timestampsArray)
    print(' ')
    print(entry + ':')
    print('num_messages: ' + str(messageCount))
    print('min: ' + str(minTime))
    print('max: ' + str(maxTime))
    print('average: ' + str(avgTime))
    print('median: ' + str(medTime))
    print(' ')
bag.close()
