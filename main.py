import runner

def initCompiler():
    while True:
        text = input('compile > ')
        result, error = runner.run('<stdin>', text)

        if error: print(error.as_string())
        else: print(result)

initCompiler()