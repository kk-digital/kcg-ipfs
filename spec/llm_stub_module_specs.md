Statically Typed Class:

Use Python's type hints to ensure static typing.

API Specifications:

Python Usage:

get_completion(prompt: str) -> str: Takes a prompt and returns a completion.

list_models() -> List[str]: Returns a list of available models.

HTTP Usage:

POST /v1/engines/<engine_id>/completions: Accepts a JSON payload with a prompt and returns a completion.

GET /v1/models: Returns a JSON list of available models.
