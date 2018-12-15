import sys

last_word = None
count = 0

for line in sys.stdin:
    word, one = line.split("\t")
    if last_word is None:
        last_word = word
        count +=1
    elif last_word == word:
        count += 1
    else:
        sys.stdout.write("{0}\t{1}\n".format(last_word, count))
        last_word = word
        count = 1

sys.stdout.write("{0}\t{1}\n".format(last_word, count))

