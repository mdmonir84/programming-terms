# Ref: https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators
# Example-01
from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


print(hello())        # returns "<b><i>hello world</i></b>"
print(hello.__name__)  # with functools.wraps() this returns "hello"
print(log('hello'))   # returns "<b><i>hello</i></b>"
