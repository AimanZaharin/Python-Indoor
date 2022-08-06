
def main():
    print("You are indoors, you should not shout or scream.")
    sentence = input("Say something... ")
    toLower(sentence)

def toLower(sentence):
    updatedSentence = sentence.lower()
    print(updatedSentence)

main()