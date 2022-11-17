FROM python:3

LABEL maintainer="apirandom"

ARG PORT=8000

ENV PORT=${PORT}

WORKDIR /app

#COPY ../src /app

RUN pip install Faker
RUN pip install fastapi
RUN pip install uvicorn
RUN uvicorn main:app --reload

EXPOSE ${PORT}

CMD [ "pip", "run", "start" , "uvicorn"]