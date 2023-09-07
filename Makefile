.PHONY: lint test up down logs psql

CMD=poetry run
lint:
	$(CMD) flake8 ./
	$(CMD) black ./
	$(CMD) isort ./

test:
	@(CMD) pytest

up:
	@docker-compose up -d

down:
	@docker-compose down

logs:
	@docker-compose logs

psql:
	@docker-compose exec postgres psql -U postgres mydatabase

help:
	@echo "Available targets:"
	@echo " - lint: Lint the project using flake8, black & isort"
	@echo " - test: Run tests using pytest"
	@echo " - up: Start services using docker-compose"
	@echo " - down: Stop services using docker-compose"
