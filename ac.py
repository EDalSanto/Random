def autocorrect(input):
    text = input.lower().split()
    for word in text:
        if word == "u":
        	print "word before: ", word
        	print "text before: ", text
            word = word.replace("u", "your sister")
            print "word after: ", word
            print "text after: ", text
        elif "you" in word:
            if word.strip("you") == 'u' or word.strip("you") == '!' or word.strip("you") == " ":
                word = word.replace("you", "your sister")
    return " ".join(text)

print autocorrect('u')