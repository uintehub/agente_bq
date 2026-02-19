# bq-adk-agent

# BigQuery ADK Agent
This repository contains the code for the BigQuery ADK Agent. Follow the instructions below to set up your environment in Google Cloud Shell and install the necessary dependencies.

# Environment Setup

## 0. Service Account Permissions
Assign the AI Platform Reasoning Engine Service Agent "service-<YOUR-PROJECT-NUMBER-ID>@gcp-sa-aiplatform-re.iam.gserviceaccount.com" the roles: BigQuery User, BigQuery Data Viewer, and Vertex AI User.

## 1. Prepare Google Cloud Shell
Return to Cloud Shell and ensure you are in your home directory. We will create a virtual Python environment and install the required packages.

Open a new terminal tab in Cloud Shell and run the following commands to create and navigate to a working directory:

```
git clone https://gitlab.com/carlos-navarro-anez/bq-adk-agent.git
cd bq-adk-agent
```

(Note: If you have already cloned this repository, ensure you navigate into the project folder instead of creating a new empty directory).

## 2. Create and Activate Virtual Environment
Create a virtual Python environment to manage dependencies:
```
python -m venv .venv
```

Activate the virtual environment:
```
source .venv/bin/activate
```

## 3. Install Dependencies
Install Google's ADK and AI-Platform python packages.

Note: The AI platform and pandas package are specifically required to evaluate the BigQuery agent.

Run the following command:
```
pip install google-adk google-cloud-aiplatform[evaluation] pandas
```
## 4. Run ADK

Run the following command:
```
adk web
```

# Agent Engine Deployment

Root folder

Run the following command:
```
cd bq-adk-agent
```

## 1: Install the ADK CLI
Since you are in Cloud Shell, ensure the ADK library is installed and the CLI is available in your path.
```
pip install google-adk
```

## 2. 
Run this command to tell your shell where to look for the tool:
```
export PATH="$HOME/.local/bin:$PATH"
which adk
```

## 3: Run the ADK Deploy Command
Use the adk deploy agent_engine command. This wrapper handles the packaging, staging to GCS, and creation of the Reasoning Engine in Vertex AI.

Run the following command:
```
adk deploy agent_engine \
     --project=<YOUR-PROJECT-ID> \
     --region=<LOCATION> \
     --staging_bucket=<YOUR-STAGING-BUCKET> \
     --display_name="bigquery-data-agent" \
     --env_file=data_agent_app/.env \
     ./data_agent_app
```

# Gemini Enterprise Registering

Run the following command:
```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: <YOUR-PROJECT-ID>" \
"https://discoveryengine.googleapis.com/v1alpha/projects/<YOUR-PROJECT-NUMBER>/locations/<GE-APP-LOCATION>/collections/default_collection/engines/<GE-APP-ID>/assistants/default_assistant/agents" \
-d '{
 "displayName": "Data Analytics Agent",
  "description": "Convert data into insights with natural language",
  "adk_agent_definition": {
    "tool_settings": {
      "tool_description": "Retrive data with SQL from BigQuery to answer analytical questions"
    },
    "provisioned_reasoning_engine": {
      "reasoning_engine": "<AGENT-ENGINE-RESOURCE-ID>"
    }
  }
}'
```
If the app is located in US and not Global change the API URL to "https://us-discoveryengine.googleapis.com/v1alpha/projects/<YOUR-PROJECT-NUMBER>/locations/GE-APP-LOCATION/collections/default_collection/engines/GE-APP-ID/assistants/default_assistant/agents"

# Agent Engine Forced Deletion

Run the following command:
```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://us-central1-aiplatform.googleapis.com/v1beta1/<AGENT-ENGINE-RESOURCE-ID>?force=true"
```

Usage
(You can add instructions here on how to run the agent once the environment is set up, for example: python main.py)