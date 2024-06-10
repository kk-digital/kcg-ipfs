'''
eval for openai
 this script takes in the humaneval dataset and generates an output file with completions for it using lmstudio
 this can be used for evaluation together with evaluate_functional_correctness to check the accuracy of your model.
'''

import fire
import sys
import os

from openai import OpenAI
from llm_wrapper.llm_manager import LLMWrapperManager
from llm_wrapper.llm_wrapper import LLMRequest, LLMResponse, LLMWrapperOpenAI
from human_eval.data import read_problems, write_jsonl, split_problems

DEFAULT_OUTPUT_DIR = './humaneval_results/openai.jsonl.gz'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def generate_completions_for_humaneval(model_name: str="gpt-3.5-turbo-0125", tests_per_problem:int = 3, problems_used:int = 164, output_file:str = DEFAULT_OUTPUT_DIR):

    # load the model, wrapper & manager
    model =  OpenAI(api_key=OPENAI_API_KEY)
    wrapper = LLMWrapperOpenAI(model, model_name=model_name)
    manager = LLMWrapperManager(wrapper)

    # read problems and cut up to a certain number
    problems = read_problems()
    problems = split_problems(problems, problems_used)

    # create the requests in the queue
    for problem in problems.values():

        task_id = problem['task_id']
        prompt = problem['prompt']

        # modify the prompt for outputting only code
        prompt = prompt + "# Provide only the complete implementation of the function. Do not include any explanations, comments, \
          examples or Markdown formatting."
        
        for _ in range(tests_per_problem):
            request = LLMRequest(task_id, prompt)
            manager.add_request_to_queue(request)
        
    responses = manager.process_queue()

    # write the list output and write to a file
    samples = []
    for response in responses:

        # removing any markdown outputs
        lines = response.output_text.split('\n')
        cleaned_lines = [line for line in lines if '```' not in line]
        removed_markdown_response = '\n'.join(cleaned_lines)

        samples.append({"task_id": response.task_id, "completion": removed_markdown_response})

    write_jsonl(output_file, samples)

def main():
    
    fire.Fire(generate_completions_for_humaneval)

sys.exit(main())
