# Requirements to run this project:
1. Docker and docker-compose
2. Python3
3. [Pipenv](https://pipenv.pypa.io/en/latest/)


## Run MYSQL using docker & docker-compose
```bash
sudo docker-compose up
```

# Run Backend

```bash
pipenv shell
pipenv sync
uvicorn main:app --port 8081 --reload
```

```bash
#Signup
curl -X POST "http://localhost:8081/signup" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"username\":\"example\",\"password\":\"password\"}"
#Login
curl -X POST "http://localhost:8081/login" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "username=example&password=password"
```
