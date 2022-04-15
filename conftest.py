# —*- coding:utf-8 -*-
from until.get_yml import auto_get_yml_data
import pytest
import sys
from os.path import abspath, dirname
package_path = abspath((dirname(__file__)))
sys.path.insert(0, package_path)


def auto_parametrize_yml(*args, **kwargs):
    """
    @summary： 根据被测的函数和文件名,自动找对应的yaml测试数据
    :param args:
    :param kwargs:
    :return:
    """
    def decorator(func):
        yml_data=auto_get_yml_data(package_path,func.__name__.replace('test_',''))
        print('test data is automatic get ',yml_data)
        return pytest.mark.parametrize(**yml_data)(func)
    return decorator

pytest.auto_parametrize_yml=auto_parametrize_yml  #注册插件