#!/bin/bash
# Sends a DELETE request to that URL, displays the body
curl -sL "$1" | grep "Allow" | cut -d " " -f 2
