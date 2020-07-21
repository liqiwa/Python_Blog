import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call %s' % func.__name__)
            return wrapper
            end = func(*args,**kw)
        print('end call %s' % func.__name__)
        return end
    return decorator







@log
def f():
    pass



@log('execute')
def f():
    pass

if __name__ == "__main__":
    run()
