#!/usr/bin/env python

from pycupti import *
import pycuda.driver    

if __name__ == "__main__":
    print "CUPTI version", cuptiGetVersion()
    #pycuda.driver.init()
    #numMetrics = cuptiDeviceGetNumMetrics(0)
    #metrics = cuptiDeviceEnumMetrics(0, numMetrics)
    #print "Number of metrics:", numMetrics, len(metrics)

    #print cuptiGetResultString(2)
    #print cuptiMetricGetAttribute(1279, CUPTI_METRIC_ATTR_VALUE_KIND)
