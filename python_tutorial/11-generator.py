def index_words(text):
    result = []
    if text:
        result.append(0)
    for idx, letter in enumerate(text):
        if letter == ' ':
            result.append(idx + 1)
    return result

def index_iter(text):
    if text:
        yield 0
    for idx, letter in enumerate(text):
        if letter == ' ':
            yield idx + 1

def func1():
    sentence = "컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관"
    result = index_words(sentence)
    print(result)

def func2():
    sentence = "컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관"
    it = index_iter(sentence)
    for i in it:
        print(i)

if __name__ == "__main__":
    # func1()
    func2()