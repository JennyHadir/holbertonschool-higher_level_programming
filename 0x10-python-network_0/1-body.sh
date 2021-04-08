#!/bin/bash
# Takes in a URL, sends a GET request to that URL, displays the size of the body
curl -sI $1
