fin = open('words.txt')


def has_no_e():
    count = 0
    count_e = 0
    for line in fin:
        word = line.strip()
        count = (count + 1)
        if "e" not in word:
            count_e = (count_e + 1)
            float(count_e)
            float(count)
            print word
    answer = round(float(count_e) / float(count) * 100, 2)

    print ("The percentage is " + str(answer) + "%")

print has_no_e()
