from Processor import DataInput
from Processor import Processor
import utils

def read_states():
    states_amount = int(input())
    return states_amount

def read_terminal_data():
    input_string = str(input()).split()
    terminal_sets_amount = input_string.pop(0)
    terminal_sets = input_string
    return terminal_sets_amount, terminal_sets
    
def read_acceptance_data():
    input_string = str(input()).split()
    acceptance_states_amount = int(input_string.pop(0))
    acceptance_states = input_string
    return acceptance_states_amount, acceptance_states

def read_transitions_data():
    acceptance_states_amount = int(input())
    acceptance_states = [input() for _ in range(acceptance_states_amount)]
    return acceptance_states_amount, acceptance_states

def read_input_strings():
    input_strings_amount = int(input())
    input_strings = [input() for _ in range(input_strings_amount)]
    return input_strings_amount, input_strings

def read_input():
    data = DataInput()

    data.states_amount = read_states()
    data.terminal_sets_amount, data.terminal_sets = read_terminal_data()
    data.acceptance_states_amout, data.acceptance_states = read_acceptance_data()
    data.transitions_amount, data.transitions = read_transitions_data()
    data.input_strings_amount, data.input_strings = read_input_strings()

    return data


def main():
    input_info = read_input()
    processor = Processor(input_info)

    # print(input_info.to_string())
    columns_index = list(range(input_info.states_amount))
    # print(utils.print_matrix(processor.matrix, columns_index, input_info.terminal_sets))
    final_state = processor.data.states_amount - 1
    for input_string in input_info.input_strings:
        if(input_string == "-"):
            print("rejeita")
            continue

        last_state = processor.process(input_string)
        if(int(last_state) != int(final_state)):
            print("rejeita")
        else:
            print("aceita")


if __name__ == "__main__":
    main()