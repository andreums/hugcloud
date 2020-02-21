FUNCTION_NAME?=usuarios
REGION:=us-east1
FUNCTION_URL:=https://$(REGION)-linear-reason-268216.cloudfunctions.net/$(FUNCTION_NAME)
DEPLOY_PARAMS:=--region $(REGION)

include ../common.mk

.PHONY: test_curl
test_curl: ## Sends a sample request using cURL
	curl -w'\n' -X POST $(FUNCTION_URL) \
		-H "Content-Type: application/json" \
		-d '{ "email": "daphine@example.org", "name": "Ahmad Wiza", "age": 18 }'

PHONY: test_httpie
test_httpie: ## Sends a sample request using HTTPie
	http -v $(FUNCTION_URL)

