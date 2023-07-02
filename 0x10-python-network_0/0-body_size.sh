#!/bin/bash
# Display the size of the response body
curl -sI "$1" | awk '/Content-Length/{print $2}'
