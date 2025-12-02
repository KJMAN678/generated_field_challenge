#!/bin/sh
docker compose down
docker compose build
docker compose up -d
sleep 5
docker compose exec backend uv run manage.py create_dummy_books
