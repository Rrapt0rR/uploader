#!/usr/bin/env bash

# Run a Gunicorn production server
# --workers     # Number of worker processes
# --bind        # Bind to host:port
# --worker-class # Use specific worker class (gevent)
# talos:app     # Run the 'app' project in the file 'master.py'
gunicorn --workers 4 --bind 0.0.0.0:5000 --worker-class gevent wsgi:app
