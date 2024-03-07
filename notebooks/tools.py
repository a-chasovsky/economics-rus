import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import time
import datetime as dt


class Stopwatch():

    def start(self):
        time_start = time.time()
        return time_start

    
    def stop_sec(self, start=None):
        if start is None:
            time_sec = time.time()
        else:
            time_sec = time.time() - start
        return time_sec


    def stop(self, start=None):
        if start is None:
            time_format = time.time()
        else:
            time_sec = time.time() - start
            time_sec = dt.timedelta(seconds=np.round(time_sec))
            time_format = str(time_sec)
        return time_format

