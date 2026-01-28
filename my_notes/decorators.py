"""Using decorators"""
from functools import wraps

def bold(f):
    @wraps(f)
    def wrapper (text):
        return f(f"<strong>{text}</strong>")
    
    return wrapper

def italic(f):
    @wraps(f)
    def wrapper(text):
        return f(f"<i>{text}</i>")
    
    return wrapper

@bold
@italic
def hello(text):
    return f"Hello {text}"