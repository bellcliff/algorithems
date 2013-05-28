# encoding: utf-8

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class CombSorting(TestStuf):
    '''
    The basic idea is to eliminate turtles,
or small values near the end of the list, since in a bubble sort these
slow the sorting down tremendously. Rabbits, large values around the
beginning of the list, do not pose a problem in bubble sort.
    In bubble sort, when any two elements are compared,
they always have a gap (distance from each other) of 1.
The basic idea of comb sort is that the gap can be much more than
1 (Shell sort is also based on this idea,
but it is a modification of insertion sort rather than bubble sort).
    In other words, the inner loop of bubble sort,
which does the actual swap, is modified such that gap
between swapped elements goes down (for each iteration of outer loop)
in steps of shrink factor. i.e. [ input size / shrink factor,
input size / shrink factor^2, input size / shrink factor^3, ...., 1 ].
Unlike in bubble sort, where the gap is constant i.e. 1.
    The gap starts out as the length of the list being sorted
divided by the shrink factor (generally 1.3; see below),
and the list is sorted with that value (rounded down to an integer if needed)
as the gap. Then the gap is divided by the shrink factor again,
the list is sorted with this new gap, and the process repeats until
the gap is 1. At this point, comb sort continues using a gap of 1 until
the list is fully sorted. The final stage of the sort is thus equivalent
to a bubble sort, but by this time most turtles have been dealt with,
so a bubble sort will be efficient.
    The shrink factor has a great effect on the efficiency of comb sort.
In the original article, the author suggested .
A value too small slows the algorithm down because more comparisons
must be made, whereas a value too large means that no comparisons
will be made. Lacey and Box empirically found (by testing Combsort on
over 200,000 random lists) the shrink factor of 1.3 to be the best.
    '''

    def v1(self):
        ''' '''
        gap = len(self.L)
        shrink = 1.3
        swapped = False
        while True:
            if gap == 1 and not swapped:
                break
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            i = 0
            swapped = False
            while i + gap < len(self.L):
                if self.L[i] > self.L[i + gap]:
                    self.L[i], self.L[i + gap] = self.L[i + gap], self.L[i]
                    swapped = True
                i += 1


sort = CombSorting()
sort.run()
