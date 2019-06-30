class SampledSeries(object):
    def __init__(self, series, fs):
        self.series = series
        self.fs = fs
    def delta_t(self):
        return 1.0/self.fs
    def duration(self):
        '''to get the duration of the series
        '''
        N = len(self.series)-1
        return N*self.delta_t()