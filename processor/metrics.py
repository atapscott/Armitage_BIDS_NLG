import numpy


def mean(magnitude: list):
    return numpy.mean(magnitude)


def standard_deviation(magnitude: list):
    np_array = numpy.array(magnitude)
    return numpy.std(np_array, axis=0)
