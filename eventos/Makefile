BUCKET_NAME:=mibucketandreums
FUNCTION_NAME?=eventos
REGION:=us-east1
FUNCTION_URL:=https://$(REGION)-linear-reason-268216.cloudfunctions.net/$(FUNCTION_NAME)
DEPLOY_PARAMS:=--set-env-vars BUCKET_NAME=$(BUCKET_NAME) --region $(REGION)



include ../common.mk

.PHONY: test_curl
test_curl: ## Sends a sample request using cURL
	curl -w'\n' -X POST $(FUNCTION_URL) \
		-H "Content-Type: application/json" \
		-d '{ "tenantId": "airbnb", "eventId": "a0d7f3b9-e463-4027-a729-b1a691001478", "eventTime": 1582314034.9, "processTime": 1582314082.9, "resourceId": "RES.002", "userId": "merilyn@example.net", "countryCode": "GB", "duration": 228, "itemPrice": 19.1 }'

create_bucket: ## Creates the bucket needed for samples
	gsutil mb -c regional -l $(REGION) gs://$(BUCKET_NAME)

list_bucket: ## List bucket contents
	gsutil ls gs://$(BUCKET_NAME)


PHONY: test_httpie
test_httpie: ## Sends a sample request using HTTPie
	http -v $(FUNCTION_URL)

