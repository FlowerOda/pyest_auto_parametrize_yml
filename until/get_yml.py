# —*- coding:utf-8 -*-
import inspect
import os
import yaml



def auto_get_yml_data(package_path,name) :
    """
    :param name: 用例名称
    :return: yml对象
    """
    filepath=os.path.join(package_path,f"data\{os.path.basename(inspect.stack()[2][1]).split('.')[0]}_data.yml")

    print('yaml data path automatic get ',filepath)
    with open(filepath, encoding='utf-8') as f:
        return yaml.safe_load(f)[name]