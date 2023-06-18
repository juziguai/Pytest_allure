# parameter_dict.py
"""
Created by: juzi
Created time: 2023/6/5 1:17 
Purpose:
"""


class parameter_dict(object):
    # 定义一个私有字典
    _parameter_dict = {}

    # 向字典添加数据
    def set_parameter(self, key, value):
        self._parameter_dict[key] = value

    # 展示字典所有数据
    def show_parameter(self):
        return self._parameter_dict
