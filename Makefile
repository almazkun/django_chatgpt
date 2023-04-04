lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 .
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports .
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 140 .
	pipenv run black .

cov:
	docker compose exec web pip install coverage
	docker compose exec web coverage run ./manage.py test 
	docker compose exec web coverage html
	docker compose exec web coverage report -m

up:
	docker compose up -d web --build
	docker compose up -d nginx
	docker ps -a

ps: 
	docker ps -a

down:
	docker compose down	-v

down_prod:
	docker compose -f docker-compose.prod.yml down -v

_prod:
	docker compose -f docker-compose.prod.yml up db -d --build
	docker compose -f docker-compose.prod.yml up -d --build
	docker ps -a

collectstatic:
	docker compose exec web python manage.py collectstatic --no-input

makemessages:
	docker compose exec web python manage.py makemessages -a

compilemessages:
	docker compose exec web python manage.py compilemessages

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

demo:
	docker compose exec web python manage.py demo
	
build:
	docker compose build

logs:
	docker compose logs -f

logs_prod:
	docker compose -f docker-compose.prod.yml logs -f

test:
	docker compose run --rm --entrypoint="python" web manage.py test ${K}

prod: _prod collectstatic

prod_restart: down_prod prod