# —*- coding:utf-8 -*-
import pytest
from conftest import auto_parametrize_yml

class TestBaiDu:
    @pytest.auto_parametrize_yml()
    def test_search_success(self,key):
        '''注意对应的 yaml文件 里面的值必须是  search_success，看这个case名称和yml名称你就明白咋回事了，约定大于配置 '''
        print(f'搜索关键字为{key}')

if __name__ == '__main__':
    pytest.main(['-vs',__file__],plugins=[auto_parametrize_yml])
    # 命令行运行 pytest -vs case/test_baidu.py  
