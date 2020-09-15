# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import sys
import experience
import marker
import numpy as np
import sorting as sort

def compare (m1,m2):
    global cpt
    cpt += 1
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers 
    :type markers: Numpy array of String
    :param positive: The list of positive markers
    :type positive: Numpy array of String
    :return: The list of negative markers
    :rtype: Numpy array of String
    """
    negative = np.array([])
    for i in range(len(markers)):
        cmp = 0
        for j in range(len(positive)):
            if compare(markers[i], positive[j]) == 0:
                break
            else :
                cmp += 1  
        if cmp == len(positive):
            negative = np.append(negative, markers[i])
    return negative

# STRATEGY 2
def binary_search(element, positive):
    """
       The function use the binary search algorithm.
       if the element exist in the list of positive markers, the function will return the index of that element.
       otherwise -1 is returned.
    """
    i, j = 0, len(positive)-1
    while i < j:
        k = (i + j) // 2
        if compare(element, positive[k]) <= 0:
            j = k
        else:
            i = k + 1
    return [compare(element, positive[i]), i]

def negative_markers2(markers,positive):
    negative = np.array([])
    positive_sorted = sort.merge_sort(positive, compare)
    for i in markers:
        index = binary_search(i, positive_sorted)
        if index[0] != 0:
            negative = np.append(negative, i)
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    negative = np.array([])
    markers_sorted = sort.merge_sort(markers, compare)
    positive_sorted = sort.merge_sort(positive, compare)
    m_ind = 0
    p_ind = 0
    while (p_ind < len(positive_sorted)) and (m_ind < len(markers_sorted)):
        marker = markers_sorted[m_ind]
        cmp = compare(marker, positive_sorted[p_ind])
        if cmp == 0:
            m_ind += 1
            p_ind += 1
        elif cmp == -1:
            negative = np.append(negative, marker)
            m_ind += 1
        else:
            p_ind += 1
    negative = np.append(negative, markers_sorted[m_ind:])
    return negative     
            


if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    assert (m > 0), "The number of markers must be greater than 0"
    assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
    
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()

    print("Markers: %s" % (markers))
    print("Positive markers: %s" % (positive))
    
    # test stategy 1
    cpt = 0
    print("Negative markers: %s" % (negative_markers1(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))

    # test stategy 2
    cpt = 0
    print("Negative markers: %s" % (negative_markers2(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))

    # test stategy 3
    cpt = 0
    print("Negative markers: %s" % (negative_markers3(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))
    
    # test question 1.5.3
    ma = 10
    for p in range(1, ma+1):
        exp = experience.Experience(p, ma)
        positive = exp.get_positive_markers()
        # test stategy 1
        cpt = 0
        negative_markers1(markers, positive)
        cpt1 = cpt

        # test stategy 2
        cpt = 0
        negative_markers2(markers, positive)
        cpt2 = cpt

        # test stategy 3
        cpt = 0
        negative_markers3(markers, positive)
         
        print("{:3d} {:3d} {:5d} {:5d} {:5d}".format(ma, p, cpt1, cpt2, cpt))
        
    # test creation des dix fichier avec m different de 10 à 100
    # Ce programme lance la création des dix fichiers, qui est demandé à la question 1.5.4 
    for m in range(10, 100 + 1, 10):
        fichier = open("dix_fichiers/tp1-"+str(m)+".dat", "w")
        for p in range(1, m+1):           
            exp = experience.Experience(p, m)
            markers = exp.get_markers()
            positive = exp.get_positive_markers()
            
            # test stategy 1
            cpt = 0
            negative_markers1(markers, positive)
            cpt1 = cpt

            # test stategy 2
            cpt = 0
            negative_markers2(markers, positive)
            cpt2 = cpt

            # test stategy 3
            cpt = 0
            negative_markers3(markers, positive)
            ligne = "{:3d} {:3d} {:5d} {:5d} {:5d}\n".format(m, p, cpt1, cpt2, cpt)
            fichier.write(ligne)
