# **Image Pixels Coordinates generation from Corner Points and dimensions**.

## Introduction

A webapp that return pixel coordinates is response to the Corner coordinates and size of the image. The coordinates and size is passed to the server in form of POST requests in specific format described below. Response is a matrix containing the image pixel coordinates.

## Installation

1. Clone/Download repository

2. Go to the root folder.

3. Open terminal and build from Dockerfile. Use the following command.
   => docker build - t "imagename" . (include the period at the end of the line.)
4. Run using the following command.
   => docker run -p 8000:8000 "imagename"

---

## Running the app

To produce the Solution, POST request should be sent to http://localhost:<portnumber>/getvals e.g (http://0.0.0.0:8000/getval) in the following format:

                {
                    "Dimensions": [3, 3],
                    "Points": [[1.5, 1.5],[4.0, 1.5],[1.5, 8.0],[4.0, 8.0]]
                }

The key values and the format are validated and should be exact or an exception is going to be raised.

In previous commits e.g. "cfa64cb" , there was a strict format validation method using regex which I changed in the later commits. The reason was the payload was required to be
stringified if I wanted to follow the input format instructed e.g. [(3,4),(5,6),(6,6),(7,7)]. If you are interested in finding out more please check the given SHA.
