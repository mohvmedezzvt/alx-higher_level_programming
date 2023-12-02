#!/bin/bash
# Sends a JSON POST request to a URL

url="$1"
filename="$2"

# checks if the file is not valid JSON
if ! jq . "$filename" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

curl -sX POST -H "Content-Type: application/json" --data @"$filename" "$url"
