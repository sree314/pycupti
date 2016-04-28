# pycupti.py
# Wrapper for CUDA's CUPTI library.
#
# Author: Sreepathi Pai <sreepai@ices.utexas.edu> 
#
# Year: 2016
#
# Includes contents of the file cupti.h and subject to the same copyright license

from .types import *
from .constants import *

class CUPTIError(Exception):
    def __init__(self, value):
        self.value = value
        self.desc = cuptiGetResultString(value)

    def __str__(self):
        return "%d: %s" % (self.value, self.desc)

cupti = ctypes.cdll.LoadLibrary('libcupti.so')

_cuptiGetVersion = cupti['cuptiGetVersion']
_cuptiGetVersion.argtypes = [ctypes.POINTER(ctypes.c_int)]
_cuptiGetVersion.restype = CUptiResult

def cuptiGetVersion():
    v = ctypes.c_int(0)
    res = _cuptiGetVersion(v)

    if res == CUPTI_SUCCESS:
        return v.value
    else:
        raise CUPTIError(res)

#CUptiResult cuptiMetricGetAttribute ( CUpti_MetricID metric, CUpti_MetricAttribute attrib, size_t* valueSize, void* value )

_cuptiMetricGetAttribute = cupti['cuptiMetricGetAttribute']
_cuptiMetricGetAttribute.restype = CUptiResult
_cuptiMetricGetAttribute.argtypes = [CUpti_MetricID, CUpti_MetricAttribute, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p]


def cuptiMetricGetAttribute(metric, attrib):
    if attrib in (CUPTI_METRIC_ATTR_NAME, CUPTI_METRIC_ATTR_SHORT_DESCRIPTION, CUPTI_METRIC_ATTR_LONG_DESCRIPTION):
        arg1 = ctypes.create_string_buffer(512)
        sz = ctypes.c_size_t(len(arg1))

        r = _cuptiMetricGetAttribute(metric, attrib, sz, arg1)

        if r != CUPTI_SUCCESS:
            raise CUPTIError(r)
        else:
            if sz.value == len(arg1):
                # no null byte
                return arg1[:sz.value]
            else:
                # discard null byte
                return arg1[:sz.value-1]

    elif attrib in (CUPTI_METRIC_ATTR_CATEGORY, CUPTI_METRIC_ATTR_VALUE_KIND, CUPTI_METRIC_ATTR_EVALUATION_MODE):
        arg1 = ctypes.c_int(0)
        sz = ctypes.c_size_t(ctypes.sizeof(ctypes.c_int))

        r = _cuptiMetricGetAttribute(metric, attrib, sz, ctypes.byref(arg1))
        
        if r != CUPTI_SUCCESS:
            raise CUPTIError(r)
        else:
            if sz.value == ctypes.sizeof(ctypes.c_int):
                return arg1.value
            else:                
                # not of type int!
                assert False, sz.value
    else:
        raise NotImplementedError
    

# CUptiResult cuptiDeviceGetNumMetrics ( CUdevice device, uint32_t* numMetrics ) 
_cuptiDeviceGetNumMetrics = cupti['cuptiDeviceGetNumMetrics']
_cuptiDeviceGetNumMetrics.restype = CUptiResult
_cuptiDeviceGetNumMetrics.argtypes = [ctypes.c_int, 
                                      ctypes.POINTER(ctypes.c_uint32)]

def cuptiDeviceGetNumMetrics(device = 0):
    d = ctypes.c_int(device)
    n = ctypes.c_uint32(0)

    r = _cuptiDeviceGetNumMetrics(d, n)

    if r == CUPTI_SUCCESS:
        return n.value
    else:
        raise CUPTIError(r)


# CUptiResult cuptiDeviceEnumMetrics ( CUdevice device, size_t* arraySizeBytes, CUpti_MetricID* metricArray ) 

_cuptiDeviceEnumMetrics = cupti['cuptiDeviceEnumMetrics']
_cuptiDeviceEnumMetrics.restype = CUptiResult
_cuptiDeviceEnumMetrics.argtypes = [CUdevice, 
                                    ctypes.POINTER(ctypes.c_size_t), 
                                    ctypes.POINTER(CUpti_MetricID)]

def cuptiDeviceEnumMetrics(device, numMetrics):
    metrics = (CUpti_MetricID * numMetrics)()
    sz = ctypes.c_size_t(ctypes.sizeof(metrics))
    
    r = _cuptiDeviceEnumMetrics(device, ctypes.byref(sz), metrics)

    if r == CUPTI_SUCCESS:
        return metrics[:sz.value/ctypes.sizeof(ctypes.c_int)]
    else:
        raise CUPTIError(r)

# CUptiResult cuptiGetResultString ( CUptiResult result, const char** str )
_cuptiGetResultString = cupti['cuptiGetResultString']
_cuptiGetResultString.restype = CUptiResult
_cuptiGetResultString.argtypes = [CUptiResult, ctypes.c_void_p]

def cuptiGetResultString(result):
    cp = ctypes.c_void_p()

    r = _cuptiGetResultString(result, ctypes.byref(cp))

    if r == CUPTI_SUCCESS:
        return ctypes.c_char_p(cp.value).value
    else:
        raise CUPTIError(r)
