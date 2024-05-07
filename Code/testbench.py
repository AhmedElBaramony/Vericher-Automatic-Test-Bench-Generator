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
stim = generate_stimulus(test_cases)

#####################################################################################

input_ports_test = '\n   '.join([f'reg {port[1]}{port[0]};' for port in inputs])
output_ports_test = '\n '.join([f'wire {port[1]}{port[0]};' for port in outputs])
input_ports_instance = ','.join([f'.{port[0]} ({port[0]})' for port in inputs])
output_ports_instance = ','.join([f'.{port[0]} ({port[0]})' for port in outputs])
#stimuls = ''.join([f'{name}={value}; \n' for name,value in test_cases])

if (clock_signal):
    clk = f""" 
     reg clk;
     initial begin

    // Generate clock
    clk = 0;
    forever #5 clk = ~clk;
  end"""
else:
    clk = ""  


tb_code = f"""
module {output_dict["module_name"]}_tb;

  //INPUTS
    {input_ports_test}
    
  //OUTPUTS
    {output_ports_test}
  
  //INISTANCE
  {output_dict["module_name"]} T ({input_ports_instance},{output_ports_instance});

  {clk}

  initial begin
    // Run the simulation for a specific time

    {stim}

    // End the simulation
    $stop;
  end

endmodule
"""
print (tb_code)

with open(f'{output_dict["module_name"]}_tb.v', 'w') as f:
  f.write(tb_code)
