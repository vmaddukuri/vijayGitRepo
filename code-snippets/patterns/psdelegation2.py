class yrangeiterator(object):
    def __init__(self, yrange_object):
        self.yr = yrange_object

    def next(self):
        if self.yr.start < self.yr.end:
            temp = self.yr.start
            self.yr.start += 1
        else:
            raise StopIteration()
        return temp

class yrange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return yrangeiterator(self)


for item in yrange(1, 10):
    print item