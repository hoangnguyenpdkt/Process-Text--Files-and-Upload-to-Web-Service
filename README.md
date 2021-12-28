# Process Text Files with Python Dictionaries and Upload to Running Web Service

## Introduction
You’re working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company’s website. To do this, you’ll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company’s website (currently using Django).

## What you’ll do
	Use the Python OS module to process a directory of text files 
	Manage information stored in Python dictionaries
	Use the Python requests module to upload content to a running Web service
	Understand basic operations for Python requests like GET and POST methods 
## Writing the scripts
Create the script file
```
	nano run.py
```

Add the following codes:

```python
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

```

Grant executable permission to the run.py script.
```
chmod +x ~/run.py
```
Now, run the run.py script:
```
./run.py
```


Lab-2: Automating Real-World Tasks, Google IT Automation with Python Professional Certificate