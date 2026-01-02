from calculator import evaluate, EvalError


def repl():
	print("Simple calculator. Type 'quit' or 'exit' to leave.")
	while True:
		try:
			s = input('> ').strip()
		except (EOFError, KeyboardInterrupt):
			print()
			break

		if not s:
			continue
		if s.lower() in ('quit', 'exit'):
			break
		if s.lower() in ('help', '?'):
			print("Enter arithmetic expressions, e.g. 2+3*(4-1).")
			continue

		try:
			result = evaluate(s)
		except EvalError as e:
			print('Error:', e)
		else:
			print(result)


if __name__ == '__main__':
	repl()



