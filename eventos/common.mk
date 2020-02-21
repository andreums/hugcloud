current_makefile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(dir $(current_makefile_path))

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(current_makefile_path) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: list
list: ## List all cloud functions deployed in region
	gcloud functions list

.PHONY: describe
describe: ## Get information about one function
	gcloud functions describe $(FUNCTION_NAME)

.PHONY: delete
delete: ## Removes deployment	
	gcloud functions delete --quiet $(FUNCTION_NAME)

.PHONY: deploy
deploy: ## Deploys function
	gcloud functions deploy $(FUNCTION_NAME) --runtime python37 --trigger-http $(DEPLOY_PARAMS)

.PHONY: test
test: ## Runs tests locally using pytest
	pytest -v

# python3 -m venv .venv
# source .venv/bin/activate
.PHONY: dependencies
dependencies: ## Installs python dependencies locally
	pip install --upgrade pip
	pip install -r $(addprefix $(current_dir),requirements.txt)
	pip install -r $(addprefix $(current_dir),requirements-dev.txt)

