#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me for a response "You got me!"
curl -sX PUT -L -d  "You got me!" 0.0.0.0:5000/catch_me
