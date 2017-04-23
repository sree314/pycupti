CUPTI_SUCCESS = 0
CUPTI_ERROR_INVALID_EVENT_NAME = 6

CUPTI_METRIC_ATTR_NAME = 0 #   Metric name. Value is a null terminated const c-string. 
CUPTI_METRIC_ATTR_SHORT_DESCRIPTION = 1 #    Short description of metric. Value is a null terminated const c-string. 
CUPTI_METRIC_ATTR_LONG_DESCRIPTION = 2 #    Long description of metric. Value is a null terminated const c-string. 
CUPTI_METRIC_ATTR_CATEGORY = 3 #    Category of the metric. Value is of type CUpti_MetricCategory. 
CUPTI_METRIC_ATTR_VALUE_KIND = 4 #     Value type of the metric. Value is of type CUpti_MetricValueKind. 
CUPTI_METRIC_ATTR_EVALUATION_MODE = 5 #     Metric evaluation mode. Value is of type CUpti_MetricEvaluationMode. 

CUPTI_METRIC_CATEGORY_MEMORY = 0 #    A memory related metric. 
CUPTI_METRIC_CATEGORY_INSTRUCTION = 1 #    An instruction related metric. 
CUPTI_METRIC_CATEGORY_MULTIPROCESSOR = 2 #    A multiprocessor related metric. 
CUPTI_METRIC_CATEGORY_CACHE = 3 #    A cache related metric. 
CUPTI_METRIC_CATEGORY_TEXTURE = 4 #    A texture related metric. 


CUPTI_METRIC_VALUE_KIND_DOUBLE = 0 #    The metric value is a 64-bit double. 
CUPTI_METRIC_VALUE_KIND_UINT64 = 1 #    The metric value is a 64-bit unsigned integer. 
CUPTI_METRIC_VALUE_KIND_PERCENT = 2 #    The metric value is a percentage represented by a 64-bit double. For example, 57.5% is represented by the value 57.5.  
CUPTI_METRIC_VALUE_KIND_THROUGHPUT = 3 #     The metric value is a throughput represented by a 64-bit integer. The unit for throughput values is bytes/second.  
CUPTI_METRIC_VALUE_KIND_INT64 = 4 #     The metric value is a 64-bit signed integer. 
CUPTI_METRIC_VALUE_KIND_UTILIZATION_LEVEL = 5 #    The metric value is a utilization level, as represented by CUpti_MetricValueUtilizationLevel. 

CUPTI_METRIC_EVALUATION_MODE_PER_INSTANCE = 1 #If this bit is set, the metric can be profiled for each instance of the domain. The event values passed to cuptiMetricGetValue can contain values for one instance of the domain. And cuptiMetricGetValue can be called for each instance. 
CUPTI_METRIC_EVALUATION_MODE_AGGREGATE = 1<<1 

CUPTI_DEVICE_ATTR_MAX_EVENT_ID = 1
#    Number of event IDs for a device. Value is a uint32_t. 
CUPTI_DEVICE_ATTR_MAX_EVENT_DOMAIN_ID = 2
#    Number of event domain IDs for a device. Value is a uint32_t. 
CUPTI_DEVICE_ATTR_GLOBAL_MEMORY_BANDWIDTH = 3
#    Get global memory bandwidth in Kbytes/sec. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_INSTRUCTION_PER_CYCLE = 4
#    Get theoretical maximum number of instructions per cycle. Value is a uint32_t. 
CUPTI_DEVICE_ATTR_INSTRUCTION_THROUGHPUT_SINGLE_PRECISION = 5
#    Get theoretical maximum number of single precision instructions that can be executed per second. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_MAX_FRAME_BUFFERS = 6
#    Get number of frame buffers for device. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_PCIE_LINK_RATE = 7
#    Get PCIE link rate in Mega bits/sec for device. Return 0 if bus-type is non-PCIE. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_PCIE_LINK_WIDTH = 8
#    Get PCIE link width for device. Return 0 if bus-type is non-PCIE. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_PCIE_GEN = 9
#    Get PCIE generation for device. Return 0 if bus-type is non-PCIE. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_DEVICE_CLASS = 10
#    Get the class for the device. Value is a CUpti_DeviceAttributeDeviceClass. 
CUPTI_DEVICE_ATTR_FLOP_SP_PER_CYCLE = 11
#    Get the peak single precision flop per cycle. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_FLOP_DP_PER_CYCLE = 12
#    Get the peak double precision flop per cycle. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_MAX_L2_UNITS = 13
#    Get number of L2 units. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_SHARED = 14
#    Get the maximum shared memory for the CU_FUNC_CACHE_PREFER_SHARED preference. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_L1 = 15
#    Get the maximum shared memory for the CU_FUNC_CACHE_PREFER_L1 preference. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_MAX_SHARED_MEMORY_CACHE_CONFIG_PREFER_EQUAL = 16
#    Get the maximum shared memory for the CU_FUNC_CACHE_PREFER_EQUAL preference. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_FLOP_HP_PER_CYCLE = 17
#    Get the peak half precision flop per cycle. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_NVLINK_PRESENT = 18
#    Check if Nvlink is connected to device. Returns 1, if at least one Nvlink is connected to the device, returns 0 otherwise. Value is a uint32_t. 
CUPTI_DEVICE_ATTR_GPU_CPU_NVLINK_BW = 19
#    Check if Nvlink is present between GPU and CPU. Returns Bandwidth, in Bytes/sec, if Nvlink is present, returns 0 otherwise. Value is a uint64_t. 
CUPTI_DEVICE_ATTR_FORCE_INT = 0x7fffffff


CUPTI_EVENT_ATTR_NAME = 0
#    Event name. Value is a null terminated const c-string. 
CUPTI_EVENT_ATTR_SHORT_DESCRIPTION = 1
#    Short description of event. Value is a null terminated const c-string. 
CUPTI_EVENT_ATTR_LONG_DESCRIPTION = 2
#    Long description of event. Value is a null terminated const c-string. 
CUPTI_EVENT_ATTR_CATEGORY = 3
#    Category of event. Value is CUpti_EventCategory. 
CUPTI_EVENT_ATTR_FORCE_INT = 0x7fffffff

CUPTI_EVENT_CATEGORY_INSTRUCTION = 0
#    An instruction related event. 
CUPTI_EVENT_CATEGORY_MEMORY = 1
#    A memory related event. 
CUPTI_EVENT_CATEGORY_CACHE = 2
#    A cache related event. 
CUPTI_EVENT_CATEGORY_PROFILE_TRIGGER = 3
#    A profile-trigger event. 
CUPTI_EVENT_CATEGORY_FORCE_INT = 0x7fffffff

CUPTI_EVENT_COLLECTION_METHOD_PM = 0
#    Event is collected using a hardware global performance monitor. 
CUPTI_EVENT_COLLECTION_METHOD_SM = 1
#    Event is collected using a hardware SM performance monitor. 
CUPTI_EVENT_COLLECTION_METHOD_INSTRUMENTED = 2
#    Event is collected using software instrumentation. 
CUPTI_EVENT_COLLECTION_METHOD_NVLINK_TC = 3
#    Event is collected using NvLink throughput counter method. 
CUPTI_EVENT_COLLECTION_METHOD_FORCE_INT = 0x7fffffff

CUPTI_EVENT_DOMAIN_ATTR_NAME = 0
#    Event domain name. Value is a null terminated const c-string. 
CUPTI_EVENT_DOMAIN_ATTR_INSTANCE_COUNT = 1
#    Number of instances of the domain for which event counts will be collected. The domain may have additional instances that cannot be profiled (see CUPTI_EVENT_DOMAIN_ATTR_TOTAL_INSTANCE_COUNT). Can be read only with cuptiDeviceGetEventDomainAttribute. Value is a uint32_t. 
CUPTI_EVENT_DOMAIN_ATTR_TOTAL_INSTANCE_COUNT = 3
#    Total number of instances of the domain, including instances that cannot be profiled. Use CUPTI_EVENT_DOMAIN_ATTR_INSTANCE_COUNT to get the number of instances that can be profiled. Can be read only with cuptiDeviceGetEventDomainAttribute. Value is a uint32_t. 
CUPTI_EVENT_DOMAIN_ATTR_COLLECTION_METHOD = 4
#    Collection method used for events contained in the event domain. Value is a CUpti_EventCollectionMethod. 
CUPTI_EVENT_DOMAIN_ATTR_FORCE_INT = 0x7fffffff


