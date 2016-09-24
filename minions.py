def minion(string):
    person_a_name = 'Stuart'
    person_b_name = 'Kevin'
    letter_list = list(string)
    l = len(letter_list)
    vowel = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    all_word = []
    person_a_words = 0
    person_b_words = 0

    all_word = (letter_list[start:end+1] for start in xrange(l) for end in xrange(start, l))

    for idx, letter in enumerate(letter_list):
        if letter in vowel:
            person_b_words += len(letter_list) - idx
        else:
            person_a_words += len(letter_list) - idx
    if person_a_words == person_b_words:
        print 'Draw'
    elif person_a_words > person_b_words:
        print person_a_name, person_a_words
    elif person_b_words > person_a_words:
        print person_b_name, person_b_words

def main():
    str = raw_input()
    minion(str.upper())

if __name__ == '__main__':
    main()
