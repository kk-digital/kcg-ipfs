from llm_wrapper.llm_wrapper import LLMRequest
import tqdm

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
        print("Processing queue of LLM model: %s" % self.model_name)

        for request in tqdm.tqdm(self.queue, desc="Processing requests"):
            result = self.llm_wrapper.make_request(request)
            results.append(result)
        
        print("Processing done.")
        if clear_queue: self.queue = []  # Clear the queue after processing
        return results