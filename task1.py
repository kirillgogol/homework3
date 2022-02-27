
def validation(type_value=int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                try:
                    args[i] = type_value(args[i])
                except:
                    pass
            args = tuple(args)
            for key, value in kwargs.items():
                try:
                    kwargs.update(
                        {
                            key: type_value(value)
                        }
                    )
                except:
                    pass
            func(*args, **kwargs)
            
        return wrapper
    return decorator


@validation(type_value=int)
def show_params(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for item in kwargs.items():
        print(item, type(item))
    


show_params(1, 2.23, '123', [5, 6, 7], x=12.3, y='144', s='123/321')
