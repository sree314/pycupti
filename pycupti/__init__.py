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

# CUptiResult cuptiDeviceGetNumEventDomains ( CUdevice device, uint32_t* numDomains ) 
_cuptiDeviceGetNumEventDomains = cupti['cuptiDeviceGetNumEventDomains']
_cuptiDeviceGetNumEventDomains.restype = CUptiResult
_cuptiDeviceGetNumEventDomains.argtypes = [CUdevice,
                                           ctypes.POINTER(ctypes.c_uint32)]

def cuptiDeviceGetNumEventDomains(device= 0):
    d = CUdevice(device)
    n = ctypes.c_uint32(0)
    r = _cuptiDeviceGetNumEventDomains(d, n)

    if r == CUPTI_SUCCESS:
        return n.value
    else:
        raise CUPTIError(r)

# CUptiResult cuptiEventDomainGetNumEvents ( CUpti_EventDomainID eventDomain, uint32_t* numEvents ) 
_cuptiEventDomainGetNumEvents = cupti['cuptiEventDomainGetNumEvents']
_cuptiEventDomainGetNumEvents.restype = CUptiResult
_cuptiEventDomainGetNumEvents.argtypes = [CUpti_EventDomainID,
                                           ctypes.POINTER(ctypes.c_uint32)]

def cuptiEventDomainGetNumEvents(eventDomain):
    d = CUpti_EventDomainID(eventDomain)
    n = ctypes.c_uint32(0)
    r = _cuptiEventDomainGetNumEvents(d, n)

    if r == CUPTI_SUCCESS:
        return n.value
    else:
        raise CUPTIError(r)

# CUptiResult cuptiDeviceEnumEventDomains ( CUdevice device, size_t* arraySizeBytes, CUpti_EventDomainID* domainArray ) 

_cuptiDeviceEnumEventDomains = cupti["cuptiDeviceEnumEventDomains"]
_cuptiDeviceEnumEventDomains.restype = CUptiResult
_cuptiDeviceEnumEventDomains.argtypes = [CUdevice, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(CUpti_EventDomainID)]

def cuptiDeviceEnumDomains(device, ndomains):
    a = ctypes.c_size_t(ndomains * ctypes.sizeof(CUpti_EventDomainID))
    did = (CUpti_EventDomainID * ndomains)()

    r = _cuptiDeviceEnumEventDomains(device, a, did)

    if r == CUPTI_SUCCESS:
        assert a.value == ctypes.sizeof(did), "written bytes %d != %d" % (a.value, ctypes.sizeof(did))

        return did
    else:
        raise CUPTIError(r)

# CUptiResult cuptiEnumEventDomains ( size_t* arraySizeBytes, CUpti_EventDomainID* domainArray ) 
_cuptiEnumEventDomains = cupti["cuptiEnumEventDomains"]
_cuptiEnumEventDomains.restype = CUptiResult
_cuptiEnumEventDomains.argtypes = [ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(CUpti_EventDomainID)]

def cuptiEnumEventDomains(ndomains):
    a = ctypes.c_size_t(ndomains * ctypes.sizeof(CUpti_EventDomainID))
    did = (CUpti_EventDomainID * ndomains)()
    
    r = _cuptiEnumEventDomains(a, did)

    if r == CUPTI_SUCCESS:
        assert a.value == ctypes.sizeof(did), "written bytes %d != %d" % (a.value, ctypes.sizeof(did))
        return did
    else:
        raise CUPTIError(r)

# CUptiResult cuptiEventDomainEnumEvents ( CUpti_EventDomainID eventDomain, size_t* arraySizeBytes, CUpti_EventID* eventArray ) 
_cuptiEventDomainEnumEvents = cupti["cuptiEventDomainEnumEvents"]
_cuptiEventDomainEnumEvents.restype = CUptiResult
_cuptiEventDomainEnumEvents.argtypes = [CUpti_EventDomainID, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(CUpti_EventID)]

def cuptiEventDomainEnumEvents(eventDomain, nevents):
    a = ctypes.c_size_t(nevents * ctypes.sizeof(CUpti_EventID))
    eid = (CUpti_EventID * nevents)()
    
    r = _cuptiEventDomainEnumEvents(eventDomain, a, eid)

    if r == CUPTI_SUCCESS:
        assert a.value == ctypes.sizeof(eid), "written bytes %d != %d" % (a.value, ctypes.sizeof(eid))
        return eid
    else:
        raise CUPTIError(r)


# CUptiResult cuptiEventDomainGetAttribute ( CUpti_EventDomainID eventDomain, CUpti_EventDomainAttribute attrib, size_t* valueSize, void* value ) 
_cuptiEventDomainGetAttribute = cupti["cuptiEventDomainGetAttribute"]
_cuptiEventDomainGetAttribute.restype = CUptiResult
_cuptiEventDomainGetAttribute.argtypes = [CUpti_EventDomainID, CUpti_EventDomainAttribute, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p]

def cuptiEventDomainGetAttribute(eventDomain, attrib):
    uint32_attr = set([CUPTI_EVENT_DOMAIN_ATTR_INSTANCE_COUNT, CUPTI_EVENT_DOMAIN_ATTR_TOTAL_INSTANCE_COUNT])
    const_cstr_attr = set([CUPTI_EVENT_DOMAIN_ATTR_NAME])
    int_attr = set([CUPTI_EVENT_DOMAIN_ATTR_COLLECTION_METHOD])

    if attrib in uint32_attr:
        value = ctypes.c_uint32()
    elif attrib in int_attr:
        value = ctypes.c_int()
    elif attrib in const_cstr_attr:
        value = ctypes.create_string_buffer(512)
    else:
        assert False, "Unknown attribute type"

    sz = ctypes.c_size_t(ctypes.sizeof(value))
    r = _cuptiEventDomainGetAttribute(eventDomain, attrib, sz, value)

    if r != CUPTI_SUCCESS:
        raise CUPTIError(r)
    else:
        if attrib in uint32_attr:
            return value.value
        elif attrib in int_attr:
            return value.value
        elif attrib in const_cstr_attr:
            if sz.value == len(value):
                # no null byte
                return value[:sz.value]
            else:
                # discard null byte
                return value[:sz.value-1]


# CUptiResult cuptiEventGetIdFromName ( CUdevice device, const char* eventName, CUpti_EventID* event ) 
_cuptiEventGetIdFromName = cupti["cuptiEventGetIdFromName"]
_cuptiEventGetIdFromName.restype = CUptiResult
_cuptiEventGetIdFromName.argtypes = [CUdevice, ctypes.c_char_p, ctypes.POINTER(CUpti_EventID)]

def cuptiEventGetIdFromName(device, eventName):
    evId = CUpti_EventID()

    r = _cuptiEventGetIdFromName(device, eventName, evId)

    if r == CUPTI_ERROR_INVALID_EVENT_NAME:
        return None
    elif r == CUPTI_SUCCESS:
        return evId.value
    else:
        raise CUPTIError(r)

def cuptiHelperGetAllEvents(d):
    domains = cuptiDeviceGetNumEventDomains(d)
    dids = cuptiDeviceEnumDomains(d, domains)

    out = {}
    for did in dids:
        nevents = cuptiEventDomainGetNumEvents(did)
        eids = cuptiEventDomainEnumEvents(did, nevents)
        out[did] = [x for x in eids]

    return out

# CUptiResult cuptiEventGetAttribute ( CUpti_EventID event, CUpti_EventAttribute attrib, size_t* valueSize, void* value ) 
_cuptiEventGetAttribute = cupti["cuptiEventGetAttribute"]
_cuptiEventGetAttribute.restype = CUptiResult
_cuptiEventGetAttribute.argtypes = [CUpti_EventID, CUpti_EventAttribute, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p]

def cuptiEventGetAttribute(event, attrib, strsize = 512):
    const_cstr_attr = set([CUPTI_EVENT_ATTR_NAME, CUPTI_EVENT_ATTR_LONG_DESCRIPTION, CUPTI_EVENT_ATTR_SHORT_DESCRIPTION])
    int_attr = set([CUPTI_EVENT_ATTR_CATEGORY])

    if attrib in int_attr:
        value = ctypes.c_int()
        arg_value = ctypes.byref(value)
    elif attrib in const_cstr_attr:
        value = ctypes.create_string_buffer(strsize)
        arg_value = value
    else:
        assert False, "Unknown attribute type"

    sz = ctypes.c_size_t(ctypes.sizeof(value))
    r = _cuptiEventGetAttribute(event, attrib, sz, arg_value)

    if r != CUPTI_SUCCESS:
        raise CUPTIError(r)
    else:
        if attrib in int_attr:
            return value.value
        elif attrib in const_cstr_attr:
            if sz.value == len(value):
                # no null byte
                return value[:sz.value]
            else:
                assert sz.value > 0
                if ord(value[sz.value - 1]) == 0:
                    # discard null byte
                    return value[:sz.value-1]
                else:
                    # buggy, CUPTI not counting null byte
                    return value[:sz.value]

# CUptiResult cuptiDeviceGetAttribute ( CUdevice device, CUpti_DeviceAttribute attrib, size_t* valueSize, void* value ) 
_cuptiDeviceGetAttribute = cupti['cuptiDeviceGetAttribute']
_cuptiDeviceGetAttribute.restype = CUptiResult
_cuptiDeviceGetAttribute.argtypes = [CUdevice, CUpti_DeviceAttribute, 
                                     ctypes.POINTER(ctypes.c_size_t),
                                     ctypes.c_void_p]

def cuptiDeviceGetAttribute(device, attrib):
    uint32_attr = set([CUPTI_DEVICE_ATTR_MAX_EVENT_ID,
                       CUPTI_DEVICE_ATTR_MAX_EVENT_DOMAIN_ID,
                       CUPTI_DEVICE_ATTR_INSTRUCTION_PER_CYCLE,
                       CUPTI_DEVICE_ATTR_NVLINK_PRESENT,
                       ])
                       
    uint64_attr = set([CUPTI_DEVICE_ATTR_GLOBAL_MEMORY_BANDWIDTH,
                       CUPTI_DEVICE_ATTR_INSTRUCTION_THROUGHPUT_SINGLE_PRECISION,
                       CUPTI_DEVICE_ATTR_MAX_FRAME_BUFFERS,
                       CUPTI_DEVICE_ATTR_PCIE_LINK_RATE,
                       CUPTI_DEVICE_ATTR_PCIE_LINK_WIDTH,
                       CUPTI_DEVICE_ATTR_PCIE_GEN,
                       CUPTI_DEVICE_ATTR_FLOP_SP_PER_CYCLE,
                       CUPTI_DEVICE_ATTR_FLOP_DP_PER_CYCLE,
                       CUPTI_DEVICE_ATTR_MAX_L2_UNITS,
                       CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_SHARED,
                       CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_L1,
                       CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_EQUAL,
                       CUPTI_DEVICE_ATTR_FLOP_HP_PER_CYCLE,
                       CUPTI_DEVICE_ATTR_GPU_CPU_NVLINK_BW,
                   ])
    
    if attrib in uint32_attr:
        arg1 = ctypes.c_uint32(0)
        sz = ctypes.c_size_t(ctypes.sizeof(ctypes.c_uint32))

        r = _cuptiDeviceGetAttribute(device, attrib, sz, ctypes.byref(arg1))
        
        if r != CUPTI_SUCCESS:
            raise CUPTIError(r)
        else:
            if sz.value == ctypes.sizeof(ctypes.c_uint32):
                return arg1.value
            else:                
                # not of type c_uint32!
                assert False, sz.value
    elif attrib in uint64_attr:
        arg1 = ctypes.c_uint64(0)
        sz = ctypes.c_size_t(ctypes.sizeof(ctypes.c_uint64))

        r = _cuptiDeviceGetAttribute(device, attrib, sz, ctypes.byref(arg1))
        
        if r != CUPTI_SUCCESS:
            raise CUPTIError(r)
        else:
            if sz.value == ctypes.sizeof(ctypes.c_uint64):
                return arg1.value
            else:                
                # not of type c_uint32!
                assert False, sz.value       
    else:
        raise NotImplementedError
    
    
