test-input:
	python3 main.py < input.txt

test-input-and-compare:
	python3 main.py < input.txt
	diff result.txt expected_output.txt