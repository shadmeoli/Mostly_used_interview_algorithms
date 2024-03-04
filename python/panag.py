def identifyPanag(sentence: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(alphabet)
    sentence = set(sentence.replace(" ", ""))
    print([**sentence])
    # print(sentence.count() == len(alphabet))



identifyPanag("The quick brown fox jumps over the lazy dog")
