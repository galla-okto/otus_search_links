def input_datas(input_questions, input_answers):
    for key, value in input_questions.items():
        while True:
            try:
                line = input(value)
                if line:
                    input_answers[key] = line
                    break
            except ValueError as err:
                print(err)
                continue
            except EOFError:
                break