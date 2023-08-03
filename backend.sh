#!/bin/bash
export $(xargs < .env)

# wait for MySQL server starting
while :
do
    echo "Checking if MySQL is up on port 3306"
    if echo > /dev/tcp/mysql/3306 2>/dev/null; then
        echo "MySQL is up"
        break
    else
        echo "MySQL is not up. Sleep for 5 seconds then check again."
        sleep 5
    fi
done
sleep 5

# only initial migration
if [ -d "alembic" ]; then 
  alembic revision --autogenerate -m "default model migration"
  alembic upgrade head
  echo exist; 
else  
  alembic init alembic;
  # Set DATABASE_URL
  DATABASE_URL="mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}/${MYSQL_DATABASE}"
  # Replace sqlalchemy.url in alembic.ini
  sed -i "s|sqlalchemy.url = .*|sqlalchemy.url = ${DATABASE_URL}|" /home/appuser/devcon/alembic.ini
  # exchange ./alembic/env.py already updated.
  cp ./env.py ./alembic/env.py

  #alembic revision --autogenerate -m "default model migration"
  alembic upgrade head
fi

# start uvicorn server
uvicorn server.main:app --reload --host 0.0.0.0 --port ${PORT_BACK}