def mocking_spongebob(sentence):
    meme = ""
    length =len(sentence)
    position = 0

    while position < length:
        if sentence[position] == " ":
            meme += " "
            position += 1

        elif position % 2 == 0:
            meme = meme + sentence[position].lower()
            position += 1

        else:
            meme = meme + sentence[position].upper()
            position += 1

    return meme

print(mocking_spongebob("goof moring class"))