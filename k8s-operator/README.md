# k8s-operator
K8s operator for the [Eidolon project](http://www.eidolonai.com)

## Description
Three k8s operators are implemented in this project:
- **Eidolon Machine Operator**: This operator is responsible for managing the Eidolon Machine resources.
- **Eidolon Agent Operator**: This operator is responsible for managing Eidolon Agent resources.
- **Eidolon Reference Operator**: This operator is responsible for managing Eidolon Reference resources.

## Getting Started

### Prerequisites
- go version v1.20.0+
- Access to a Kubernetes v1.11.3+ cluster.
- OLM.  The instructions for our operator on operatorhub.io will install OLM for you.
 
### Installation
*TODO* - once we are accepted on operatorhub.io

### Local machine deployment
We recommend minikube for local development.  You can find the minikube installation instructions [here](https://minikube.sigs.k8s.io/docs/start/).

We develop on a Mac, so we have the following instructions for Mac users.  If you are on a different OS, please refer to the minikube documentation.

* Install minikube
    ```sh
    brew install minikube
    minikube start --driver qemu --network socket_vmnet  —disk 100g
    alias kubectl="minikube kubectl --"   
    eval $(minikube docker-env)
    minikube addons enable ingress 
    ```

* Install your secrets

  A secret with the needed credentials for your Eidolon deployment. The name of the secret is `eidolon`.

  See the [Eidolon documentation](https://www.eidolonai.com) for more information on what keys you need. 
  However, typically this will be a secret with the following keys:
  - `OLLAMA_URL` - the URL for your Ollama deployment if you are using ollama.
  - `OPENAI_API_KEY` - your OpenAI API key if you are using OpenAI.
  - `MISTRAL_API_KEY` - your Mistral API key if you are using Mistral.
  - `ANTHROPIC_API_KEY` - your Anthropic API key if you are using Anthropic.

  If you already have a .env file with these keys, you can create the secret with the following command:
  - `kubectl create secret generic eidolon --from-env-file=<location of your env file>/.env`


*TODO* - once we are accepted on operatorhub.io