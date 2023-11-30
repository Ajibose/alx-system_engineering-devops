#!/bin/bash
# Request to a URL and display the size of the body of the response
curl -s -w "%{size_download}\n" "$1"
