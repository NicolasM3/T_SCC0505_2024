test-input:
	python3 src/main.py < utils/input.txt

test-input-and-compare:
	python3 src/main.py < utils/input.txt
	diff result.txt utils/expected_output.txt