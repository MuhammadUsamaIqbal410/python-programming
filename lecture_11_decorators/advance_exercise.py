def cache_decorator(function):
    result = {}

    def wrapper(n):
        if n in result:
            print(f"Getting from the cache: {n}")
            return result[n]
        else:
            print(f"Claulating for: {n}")
            new_result = function (n)
            result [n] = new_result
            return new_result
        
    return wrapper

@cache_decorator
def square(n):
    return n *n

print(square(2))
print(square(5))
print(square(27))
print(square(2))
print(square(34))
print(square(27))

