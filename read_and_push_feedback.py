#!/usr/bin/env python3

import os
import requests

dir="/data/feedback"
file_list=[]
feedback_list=[]
feed={}

for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        file_list.append(f)
print(file_list)
for file in file_list:
    with open(file) as f:
        feed["title"]= f.readline().splitlines()
        feed["name"]= f.readline().splitlines()
        feed["date"]= f.readline().splitlines()
        feed["feedback"]= f.readline().splitlines()
# append a copy of dict to remove any reference
    feedback_list.append(feed.copy())

for feedback in feedback_list:
    response = requests.post("http://server_IP/feedback/", data=feedback)
