import unittest

def square(x):
    "raise x to the second power"
    return x*x

print('Testing square function')
unittest.expectedFailure(square(10))
test.