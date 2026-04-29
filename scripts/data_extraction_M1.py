import os

def extract_answers_sequence(file_path):
    answers = []
    with open(file_path, 'r', encoding='utf-8') as file:
        option_number = 0
        selected_option = 0
        for line in file:
            line = line.strip()
            if line.startswith("Question"):
                option_number = 0
                selected_option = 0
                continue
            if line.startswith("["):
                option_number += 1
                if "[x]" in line.lower():
                    selected_option = option_number
                if option_number == 4:
                    answers.append(selected_option)
    return answers

def write_answers_sequence(answers, n, destination_path):
    os.makedirs(destination_path, exist_ok=True)
    filename = f"answers_list_respondent_{n}.txt"
    full_path = os.path.join(destination_path, filename)
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(str(answers))