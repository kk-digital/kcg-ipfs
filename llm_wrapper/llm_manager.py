import sys
import os

base_directory = os.getcwd()
sys.path.insert(0, os.path.join(base_directory, 'wrapper'))

from llm_wrapper import LLMRequest

class LLMWrapperManager:
    # The LLMWrapperManager object manages the LLMWrapperOpenAI, LLMWrapperStub or LLMWrapperLMStudio objects.
    # It stacks the LLMRequests into queues to just process the whole queue at once.

    def __init__(self, llm_wrapper):
        self.llm_wrapper = llm_wrapper
        self.model_name = llm_wrapper.model_name #model_name is extracted from LLMWrapper object
        self.queue = []

    def add_request_to_queue(self, request: LLMRequest):
        self.queue.append(request)

    def process_queue(self, clear_queue = True):
        results = []
        for request in self.queue:
            result = self.llm_wrapper.make_request(request)
            results.append(result)
        if clear_queue: self.queue = []  # Clear the queue after processing
        return results