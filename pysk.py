
import sys
from ast import literal_eval


def parse(f, source, word, jump):

    if source not in ['json', 'text']:
        print(' ! cannot process input file. json/text file only')
        sys.exit(1)

    if source == 'json':
        word = '"{}"'.format(word)

    f = open(f, 'rb')
    f.seek(0, 2)
    size = f.tell()
    word_size = len(word)
    scan_size = size - word_size

    jump = jump or 1
    off = int(scan_size * (jump / 100.))
    results = []

    f.seek(0, 0)

    if source == 'json':
        while off < scan_size:
            f.seek(off, 0)
            off += 1

            if word == f.read(word_size):

                while ord(f.read(1)) != 58:
                    pass

                ch = 0
                value = ''
                apostrophe = False
                b = 0
                p = 0
                c = 0

                while ch != 44 or ((b + p + c) > 0) or apostrophe:
                    ch = ord(f.read(1))

                    if ch == 34:
                        apostrophe = not apostrophe

                    elif ch == 91:
                        b += 1

                    elif ch == 40:
                        p += 1

                    elif ch == 123:
                        c += 1

                    elif ch == 93:
                        b -= 1

                    elif ch == 41:
                        p -= 1

                    elif ch == 125:
                        c -= 1

                    value = '{}{}'.format(value, chr(ch))

                value = value[:-1].strip()
                results.append(literal_eval(value))
    
    else:
        occurrences = []

        while off < scan_size:
            f.seek(off, 0)
            off += 1
            if word == f.read(word_size):

                match_pos = off - 1
                end_pos = match_pos

                while ord(f.read(1)) != 10:
                    end_pos = f.tell()
                
                f.seek(match_pos, 0)

                while ord(f.read(1)) != 10:
                    start_pos = f.tell()
                    f.seek(-2, 1)
                
                occurrences.append([start_pos, end_pos])
        
        for occurrence in occurrences:
            f.seek(occurrence[0], 0)
            results.append(f.read(occurrence[1] - occurrence[0]).strip())
    
    if not results:
        return None

    return dict(word=results)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 5:
        print " ! expecting 4 arguments\n > python <source_file> <method=[json|text]> <word> <offset=[0-100]>"
        sys.exit()
    source, method, word, jump = sys.argv[1:]
    print parse(source, method, word, int(jump))
        