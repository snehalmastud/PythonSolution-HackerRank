def wrapper(f):
    def fun(l):
        decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
        return f(decorated_l)
    return fun
