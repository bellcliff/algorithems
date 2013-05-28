# encoding: utf-8

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class QuickSorting(TestStuf):
    '''
from [[http://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F]]
function quicksort(q)
    var list less, pivotList, greater
    if length(q) ≤ 1 {
        return q
    } else {
        select a pivot value pivot from q
        for each x in q except the pivot element
            if x < pivot then add x to less
            if x ≥ pivot then add x to greater
        add pivot to pivotList
        return concatenate(quicksort(less), pivotList, quicksort(greater))
    }
    '''
    def v1(self):
        def qsort(q):
            if not q:
                return []
            return qsort([x for x in q[1:] if x < q[0]]) + q[0:1] + \
                qsort([x for x in q[1:] if x >= q[0]])
        self.L = qsort(self.L)

    def v2(self):
        def qsort(q):
            l = []
            g = []
            n = []
            if len(q) <= 1:
                return q
            else:
                # select key
                key = q[len(q) - 1]
                for i in q[0: -1]:
                    if i < key:
                        l.append(i)
                    else:
                        g.append(i)
                n.extend(qsort(l))
                n.append(key)
                n.extend(qsort(g))
                return n
        self.L = qsort(self.L)

pop = QuickSorting()
pop.run(10)
