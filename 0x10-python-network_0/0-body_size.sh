#!/usr/bin/env bash
# Request to a URL and display the size of the body of the response
url=$(nslookup "$1")
curl -w "%{size_download}" "$url"
