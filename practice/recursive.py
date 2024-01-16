def recursive_function(i):
    if i==100:
        return
    recursive_function(i+1)
print(recursive_function(3))