"""

Answer to Question 6.7

The percentage will be 50-50 since still the chance for each pregnancy is 50-50,
no matter when a family decides to stop having more children. Biology hasn't changed

"""
import numpy as numpy


def apocalypse(generation, numFamilies):
    Bcounter = 0
    Gcounter = 0

    for i in range(numFamilies):
        numChild = 0
        while numChild <= generation:
            nextChild = numpy.random.randint(2)
            if nextChild == 1:
                Gcounter += 1
                break
            else:
                Bcounter += 1
                numChild += 1
    print("Girls number = " + str(Gcounter) + ", Boys number = " + str(Bcounter))

if __name__ == '__main__':
    apocalypse(10, 100)