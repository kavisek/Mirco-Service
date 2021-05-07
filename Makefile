

startup:
	docker-compose down
	docker-compose up


zip_database:
	gzip -k ./database/demo-small-en-20170815.sql

unzip_database:
	gzip -k ./database/demo-small-en-20170815.sql