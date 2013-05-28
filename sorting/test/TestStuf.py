
class TestStuf:
    L = []
    size = 10

    def test(self):
        if len(self.L) != self.size:
            raise AssertionError(
                'size check fail e[%d] a[%d]'
                % (len(self.L), self.size))
        for i in range(self.size):
            if i == 0:
                continue
            d1 = self.L[i - 1]
            d2 = self.L[i]
            if d2 < d1:
                info = '''
test failure : %(i1)d[%(v1)d] > %(i2)d[%(v2)d]  ''' % {
                    'i1': i - 1,
                    'i2': i,
                    'v1': d1,
                    'v2': d2
                }
                raise AssertionError(info)

    def init(self):
        import random
        random.seed()
        self.L = []
        maxvalue = self.size * 10
        for i in range(self.size):
            v = random.randint(0, maxvalue)
            #print '%d %d' % (i, v)
            self.L.append(v)

    def getSortingMethods(self):
        ms = []
        import re
        patt = re.compile(r'''^v\d+$''')
        for m in dir(self):
            if patt.match(m):
                ms.append(m)
        return ms

    def run(self, size=10):
        self.size = size
        import time
        ms = self.getSortingMethods()
        self.init()
        L = list(self.L)
        times = []
        print "un : %s" % str(L)
        for m in ms:
            self.L = list(L)
            start_time = time.time()
            getattr(self, m)()
            end_time = time.time()
            self.test()
            print '%s : %s' % (m, str(self.L))
            times.append('%s used %s' % (m, str(end_time - start_time)))
        for t in times:
            print t
