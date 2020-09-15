# -*- coding: utf-8 -*-

"""
:mod:`sorting` module : sorting functions module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import copy
import random
import numpy as np
import test

def merge (t1,t2, cmp):
    """
    Given two sorted array, creates a fresh sorted array.

    :param t1: An array of objects
    :type t1: Array
    :param t2: An array of objects
    :type t1: Array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: array

    .. note::

       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t1 = numpy.array([0,2,5,6])
    >>> t2 = numpy.array([1,3,4])
    >>> merge(t1,t2,cmp)
    array([0, 1, 2, 3, 4, 5, 6])
    """
    n1 = len(t1)
    n2 = len(t2)
    t = np.zeros(n1+n2,dtype=type(t1[0]))
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm

    :param t: A array of integers
    :type t: array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh array, sorted.
    :rtype: array

    .. note::

       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    >>> import generate
    >>> def cmp_element (x,y):
    ...    return x.cmp(y)
    >>> t = generate.random_array(10)
    >>> merge_sort(t,cmp_element)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)


def quicksort (t,cmp):
    """
    A sorting function implementing the quicksort algorithm

    :param t: An array of Element
    :type t: NumPy array
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing

    .. note::
       *t* is modified during the sort process

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> quicksort(t, cmp)
    >>> t
    array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    quicksort_slice({'data':t, 'left':0, 'right':len(t)-1}, cmp)


def quicksort_slice (s, cmp):
    """
    A sorting function implementing the quicksort algorithm

    :param s: A slice of an array, that is a dictionary with 3 fields :
              data, left, right representing resp. an array of objects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: Nothing

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> quicksort_slice(p, cmp)
    >>> p['data']
    array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    if s['left'] < s['right']:
        s1, s2 = partition(s, cmp)
        quicksort_slice(s1, cmp)
        quicksort_slice(s2, cmp)

def partition (s, cmp):
    """
    Creates two slices from *s* by selecting in the first slice all
    elements being less than the pivot and in the second one all other
    elements.

    :param s: A slice of is a dictionary with 3 fields :
              - data: the array of objects,
              - left: left bound of the slide (a position in the array),
              - right: right bound of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A couple of slices, the first slice contains all elements that are
             less than the pivot, the second one contains all elements that are
             greater than the pivot, the pivot does not belong to any slice.
    :rtype: tuple

    >>> import generate
    >>> import element
    >>> import numpy
    >>> def cmp (x,y):
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
    >>> p = {'left':0,'right':len(t)-1,'data':t}
    >>> pivot = p['data'][p['left']]
    >>> p1,p2 = partition(p,cmp)
    >>> p1['data'][p1['left']:p1['right']+1]
    array([2, 1, 3, 4], dtype=object)
    >>> p2['data'][p2['left']:p2['right']+1]
    array([8, 9, 7, 6], dtype=object)
    >>> inf = True
    >>> for i in range(p1['left'], p1['right']+1):
    ...    if p1['data'][i] >= pivot:
    ...        inf = False
    >>> inf
    True
    """
    i = s['left'] + 1
    j = s['right']
    p = s['data'][s['left']]
    place = s['left']
    while i <= j:
        comp = cmp(s['data'][i], p)
        if comp < 0 :
            s['data'][i], s['data'][place] = s['data'][place], s['data'][i]
            place = i
            i += 1
        else:
            s['data'][i], s['data'][j] = s['data'][j], s['data'][i]
            j -= 1

    p1 = {"data" : s['data'], "left" : s['left'], "right" : place - 1 }
    p2 = {"data" : s['data'], "left" : place + 1, "right": s['right'] }
    return p1, p2


def random_pivot(t):
    return random.randint(t['data']['left'], t['data']['right'])
def first_pivot(s):
    return (s['left'], 0)

def optimal_pivot(s):
    t = s['data']
    r = s['right']-s['left']
    somme = 0
    for i in range(r):
        somme += t[i].value
    optimal_pivot = element.Element(somme // r+1)
    cpt = s['left']
    cpt_comp = 0
    if r == 1:
        return (cpt, cpt_comp)
    else:
        while t[cpt].cmp(optimal_pivot) != 0 and cpt<r+1:
            cpt+=1
            cpt_comp+=1
        return (cpt, cpt_comp)
    

def functionQ_2_3_4():
    """ 
    A function that calaculates the result of 100 sorting 
    """
    with open('2.3.1.4.dat', 'w') as stream:
        somme_r = 0
        somme_f = 0
        for i in range(1, 101):
            t1 = generate.random_array(i)
            rand = quicksort(t1, cmp, random_pivot)
            t2 = generate.random_array(i)
            first = quicksort(t2, cmp, first_pivot)
            somme_r += rand
            somme_f += first
            stream.write('{:d} {:d} {:d}\n'.format(i, first, rand))
        stream.write('moyenne:\npivot aléat.= {:f} comp\npivot 0= {:f} comp'.format(somme_r/100, somme_f/100))


def question_2_3_2_1_1():
    with open('2.3.2.1.1.dat', 'w') as stream:
        somme_r = 0
        somme_f = 0
        somme_o = 0
        for i in range(1, 101):
            t1 = generate.random_array(i)
            rand = quicksort(t1, cmp, random_pivot)
            t2 = generate.random_array(i)
            first = quicksort(t2, cmp, first_pivot)
            t3 = generate.random_array(i)
            opt = quicksort(t3, cmp, optimal_pivot)
            somme_r += rand
            somme_f += first
            somme_o += opt
            stream.write('{:d} {:d} {:d} {:d}\n'.format(i, first, rand, opt))
        stream.write('moyenne:\npremier pivot= {:f} comp\npivot aléatoire= {:f} comp\npivot optimal= {:f} comp\n'.format(somme_f/100,somme_r/100,somme_o/100))
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()