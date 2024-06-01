import json
import re

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split by tasks
    tasks = content.split('{"task_')
    tasks[1] = tasks [0] + tasks[1]
    tasks = tasks[1:]
    
    result = {"tests": []}
    
    for task in tasks:
        task_lines = task.strip().split('\n')
        
        task_id_line = task_lines[0]
        task_id = re.search(r'id": "([^"]+)"', task_id_line).group(1).split('/')[1]
        
        for line in task_lines:
            if line.startswith("def "):
                function_name = line
        
        description_lines = []
        test_cases = []
        is_description = False
        current_test_case = {}
        
        for line in task_lines:

            if line.startswith('    """'):
                is_description = True
                description_lines.append(line.strip().lstrip('""" '))
                continue
            
            if line.startswith('    >>>'):
                is_description = False
                input_line = line.split('(', 1)[1][:-1]
                output_line = task_lines[task_lines.index(line) + 1].strip()
                current_test_case = {
                    "test_id": len(test_cases) + 1,
                    "input": input_line,
                    "output": output_line
                }
                test_cases.append(current_test_case)

            if is_description:
                description_lines.append(line.strip())
        
        result["tests"].append({
            "name_of_test": function_name,
            "description_of_test": ' '.join(description_lines),
            "test_cases": test_cases
        })
    
    return result

def write_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    input_file = './eval/AutoCoder_HumanEval.txt'
    output_file = './eval/autocoder.json'
    
    parsed_data = parse_input_file(input_file)
    write_to_json(parsed_data, output_file)

    print(f"JSON data successfully written to {output_file}")