FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev && \
    apt-get clean

RUN pip3 install pythonnet

WORKDIR /app
COPY main.py .

CMD ["python3", "main.py"]
