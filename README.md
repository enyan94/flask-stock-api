A simple Flask API running in a Docker container.

# Requirements
[docker](https://www.docker.com/get-docker)

# Usage
Clone this repository
```
git clone https://github.com/enyan94/flask-stock-api.git
```

Run docker-compose
```
docker-compose up --build
```

```

Homepage:
https://peaceful-mesa-91320.herokuapp.com/
http://localhost:5000/


API endpoint for a single ticker
Localhost:
http://localhost:5000/api/v1/resources/stocks?ticker=TSLA
Or Heroku instance:
https://peaceful-mesa-91320.herokuapp.com/api/v1/resources/stocks?ticker=TSLA

Example output:
[
  {
    "name": "Tesla", 
    "price": 200.75, 
    "ticker": "TSLA", 
    "timestamp": 1567206098.0
  }, 
  {
    "name": "Tesla", 
    "price": 201.85, 
    "ticker": "TSLA", 
    "timestamp": 1567206201.0
  }, 
  {
    "name": "Tesla", 
    "price": 202.41, 
    "ticker": "TSLA", 
    "timestamp": 1567206261.0
  }
]


API endpoint to view all entries
Localhost:
http://localhost:5000/api/v1/resources/stocks/all
Heroku instance:
https://peaceful-mesa-91320.herokuapp.com/api/v1/resources/stocks/all

Example output:
[
  {
    "name": "Tesla", 
    "price": 200.75, 
    "ticker": "TSLA", 
    "timestamp": 1567206098.0
  }, 
  {
    "name": "Advanced Micro Devices", 
    "price": 25.0, 
    "ticker": "AMD", 
    "timestamp": 1567206098.0
  }, 
  {
    "name": "Tesla", 
    "price": 201.85, 
    "ticker": "TSLA", 
    "timestamp": 1567206201.0
  }, 
  {
    "name": "Advanced Micro Devices", 
    "price": 27.78, 
    "ticker": "AMD", 
    "timestamp": 1567206201.0
  }, 
  {
    "name": "Tesla", 
    "price": 202.41, 
    "ticker": "TSLA", 
    "timestamp": 1567206261.0
  }, 
  {
    "name": "Advanced Micro Devices", 
    "price": 26.39, 
    "ticker": "AMD", 
    "timestamp": 1567206261.0
  }
]
```
