from vparse import *
import itertools


def generate_test_cases(input_signals):
    # Generate all possible combinations of input values
    input_combinations = list(itertools.product(*[range(signal['range'][1] + 1) for signal in input_signals]))

    # Create a list of dictionaries representing test cases
    test_cases = []
    for values in input_combinations:
        test_case = {signal['name']: value for signal, value in zip(input_signals, values)}
        test_cases.append(test_case)

    return test_cases

def generate_stimulus(test_cases):
    stimulus_code = ""

    for i, test_case in enumerate(test_cases, 1):
        stimulus_code += f"#10 "

        # Generate input assignments
        for signal_name, value in test_case.items():
            stimulus_code += f"{signal_name} = {value};"

        # Add a delay or other relevant code if needed

        stimulus_code += "\n "+"  "

    return stimulus_code

# Usage

input_signals = output_dict['input_signals']
test_cases = generate_test_cases(input_signals)
stimulus = generate_stimulus(test_cases)

print('\n')
print(test_cases)
print('\n')
print(stimulus)