# kcg-ipfs

## maestro

Is an AI assisted task breakdown script which uses the Anthropic API to coordinate the execution workflow. It uses two API models, Opus and Haiku to break an objective into smaller subtasks and solves them. 

### How to set up

#### Using LM Studio

- Download LM Studio online.
- Click "download" in any model. (this will be the AI that will solve the smaller subtasks)
- Click at "Local Server" and start the server.
- run pip install -r maestro\requirements.txt
- run maestro\maestro-lmstudio.py
- Type an objective.
- Type if you want to search on the web to improve the quality of the results.

#### Using server models

- Run pip install -r maestro\requirements.txt
- Open the file of maestro-gpt4o.py
- Replace "YOUR API KEY" to your own API Key
- Run the file.
- Type an objective.