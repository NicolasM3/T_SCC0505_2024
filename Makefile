test-input:
	python3 main.py < input.txt

test-input-and-compare:
	python3 main.py < input.txt > output.txt
	diff output.txt program_output.txt