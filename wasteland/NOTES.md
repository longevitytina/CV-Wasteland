activate v-environment: source .env/bin/activate

start server: python3 manage.py runserver
update models: python3 manage.py makemigrations
python3 manage.py migrate

open shell: python3 manage.py shell

run SQL: psql postgres
\l list databases
\c wasteland

admin: tina
pw:1234
