## Invoice creating api

Requirements doc:
<https://docs.google.com/document/d/1BXHc1_tzpsqpE1fMqkcWwVFmxDJ9kQNP40dmdYuYTqg>

### Technology stack
 - fastapi, sqlalchemy
 - postgresql

# Quick start
### Start from docker-compose

Create .env file in root and specify values below
```.env
  db_host="postgres"
  db_user="backend_app"
  db_password="root"
  db_port="5432"
  db_database="invoice_db"
  SECRET_AUTH="please, create SECRET_AUTH"
```

Build application from docker-compose.yml file
```bash
docker-compose up --build
```
After it, you need to apply alembic migrations by using this command
```bash
docker-compose exec -it backend alembic upgrade head
```
And we are there, now you can observe and test api endpoint

And open the <http://localhost:8000/docs> for view documentation

