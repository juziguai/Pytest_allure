"""
for 变量名 in 可迭代对象：
    # 操作语句块
"""
import ast

import jsonpath

# extract_parameters = '"token","code"'
extract_parameters = '"name","id"'
# print(len(extract_parameters))
# print(type(extract_parameters))
# extract_parameters = '"id"'
# extract_parameters = 'id'
extract_parameters = extract_parameters.strip()
# print(extract_parameters, new_parameters)
# print(len(extract_parameters), len(new_parameters))

json_data = {
    "msg": "success",
    "code": 0,
    "data": {
        "data": [
            {
                "id": "18720",
                "alias": "单位",
                "name": "张小花",
                "tel": "13456987465",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "小小花",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "1",
                "idcard_name": "小花",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18719",
                "alias": "单位",
                "name": "张小花",
                "tel": "13456987465",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "小小花",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "小花",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18718",
                "alias": "单位",
                "name": "张小花",
                "tel": "13456987465",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "小小花",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "小花",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18717",
                "alias": "单位",
                "name": "张小花",
                "tel": "13456987465",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "小小花",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "小花",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18715",
                "alias": "单位",
                "name": "龚哥哥",
                "tel": "13222223333",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "浦江科技⼴场",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "龚哥哥姓名",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18714",
                "alias": "单位",
                "name": "龚哥哥",
                "tel": "13222223333",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "浦江科技⼴场",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "龚哥哥姓名",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18713",
                "alias": "单位",
                "name": "龚哥哥",
                "tel": "13222223333",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "浦江科技⼴场",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "龚哥哥姓名",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18712",
                "alias": "单位",
                "name": "龚哥哥",
                "tel": "13222223333",
                "province": "9",
                "city": "152",
                "county": "1896",
                "address": "浦江科技⼴场",
                "lng": "121.3886718906",
                "lat": "31.1188928641",
                "is_default": "0",
                "idcard_name": "龚哥哥姓名",
                "idcard_number": "522228666655556666",
                "idcard_front": "https://xxx/1633946357974689.png",
                "idcard_back": "https://xxx/1633946364142699.png",
                "province_name": "上海市",
                "city_name": "闵行区",
                "county_name": "浦江镇",
                "idcard_front_old": "https://xxx/1633946357974689.png",
                "idcard_back_old": "https://xxx/1633946364142699.png"
            },
            {
                "id": "18184",
                "alias": "123",
                "name": "213",
                "tel": "123213213213213",
                "province": "1",
                "city": "38",
                "county": "578",
                "address": "213213213213",
                "lng": "0.0000000000",
                "lat": "0.0000000000",
                "is_default": "0",
                "idcard_name": "",
                "idcard_number": "",
                "idcard_front": "",
                "idcard_back": "",
                "province_name": "北京市",
                "city_name": "西城区",
                "county_name": "展览路街道",
                "idcard_front_old": "",
                "idcard_back_old": ""
            }
        ]
    }
}

aa_dict = {}
# if extract_parameters is None or extract_parameters == "":
#     print("没有获取到值")
# else:
#     print("获取到值啦")
#     extract_parameters = ast.literal_eval(extract_parameters)
#     print(extract_parameters)

if extract_parameters != '' and extract_parameters != "" or len(extract_parameters) != 0:
    if "," in extract_parameters:
        extract_parameters = ast.literal_eval(extract_parameters)
        for i in extract_parameters:
            response_parameters_data = jsonpath.jsonpath(json_data, "$.." + i)
            print(response_parameters_data, i)
            # 循环保存需要的参数数据到字典
            aa_dict.update({i: response_parameters_data[0]})
            print(aa_dict)
    else:
        print("单个参数！")
        extract_parameters = ast.literal_eval(extract_parameters)
        response_parameters_data = jsonpath.jsonpath(json_data, "$.." + extract_parameters)
        print(extract_parameters, response_parameters_data)
        # 循环保存需要的参数数据到字典
        aa_dict.update({extract_parameters: response_parameters_data[0]})
        print(aa_dict)

# elif "," not in extract_parameters:
#     print("单个参数")
#     extract_parameterss = ast.literal_eval(extract_parameters)
#     # extract_parameterss = extract_parameters
#     response_parameters_data = jsonpath.jsonpath(json_data, "$.." + extract_parameterss)
#     print(extract_parameterss, response_parameters_data)
#     # 循环保存需要的参数数据到字典
#     aa_dict.update({extract_parameterss: response_parameters_data[0]})
#     print(aa_dict)
else:
    print("提取参数为空，不做相关提取操作")
