Example API:

```bash
curl -X POST "http://localhost:8000/login" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=testpassword"

curl -X POST "http://localhost:8081/signup" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"username\":\"example\",\"password\":\"password\"}"
```