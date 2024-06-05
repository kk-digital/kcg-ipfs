import time
import sys
import os

from openai import OpenAI
base_directory = os.getcwd()
sys.path.insert(0, os.path.join(base_directory, 'wrapper'))

from llm_stub import LLMStub

class LLMRequest:
    # Is the object that represents a request to the LLM.
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.input_tokens = len(input_text.split())
        self.timestamp = time.time()

class LLMResponse:
    # Is the object that represents the response from the LLM.
    def __init__(self, output_text:str):
        self.output_text = output_text
        self.output_tokens = len(output_text.split())
        self.timestamp = time.time()

    def calculate_time_taken(self, request: LLMRequest):
        # Function that takes a LLMRequest (ideally the one used to generate the response)
        # and saves the time taken to process.
        self.time_taken = self.timestamp - request.timestamp

class LLMWrapperOpenAI:
    # It is a wrapper for the OpenAI model.

    def __init__(self, llm_service: OpenAI, model_name = "gpt-3.5-turbo", temperature=0.7):
        self.llm_service = llm_service
        self.model_name = "openai"
        self.temperature = temperature

    def make_request(self, request: LLMRequest) -> LLMResponse:

        response_text = self.llm_service.chat.completions.create(
        model=self.model_name,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": request.input_text}],
        temperature=self.temperature,).choices[0].message.content
        response = LLMResponse(response_text)
        response.calculate_time_taken(request)

        return response
    
class LLMWrapperStub:
    # It is a wrapper for the stub model, which exists just for testing purposes.
    def __init__(self, llm_service: LLMStub):
        self.llm_service = llm_service # a LMStub.
        self.model_name = "stub"


    def make_request(self, request: LLMRequest) -> LLMResponse:
        response_text = self.llm_service.generate(request.input_text)
        response = LLMResponse(response_text)
        response.calculate_time_taken(request)

        return response

class LLMWrapperLMStudio:
    # It is a wrapper for LMStudio models (local ones). It is required to set up LMStudio for them to work.
    def __init__(self, llm_service: OpenAI, lmstudio_model_name = "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF", temperature=0.7):
        self.llm_service = llm_service # an OpenAI object, which is used to use LMStudio models. 
        self.temperature = temperature
        self.model_name = lmstudio_model_name # Change the variable to use any LMStudio models.

    def make_request(self, request: LLMRequest) -> LLMResponse:

        response_text = self.llm_service.chat.completions.create(
        model=self.model_name,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": request.input_text}],
        temperature=self.temperature,).choices[0].message.content

        response = LLMResponse(response_text)
        response.calculate_time_taken(request)

        return response