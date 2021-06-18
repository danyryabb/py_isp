def main(name):
    text = input()
    words = text.replace(',', '').replace('.', ' .').split()

    d = {}
    for word in words:
        if word not in d:
            d[word] = 0
        d[word] += 1
    print(d)

    sents = text[:-1].split('.')
    count_word_in_sent = []
    for sent in sents:
        count_word_in_sent.append(len(sent.split()))
    print(count_word_in_sent)

    n = len(count_word_in_sent)
    print(sum(count_word_in_sent)/n)

    # print(count_word_in_sent.sort())
    med = (count_word_in_sent[n//2] + count_word_in_sent[-n//2])/2
    print(med)


if __name__ == '__main__':
    main('PyCharm')
