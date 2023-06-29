#!/bin/bash
# A Script that takes in a URL as an argument, sends a GET request to the URL, and then displays the body of the response.
curl "$1" -sX GET -H "X-School-User-Id: 98"
