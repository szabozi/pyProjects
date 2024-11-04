def given(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Given {description.format(*args)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def when(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"When {description.format(*args)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def then(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Then {description.format(*args)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def and_(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"And {description.format(*args)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def where(*test_cases):
    def decorator(func):
        def wrapper():
            for test_case in test_cases:
                print(f"\nRunning test case: {test_case}")
                func(*test_case)
        return wrapper
    return decorator
