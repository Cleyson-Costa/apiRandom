docker build -t apirandom .

docker run -d --name apirandom -p 80:80 {{image}}
