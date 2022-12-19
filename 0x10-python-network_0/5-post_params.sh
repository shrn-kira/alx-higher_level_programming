#!/bin/bash
# send a post request to the passed URL and displays the body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
