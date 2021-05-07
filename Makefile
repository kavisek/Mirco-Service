

startup:
	docker-compose down
	docker-compose up

run_api:
	uvicorn sql_app.main:app --reload

zip_database:
	gzip -k ./database/demo-small-en-20170815.sql

unzip_database:
	gzip -dk ./database/demo-small-en-20170815.sql


start_api:
	pip install SQLAlchemy