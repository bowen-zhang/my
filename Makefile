PYTHON = python3

setup: setup-python setup-third-party setup-docker build-proto init-db

setup-python:
	pip3 install -r requirements.txt --user

setup-third-party:
	cd third_party/intel && make init

setup-docker:
	curl -sSL https://get.docker.com | sh
	sudo usermod -aG docker pi
	newgrp docker
	# Allow connection from container to host
	sudo iptables -A INPUT -i docker0 -j ACCEPT	

build:
	cd src && make build-proto
	npx webpack src/proto/export.js

run-envoy:
	docker build -t my/envoy -f envoy.dockerfile .
	docker rm -f my.envoy || true
	docker run --name my.envoy -d -p 8082:8082 --restart always my/envoy

deploy: build
	docker-compose up -d