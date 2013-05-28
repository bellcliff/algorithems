# encoding: utf-8

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class SelectionSorting(TestStuf):
    '''
/* a[0] to a[n-1] is the array to sort */
int i,j;
int iMin;
 
/* advance the position through the entire array */
/*   (could do j < n-1 because single element is also min element) */
for (j = 0; j < n-1; j++) {
    /* find the min element in the unsorted a[j .. n-1] */
 
    /* assume the min is the first element */
    iMin = j;
    /* test against elements after j to find the smallest */
    for ( i = j+1; i < n; i++) {
        /* if this element is less, then it is the new minimum */
        if (a[i] < a[iMin]) {
            /* found new minimum; remember its index */
            iMin = i;
        }
    }
 
    /* iMin is the index of the minimum element. Swap it with the current position */
    if ( iMin != j ) {
        swap(a[j], a[iMin]);
    }
}
    '''
    def v1(self):
        '''
Heapsort greatly improves the basic algorithm
by using an implicit heap data structure
to speed up finding and removing the lowest datum.
If implemented correctly, the heap will allow
finding the next lowest element in Θ(log n) time
instead of Θ(n) for the inner loop in normal selection sort,
reducing the total running time to Θ(n log n).
        '''
        L = self.L
        for j in range(len(L) - 1):
            iMin = j
            for i in range(j + 1, len(L)):
                if L[i] < L[iMin]:
                    iMin = i
            L[j], L[iMin] = L[iMin], L[j]
        self.L = L

sort = SelectionSorting()
sort.run()
