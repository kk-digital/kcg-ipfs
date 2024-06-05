# LLM Wrapper Library

Library made for reporting each request and where they go. Input tokens, output tokens, etc.

It includes a LLMRequest object for input and an LLMResponse object for the outputs.

A wrapper object for each type of model (LLMWraperOpenAI, LLMWrapperLMStudio and LLMWrapperStub) to wrap the requests.

A LLMWrapperManager object to manage the wrappers and manage their processes into queues.

## Example Usage

### Step 1: Creating the models
```python

stub_model = LLMStub()
openai_model = OpenAI(base_url="https://api.openai.com", api_key="YOURAPIKEY")
lmstudio_model =  OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
```
### Step 2: Inserting them into a wrapper
```python
wrapper_openai = LLMWrapperOpenAI(openai_model)
wrapper_lmstudio = LLMWrapperLMStudio(lmstudio_model)
wrapper_stub = LLMWrapperStub(stub_model)
```

### Step 3: Inserting the wrappers into a wrapper manager
```python
openai_manager = LLMWrapperManager(wrapper_openai)
lmstudio_manager = LLMWrapperManager(wrapper_lmstudio)
stub_manager = LLMWrapperManager(wrapper_stub)
```

### Step 4: Creating a request and adding them into the queue
```python
sample_request_text = "sample text" # the input text
request_object = LLMRequest(sample_request_text)

openai_manager = LLMWrapperManager(wrapper_openai)
lmstudio_manager = LLMWrapperManager(wrapper_lmstudio)
stub_manager = LLMWrapperManager(wrapper_stub)

openai_manager.add_request_to_queue(request_object)
lmstudio_manager.add_request_to_queue(request_object)
stub_manager.add_request_to_queue(request_object)
```

### Step 5: Processing the queue and extracting the results
```python
# output is in list of LLMResponse

results_openai = openai_manager.process_queue(clear_queue=False)
results_lmstudio = lmstudio_manager.process_queue(clear_queue=False)
results_stub = stub_manager.process_queue(clear_queue=False)
```

### Step 6: Extract info from the results 
```python
for idx, result in enumerate(results_openai):
    print(result.output_text) # the output text
    print(result.output_tokens) # the output tokens
    print(result.calculate_time_taken(openai_manager.queue[idx])) # the time taken to process the text

for input_object in openai_manager.queue:
    print(input_object.input_text) # the input text
    print(input_object.input_tokens) # the input tokens
```