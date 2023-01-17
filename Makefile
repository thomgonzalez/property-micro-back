.PHONY: build
build:
	@docker-compose -f docker-compose.yml build

.PHONY: run_dev
run:
	@docker-compose -f docker-compose.yml  up