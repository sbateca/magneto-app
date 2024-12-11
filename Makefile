override SHELL := /bin/bash
compose_command ?= docker-compose

.PHONY: up
up:
	${compose_command} up -d

.PHONY: down
down:
	${compose_command} down

.PHONY: test
test:
	${compose_command} exec magneto-api pytest -vv

.PHONY: clean
clean:
	${compose_command} down --rmi all --volumes --remove-orphans

.PHONY: all
all: clean up