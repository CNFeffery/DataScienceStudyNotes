import dill.source
from dill import dumps, loads

def demo_func(a, b):
    
    return a * b

# 生成序列化结果
demo_func_dump = dill.dumps(demo_func)

print('demo_func的源码提取结果：')
print(dill.source.getsource(loads(demo_func_dump)))