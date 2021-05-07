# Predictive Models as Restful APIs


**This project is still in the works**

This is an example of running a FAST API with a postgres database backend again a database to make predictions on the cost of a flight for a specific time of the month.

## Local Deveploment

Unzip the database and start the api service using docker compose locally.

```bash
# Unzip airline databbase
make unzip_database

# Run docker-compose
make startup
```

Once the docker finishes setting up database, cache, and api in the compose file. You can access the API at http://localhost:80 and the documentation can be accessed at http://localhost:80/docs.

The documentation will provide your example curl request to interact with your api.

```bash
# Post data to the api.
curl -X 'POST' \
  'http://localhost/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "password": "string"
}'
```

And to fetch results back.

```bash
# Fetch results from the API.
curl -X 'GET' \
  'http://localhost/users/?skip=0&limit=100' \
  -H 'accept: application/json'
```


### Database Access

To query your historal results via an IDE. You can query the database with the following credentials on your laptop.

host: localhost
port: 5284
username: demo
password: demo

### References

- https://fastapi.tiangolo.com/tutorial/sql-databases/
- https://hub.docker.com/_/postgres
- https://hub.docker.com/_/redis
