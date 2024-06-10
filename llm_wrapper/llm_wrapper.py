import time
from openai import OpenAI
from mistralai.client import MistralClient
from llm_wrapper.llm_stub import LLMStub

class LLMRequest:
    # Is the object that represents a request to the LLM.
    def __init__(self, task_id: str, input_text: str):
        self.task_id = task_id
        self.input_text = input_text
        self.input_tokens = len(input_text.split())
        self.timestamp = time.time()

class LLMResponse:
    # Is the object that represents the response from the LLM.
    def __init__(self, task_id: str, output_text:str):
        self.task_id = task_id
        self.output_text = output_text
        self.output_tokens = len(output_text.split())
        self.timestamp = time.time()

    def calculate_time_taken(self, request: LLMRequest):
        # Function that takes a LLMRequest (ideally the one used to generate the response)
        # and saves the time taken to process.
        self.time_taken = self.timestamp - request.timestamp

class LLMWrapperOpenAI:
    # It is a wrapper for the OpenAI model.

    def __init__(self, llm_service: OpenAI, model_name:str = "gpt-3.5-turbo-0125", temperature=0.7):
        self.llm_service = llm_service
        self.model_name = model_name
        self.temperature = temperature

    def make_request(self, request: LLMRequest) -> LLMResponse:

        completion = self.llm_service.completions.create(model=self.model_name, prompt=request.input_text)
        response_text = completion.choices[0].text # the output text
        response = LLMResponse(request.task_id, response_text)
        response.calculate_time_taken(request)

        return response
    
class LLMWrapperStub:
    # It is a wrapper for the stub model, which exists just for testing purposes.
    def __init__(self, llm_service: LLMStub):
        self.llm_service = llm_service # a LMStub.
        self.model_name = "stub"


    def make_request(self, request: LLMRequest) -> LLMResponse:
        response_text = self.llm_service.generate(request.input_text)
        response = LLMResponse(request.task_id, response_text)
        response.calculate_time_taken(request)

        return response

class LLMWrapperLMStudio:
    # It is a wrapper for LMStudio models (local ones). It is required to set up LMStudio for them to work.
    def __init__(self, llm_service: OpenAI, lmstudio_model_name:str = "lmstudio_loaded_model", temperature=0.7):
        self.llm_service = llm_service # an OpenAI object, which is used to use LMStudio models. 
        self.temperature = temperature
        self.model_name = lmstudio_model_name # this is irrelevant if the server hasn't loaded multiple models

    def make_request(self, request: LLMRequest) -> LLMResponse:

        completion = self.llm_service.completions.create(model=self.model_name, prompt=request.input_text)
        response_text = completion.choices[0].text # the output text
        response = LLMResponse(request.task_id, response_text)
        response.calculate_time_taken(request)

        return response

class LLMWrapperCodestral:
    # It is a wrapper for the OpenAI model.

    def __init__(self, llm_service: MistralClient, temperature=0.7):
        self.llm_service = llm_service
        self.temperature = temperature
        self.model_name = "codestral-latest"

    def make_request(self, request: LLMRequest) -> LLMResponse:

        response = self.llm_service.completion(
        model=self.model_name,
        prompt=request.input_text
        )
        response_text = response.choices[0].message.content # the output text
        response = LLMResponse(request.task_id, response_text)
        response.calculate_time_taken(request)

        return response