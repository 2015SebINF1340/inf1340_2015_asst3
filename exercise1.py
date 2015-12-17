#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS
This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):
    """
    Perform select operation on table t that satisfy condition f.
    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    """

    """ the call is passed via the f variable
        so list is sent to filter_employees as an example
    """
    results = []
    for list in t:
         print list
         if(f(list) == True):
           results.append(list)

    return filter(None, results)


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.
    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]
    """
    """I append the "columm" id of the calues I want to project"""
    results = []
    valuePositions = []
    i = 0
    for value in t[0]:
        if( value in r):
            valuePositions.append(i)
        i += 1

    """Once this is done I create a results "table" with only the values selected for projection
       If that values index is in the valuePositions list it is aded to results"""
    for list in t:
      i = 0
      tempList = []
      for v in list:
        if (i in valuePositions):
            tempList.append(v)
        i += 1
      results.append(tempList)

    return results


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.
    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]
    """
    """adding the headers to one another"""
    result = [t1[0] + t2[0]]

    """doing the cross product of all values. I start my iterator at value 1 in order to ignore the value titles"""
    i = 1
    while i < len(t1):
        j = 1
        while j <len(t2):
            result.append(t1[i] + t2[j])
            j += 1
        i += 1


    return result