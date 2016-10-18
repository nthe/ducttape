
import os
import sys
from time import sleep

# TODO:
# 1. re-run on save / size change
# 2. clear screen each run
# 3. show locals globals, locals or watched

def co_routine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def reader(_file, target):
    _former_size = -1
    while True:
        _f = open(_file, 'rb')
        _f.seek(0, 0)
        program = _f.read()
        if _former_size == os.path.getmtime(_file):
            sleep(0.5)
            continue
        else:
            _former_size = os.path.getmtime(_file)
            target.send(program)


@co_routine
def runner(target):
    _iteration = 0
    while True:
        program = (yield)
        ns = {}
        # os.system('cls')
        try:
            code = compile(program, '<string>', 'exec')
            exec code in ns
            success = True
        except Exception as e:
            success = False
            target.send(e)
        _iteration += 1
        print "\n___iteration: " + str(_iteration) + " -> {}\n".format("success" if success else "error")


@co_routine
def exception_handler():
    while True:
        exc = (yield)
        print " ", exc.__class__.__name__
        print " ", exc.args[0]
        print "  {} @ {}:{}".format(exc.args[1][0], exc.args[1][2], exc.args[1][3])
        print "  > message:", repr(exc.message)


def watch(file_path):
    file_path = os.path.abspath(file_path)
    reader(file_path, runner(exception_handler()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: python {} <python_module.py>".format(__file__)
        sys.exit(-1)
    watch(sys.argv[1])
