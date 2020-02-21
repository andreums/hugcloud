FUNCTION_NAME?=recursos2
REGION:=us-east1
FUNCTION_URL:=https://$(REGION)-linear-reason-268216.cloudfunctions.net/$(FUNCTION_NAME)
DEPLOY_PARAMS:=--region $(REGION)

include ../common.mk

.PHONY: test_curl
test_curl: ## Sends a sample request using cURL
	curl -w'\n' -X POST $(FUNCTION_URL) \
		-H "Content-Type: application/json" \
		-d '{ "resourceId": "RES.029", "resourceName": "145 Bernier Plains, Port Leighmouth, NY 92994-8799", "categoryId": "CAT.009", "providerId": "PRO.031", "promotion": false }'

PHONY: test_httpie
test_httpie: ## Sends a sample request using HTTPie
	http -v $(FUNCTION_URL)

