# encoding: utf-8

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf

'''
# Sort an array a[0...n-1].
gaps = [701, 301, 132, 57, 23, 10, 4, 1]
 
foreach (gap in gaps)
{
    # Do an insertion sort for each gap size.
    for (i = gap; i < n; i += 1)
    {
        temp = a[i]
        for (j = i; j >= gap and a[j - gap] > temp; j -= gap)
        {
            a[j] = a[j - gap]
        }
        a[j] = temp
    }
 
}
'''
import math


class ShellSort(TestStuf):

    def __sort(self, gmethod):
        L = self.L
        n = len(L)
        gaps = gmethod(n)
        print 'gaps : ' + str(gaps)
        for gap in gmethod(n):
            # do an insertion sort for each gap size
            # print '**' + str(L)
            for i in range(gap, n):
                tmp = L[i]
                j = i
                while j >= gap and L[j - gap] > tmp:
                    L[j] = L[j - gap]
                    j -= gap
                L[j] = tmp
            # print '##' + str(L)

    def gap_shell(self, n):
        '''n / (2**k)'''
        gaps = []
        k = 1
        while True:
            gap = int(n / math.pow(2, k))
            if gap >= 1:
                gaps.append(gap)
                k += 1
            else:
                break
        return gaps

    def gap_frank(self, n):
        gaps = []
        k = 1
        while True:
            gap = int(n / math.pow(2, k + 1)) * 2 + 1
            #print 'k[%d],g[%d]' % (k, gap)
            if gap >= 2:
                gaps.append(gap)
                k += 1
            else:
                break
        gaps.append(1)
        return gaps

    def gap_hibbard(self, n):
        '''2**k - 1'''
        gaps = []
        k = 1
        while True:
            gap = int(math.pow(2, k)) - 1
            if gap > n:
                break
            gaps.append(gap)
            k += 1
        return gaps

    def gap_papernov(self, n):
        '''2**k + 1'''
        gaps = [1]
        k = 1
        while True:
            gap = int(math.pow(2, k)) + 1
            if gap > n:
                break
            gaps.append(gap)
            k += 1
        return gaps

    def gap_knuth(self, n):
        '''(3**k -1)/2, less than n / 3'''
        gaps = []
        k = 1
        while True:
            gap = (int(math.pow(3, k)) - 1) / 2
            if gap < n / 3:
                gaps.append(gap)
                k += 1
            else:
                break
        return gaps

    def v1(self):
        self.__sort(self.gap_shell)

    def v2(self):
        self.__sort(self.gap_frank)

    def v3(self):
        self.__sort(self.gap_hibbard)

    def v4(self):
        self.__sort(self.gap_papernov)

    def v5(self):
        self.__sort(self.gap_knuth)

sort = ShellSort()
sort.run()
