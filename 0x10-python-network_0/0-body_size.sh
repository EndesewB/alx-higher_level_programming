#!/bin/bash

# Check if a URL is provided
if [ $# -eq 0 ]; then
  echo "Error: No URL provided."
  exit 1
fi

url=$1

# Send request and store the response body in a variable
response=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the size of the response body
echo "Response body size: $response bytes"
