# kcg-ipfs

## Installation

First, clone the repository:

`git clone https://github.com/kk-digital/kcg-ipfs/`

Then, install it using pip:

`pip install -e kcg-ipfs`

## Scripts

#### `$ lmstudio_eval <OPTIONAL_FLAGS>`

Generates completions using LM Studio and the HumanEval.jsonl.gz dataset to benchmark a model in LM Studio. By default, generates the output at ./humaneval_results. Optional flags: `--model_name MODEL_NAME --tests_per_problem TESTS_PER_PROBLEM --output_file OUTPUT_FILE --problems_used PROBLEMS_USED`

#### `$ codestral_eval <OPTIONAL_FLAGS>`

Generates completions using Codestral and the HumanEval.jsonl.gz dataset to benchmark Codestral. By default, generates the output at ./humaneval_results. You'll need a Codestral API key, which you can get at https://console.mistral.ai/codestral. Set it as an environment variable as the name of CODESTRAL_API_KEY. The key is free to use until August 2024, so the testing won't have any costs. Optional flags: `--tests_per_problem TESTS_PER_PROBLEM --output_file OUTPUT_FILE --problems_used PROBLEMS_USED`

#### `$ openai_eval <OPTIONAL_FLAGS>`

Generates completions using OpenAI models (by default, gpt-3.5-turbo-0125). You'll need a OpenAI API key and to set it as OPENAI_API_KEY. By default, generates the output at ./humaneval_results. Optional flags: `-- model_name MODEL_NAME --tests_per_problem TESTS_PER_PROBLEM --output_file OUTPUT_FILE --problems_used PROBLEMS_USED`

#### `$ evaluate_functional_correctness SAMPLE_FILE <OPTIONAL_FLAGS>`

Checks the accuracy of the model-generated completions (the ones in human_eval/eval_scripts) in SAMPLE_FILE from the problems contained in HumanEval.jsonl.gz, which is a benchmark using a compilation of over 100 programming problems created by OpenAI. This script has been forked from OpenAI's human-eval repository, and it only runs on a non-Windows machine.