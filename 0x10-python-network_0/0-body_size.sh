#!/usr/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
echo "$size"
