def sentenceMaker(phrase):
    # Ways questions can start
    questions = ('what','why','how','where','when')

    # Capitalise first letter of phrase
    capitalized = phrase.capitalize()

    # Questions end with question marks
    # Regular sentences end with full stop
    if phrase.startswith(questions):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

output = []
# Read in sentences from user until ended
while True:
    sentence = input("Say something (Finish with /end): ")

    # Leave loop
    if sentence == '/end':
        break

    output.append(sentenceMaker(sentence))

# Print the joined up sentences
print(" ".join(output))

