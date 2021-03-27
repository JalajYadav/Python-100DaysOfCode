PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt",mode="r") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.strip("\n")
        new_letter=letter_content.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
