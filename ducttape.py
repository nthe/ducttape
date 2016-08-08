def measure_runtime(func):
    """ Measure runtime of function is seconds.
    :param func: Function, which has to be measured.
    """
    from time import time

    def inner_f(*args, **kwargs):
        _st = time()
        temp_r = func(*args, **kwargs)
        print("<{}>'s runtime: {}(s).".format(func.__name__, time() - _st))
        return temp_r
    return inner_f


def callback(callback=None):
    """ Add callback to function.
    :param callback: Function, which has to be called at end of decorated function.
    """
    def wrapper(func):
        def inner_f(*args, **kwargs):
            temp_r = func(*args, **kwargs)
            if callback: callback()
            return temp_r
        return inner_f
    return wrapper


def assert_result(test_func, propagate=False):
    """ Decorator for result test. Provided test function with be called over return value of decorated function.
    :param propagate: Signalizes whether the error should be propagated to environment.
    :param test_func: Function, which will be executed with return value of decorated function.
    """
    def wrapper(func):
        def inner_f(*args, **kwargs):
            try:
                temp_r = func(*args, **kwargs)
                assert test_func(temp_r)
                return temp_r
            except AssertionError as a_e:
                if propagate:
                    raise AssertionError(*a_e)
                print a_e
        return inner_f
    return wrapper


def do_profile(sort='cumtime', amount=None):
    """ Record profile of decorated function. The profile can be sorted and restricted.
    :param func:        Profiled function.
    """
    def wrapper(func):
        import cProfile
        import pstats
        import StringIO

        file_name = "{}.prof".format(func.__name__)

        def inner_f(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            temp_r = func(*args, **kwargs)
            pr.disable()
            s = StringIO.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats(sort)
            ps.print_stats() if not amount else ps.print_stats(amount)

            with open(file_name, 'w') as d:
                d.write(s.getvalue())
            return temp_r

        return inner_f
    return wrapper


def dict_to_object(_name=None, _dictionary=None):
    """ Create object from dictionary.
    :param _name: Name of object.
    :param _dictionary: Python dict, which will be converter to objects properties.
    """
    return type(_name or "Dicttaped", (object,), _dictionary or {})
