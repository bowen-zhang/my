PYTHON = python3
PYTHONPATH = $(CURDIR):$(CURDIR)/..

init-db:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) tools/init_db.py

build: build-proto
	docker-compose build

build-proto:
	cd proto && make build

run-frontend:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) frontend/main.py

run-backend:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) backend/main.py

console:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON)