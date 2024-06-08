import runner

def initCompiler():
    while True:
        text = input('compile: ')
        result, error = runner.run(f'<stdin>', text)

        if error: print(error.as_string())
        else: print(f'\n\n{result}\n\n')

initCompiler()