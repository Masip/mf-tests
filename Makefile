.PHONY: run_test
run_test:
	docker build . --tag=test:latest
	docker run --network tests test:latest pytest
