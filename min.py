
kwl = ['import', 'from', 'class', 'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'return'] 

def dirtify(_f, _o=None):
    _o = _o or "dirty_{}".format(_f)
    indent, old_indent, indent_change = 0, 0, False
    nline = "\n"
    indent_set = False
    indent_div = 1
    skip_line = False
    semi = ";"
    chaining_imports = False

    with open(_f, 'rb') as _s, open(_o, 'wb') as _d:
        for line in _s:
            indent = 0
            for chr in line:
                if ord(chr) == 32:
                    indent += 1
                else:
                    break
        
            if indent and not indent_set:
                indent_div = indent
                indent_set = True

            indent_change = True if old_indent != indent else False

            old_indent = indent
            first_word = line[indent:].split(' ')[0].strip()
            indent /= indent_div
            line = line.strip()
            
            # skip empty lines, comments, docstrings and multi-line strings
            if (skip_line and ("'''" not in line and '"""' not in line)) or not line or not first_word or first_word[0] == "#":
                old_indent = -1
                continue

            if skip_line and ("'''" in line or '"""' in line):
                skip_line = not skip_line
                old_indent = -1
                continue

            if '"""' in first_word or "'''" in first_word:
                if (line.count('"""') + line.count("'''")) % 2 != 0:
                    skip_line = not skip_line        
                old_indent = -1
                continue
            
            first_word = list(first_word)
            try:
                first_word.pop(first_word.index(":"))
            except ValueError:
                pass

            first_word = ''.join(first_word)
            s_indent = indent
            if first_word in kwl or '@' in first_word:
                semi = ""
                nline = "\n"
            
                if first_word in ['import', 'from']:
                    semi = ";"
                    if chaining_imports:
                        nline = ""
                    else:
                        chaining_imports = True
                else:
                    chaining_imports = False
            
            else:
                semi = ";"
                print indent_change 
                if not indent_change:
                    nline = ""
                    s_indent = 1
                else:
                    nline = "\n"
            
            _d.write(nline + " " * s_indent + line + semi)            

if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) < 2:
        print argv[0]
        print(" !! error: no input file provided\n :: usage: python %s <input_file> [<output_file>}" % argv[0])
        exit(1)
    dirtify(*argv[1:])

