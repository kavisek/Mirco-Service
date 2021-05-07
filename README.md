# Predictive Models as Restful APIs


**This project is still in the works**

This is an example of running a FAST API database again a database to make predictions on cost of a flight for a specific time of the of the month.

## Local Deveploment

Unzip the database and start the api service using docker compose locally.

```bash
# Unzip airline databbase
make unzip_database

# Run docker-compose
make startup
```

Once the docker finishes setting up database, cache, and api in the compose file. You can access the API at http://localhost:80 and the documentation can be accessed at http://localhost:80/docs.

### References

- https://fastapi.tiangolo.com/tutorial/sql-databases/
- https://hub.docker.com/_/postgres
- https://hub.docker.com/_/redis
