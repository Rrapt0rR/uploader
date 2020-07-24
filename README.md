# Uploader
File Uploader for Large Files using Docker containers with a Flask app for Http user interface.

To Start Useing
`docker-compose build`
`docker-compose up`

URL is ported to 5000, you can set to port 80 for production use.
`0.0.0.0:5000`

Files on the server are located under `static/files` but can be directed to anywhere you like.

=== NOTE ===
There is a PostgreSQL docker in this package for authentaction of the Flask app if needed. By default there is no authentaction to upload files, so be aware.

