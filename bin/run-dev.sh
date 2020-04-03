#!/usr/bin/env bash

# Run a Flask development server
# --debug       # Run it in DEBUG mode.
# --reload      # Monitor Python files for changes and restart server

# Check for docker, if so bind to 0.0.0.0
grep -q docker /proc/1/cgroup
rc=$?
if [[ rc -eq 0 ]]; then
    IP='0.0.0.0'
else
    IP='127.0.0.1'
fi

python master.py -h $IP --debug --reload
