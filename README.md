# DeepCube功能接口

## 指标字典

### 查询指标信息 

#### query_metrics

1. 支持根据指标名列表查询多个指标的指标信息。
   
请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| name_list        | 指标名列表                  | 是           | Array(Object)       |
| &emsp;&emsp;name|指标名|是|string|
| &emsp;&emsp;domain|数据域|否|string|
| &emsp;&emsp;model|数据模型|否|string|
| Authorization | Authorization放在header中 | 是           | String       |


```
{
    "name_list": [
        {
            "name":"event_count",
            "domain": "质量域",
            "model": "异常监控",
        },
        {
            "name": "acc_event_avg_speed",
        },
        ...
    ]
}
```

2. 支持根据指标id列表查询多个指标的指标信息。
   
请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| id_list        | 指标id列表                  | 是           | Array(Object)       |
| &emsp;&emsp;name|id|是|string|
| Authorization | Authorization放在header中 | 是           | String       |


```
{
    "id_list": [
        {
            "id":"adsfafs1123213",
        },
        {
            "id": "adsfafdsa3321312",
        },
        ...
    ]
}
```

返回格式：

| 参数名称         | 参数说明            | 类型     | schema         |
| ----------| --------------| ---------------- | ------------------- |
|id| 指标index| str| str|
|name|指标名|str|str|
|display_name|显示名称|str|str|
|description|说明|str|str|
|dimensions|维度|array|object|
|&emsp;&emsp;id| 维度index| str| str|
|&emsp;&emsp;name|维度名|str|str|
|&emsp;&emsp;display_name|显示名称|str|str|
|&emsp;&emsp;description|说明|str|str|
|&emsp;&emsp;type|维度类型，如：Categorical，Numerical, Timestamp等|str|str|
|&emsp;&emsp;value_list|Categorical类型维度的取值列表，其他类型为空|array|str|
|filter_contidion|过滤条件|str|str|
|domain|数据域|str|str|
|model|数据模型|str|str|


```json
# 返回格式
{
    "code": 0,
    "msg": "",
    "result": [
        {
            "id": "asdfasf",
            "name": "event_count",
            "display_name": "事件数",
            "description": "异常事件数",
            "dimensions": [
                {
                    "id": "asdfasf",
                    "name": "event_level",
                    "display_name": "事件等级",
                    "description": "异常事件等级",
                    "type": "Categorical",
                    "value_list": ["1", "2", "3"],
                },
                {...},
                ...
            ],
            "filter_condition": "event_name = 'isc'",
            "domain": "质量域",
            "model": "异常监控"
        },
        {...},
        ...
    ]
}
```

### 维度信息查询 

#### query_dims

1. 支持根据维度名查询维度信息。
   
请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| dim_list        | 维度名列表                  | 是           | Array(Object)       |
| &emsp;&emsp;name|维度名|是|string|
| &emsp;&emsp;domain|数据域|否|string|
| &emsp;&emsp;model|数据模型|否|string|
| Authorization | Authorization放在header中 | 是           | String       |


```
{
    "dim_list": [
        {
            "name":"event_level"，
            "domain":"质量域",
            "model":"异常监控",
        },
        {
            "name": "day_of_year",
        },
        ...
    ]
}
```

2. 支持根据维度id查询多个指标。
   
请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| dim_list        | 维度id列表                  | 是           | Array(Object)       |
| &emsp;&emsp;name|维度id|是|string|
| Authorization | Authorization放在header中 | 是           | String       |


```
{
    "dim_list": [
        {
            "name":"xxxxfaf"，
        },
        {
            "name": "xsdfsfsf",
        },
        ...
    ]
}
```

返回格式：

| 参数名称         | 参数说明            | 类型     | schema         |
| ----------| --------------| ---------------- | ------------------- |
|id| 维度index| str| str|
|name|维度名|str|str|
|display_name|显示名称|str|str|
|description|说明|str|str|
|type|维度类型，如：Categorical，Numerical, Timestamp等|str|str|
|value_list|Categorical类型维度的取值列表，其他类型为空|array|str|
|domain|数据域|str|str|
|model|数据模型|str|str|


```json
# 返回格式
{
    "code": 0,
    "msg": "",
    "result": [
        {
            "id": "asdfasf",
            "name": "event_level",
            "display_name": "事件等级",
            "description": "异常事件等级",
            "type": "Categorical",
            "value_list": ["1", "2", "3"],
            "domain": "质量域",
            "model": "异常监控"
        },
        {...},
        ...
    ]
}
```

### 数据模型信息查询 

#### query_models

1. 支持查询数据域数据模型信息
请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| query_list    | 数据域，数据模型列表        | 是           | Array(Object)       |
| &emsp;&emsp;domain|数据域名称|是|string|
| &emsp;&emsp;model|数据模型名|是|string|
| Authorization | Authorization放在header中 | 是           | String       |


```
{
    "query_list": [
        {
            "domain":"质量域"，
            "model":"异常监控",
        },
        {
            "domain": "自家驾域",
            "model": "功能触发统计",
        },
        ...
    ]
}
```

返回格式：

| 参数名称         | 参数说明            | 类型     | schema         |
| ----------| --------------| ---------------- | ------------------- |
|id| index| str| str|
|domain|数据域名称|str|str|
|model|数据模型名称|str|str|
|description|说明|str|str|


```json
# 返回格式
{
    "code": 0,
    "msg": "",
    "result": [
        {
            "id": "asdfasf",
            "domain": "质量域",
            "model": "异常监控",
            "descripation": "电池系统异常监控汇总",
        },
        {...},
        ...
    ]
}
```

#### list_models

2. 支持列出指定数据域中的所有数据模型

请求格式：

| **参数名**    | **说明**                  | **是否必填** | **数据类型** |
| ------------- | ------------------------- | ------------ | ------------ |
| query_list    | 数据域        | 是           | Array(Object)       |
| &emsp;&emsp;domain|数据域名称|是|string|
| Authorization | Authorization放在header中 | 是           | String       |

```
{
    "query_list": [
        {
            "domain":"质量域"，
        },
        {
            "domain": "自家驾域",
        },
        ...
    ]
}
```

返回格式：
```json
# 返回格式
{
    "code": 0,
    "msg": "",
    "result": [
        {
            "id": "asdfasf",
            "domain": "质量域",
            "description": "质量域功能说明",
            "model_list": [
                {
                    "id": "dfses",
                    "model": "异常监控",
                    "description": "电池系统异常监控汇总",
                },
                {...},
                ...
            ]
        },
        {...},
        ...
    ]
}
```

#### list_all

3. 支持列出所有数据域和数据模型
   
返回格式：
```json
# 返回格式
{
    "code": 0,
    "msg": "",
    "result": [
        {
            "id": "asdfasf",
            "domain": "质量域",
            "description": "质量域功能说明",
            "model_list": [
                {
                    "id": "dfses",
                    "model": "异常监控",
                    "description": "电池系统异常监控汇总",
                },
                {...},
                ...
            ]
        },
        {...},
        ...
    ]
}
```


## 指标数据查询

### 数据查询

#### query_data

1. 根据查询DSL查询指标数据，返回数据表格。

请求格式：

| 参数名称         | 参数说明            | 类型     | schema         |
| ----------| --------------| ---------------- | ------------------- |
|SELECT|指标, 维度|string|string|
|FROM|数据域，数据模型|string|string|
|WHERE|过滤条件|string|string|
|GROUP BY|维度|string|string|
|HAVING|聚合过滤条件|string|string|
|ORDER BY|排序维度|string|string|
|LIMIT|数据条数限制|int|int|


```json
#DSL 请求示例
{
    "SELECT": "event_count, report_date, event_level, event_name",
    "FROM": "质量域.异常监控",
    "WHERE": "event_name = 'isc'",
    "GROUP BY": "report_date, event_level, event_name",
    "HAVING": "sum(event_count)>30",
    "ORDER BY": "report_date",
    "LIMIT": 100
}
```

返回格式：

数据表格返回json格式：

```json
{
    "code": 0,
    "msg": "",
    "result":[
            {"event_count":value, "report_date": value, ...},
            {...},
            ...
        ]
}
```
