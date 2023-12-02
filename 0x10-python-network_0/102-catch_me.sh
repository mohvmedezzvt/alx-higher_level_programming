#!/bin/bash
# Causes the server to respond with a message containing You got me!
curl -sLX PUT -H origin:School 0.0.0.0:5000/catch_me
