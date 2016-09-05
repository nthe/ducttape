
import random
import sys

ri = random.randint
vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def text(file_name, size, word_len=(3, 7), sentence_len=(3, 14)):
    """ Generate text file containing dummy text
    :param str file_name:       Name of output file.
    :param int size:            Size of output file in bytes.
    :param tuple word_len:      Variance of word length.
    :param tuple sentence_len:  Variance of sentence length.
    """
    c_size = 0
    
    if size < 1:
        size = 1000

    with open(file_name, 'wb') as d:

        while c_size < size:    
            sentence_length = ri(*sentence_len)
            sentence = ''

            for _ in range(sentence_length):
                word = ''
                word_length = ri(*word_len)

                for i in range(word_length):
                    if i % 7 == 0:
                        word += random.choice(vowels)
                    else:
                        word += chr(ri(97, 122))
                
                word += ' '
                sentence += word
            
            sentence = sentence[0].capitalize() + sentence[1:-1] + '.\n'
            
            if c_size % 150 < 15:
                d.write('\n')
            
            d.write(sentence)
            c_size = d.tell()


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print " ! usage: python gen.py <output_file_name> <size_in_bytes> "
        sys.exit(1)
    
    file_name, size = sys.argv[1:]
    text(file_name, int(size))

