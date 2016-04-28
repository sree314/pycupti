CUPTI_SUCCESS = 0

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
