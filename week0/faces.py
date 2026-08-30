# Take some text and convert :) and :( into matching emoji, then return the result
def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")  
    return text

# Ask the user for text, convert it using convert(), then display the result
def main():
    text = input("Text: ")
    print(convert(text))

# Run the program
main()


