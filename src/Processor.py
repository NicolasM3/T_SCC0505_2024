class DataInput:
    def __init__(self):
        self.states_amount = 0                  # Quantidade de estados
        self.terminal_sets_amount = 0           # Quantidade de conjuntos terminais
        self.terminal_sets = []                 # Conjuntos terminais
        self.acceptance_states_amout = 0        # Quantidade de estados de aceitação
        self.acceptance_states = []             # Estados de aceitação
        self.transitions_amount = 0             # Quantidade de transições
        self.transitions = []                   # Transições
        self.input_strings_amount = 0           # Quantidade de strings de entrada
        self.input_strings = []                 # Strings de entrada


    def to_string(self):
        return f"States amount: {self.states_amount}\n" \
               f"Terminal sets amount: {self.terminal_sets_amount}\n" \
               f"Terminal sets: {self.terminal_sets}\n" \
               f"Acceptance states amount: {self.acceptance_states_amout}\n" \
               f"Acceptance states: {self.acceptance_states}\n" \
               f"Transitions amount: {self.transitions_amount}\n" \
               f"Transitions: {self.transitions}\n" \
               f"Input strings amount: {self.input_strings_amount}\n" \
               f"Input strings: {self.input_strings}"

class Processor():
    def __init__(self, data: DataInput):
        self.data = data
        self.terminal_dict = self.build_terminal_sets_dict()
        self.matrix = self.build_matrix()
        

    def build_terminal_sets_dict(self):
        terminal_dict = {}
        for i, terminal_set in enumerate(self.data.terminal_sets):
            terminal_dict[terminal_set] = i
        return terminal_dict

    def build_matrix(self):
        matrix = [[0 for _ in range(int(self.data.terminal_sets_amount))] for _ in range(int(self.data.states_amount))]
        for transition in self.data.transitions:
            transition = transition.split()
            row = int(transition[0])
            column = self.terminal_dict[transition[1]]
            matrix[row][column] = transition[2]
        return matrix

    def _process(self, actual_state: int, terminal_set):
        return self.matrix[int(actual_state)][self.terminal_dict[terminal_set]]

    def process(self, input_string):
        state = 0
        for input_char in input_string:
            state = self._process(state, input_char)

        return state
