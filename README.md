docker build --no-cache -t apirandom .

docker images

docker run -d --name apirandom -p 8000:8000 {{image}}
