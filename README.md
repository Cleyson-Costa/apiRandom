docker build -t apirandom .

docker run -d --name apirandom -p 8000:8000 {{image}}
