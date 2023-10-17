start:
	docker compose up -d --scale api-one=3 --scale api-two=3

rebuild:
	docker compose build

stop:
	docker compose down