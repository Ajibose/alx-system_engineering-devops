#!/usr/bin/env bash
# Request to a URL and display the size of the body of the response
curl -w "%{size_download}" "$1"
