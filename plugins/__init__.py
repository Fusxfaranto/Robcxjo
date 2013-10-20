import os, __builtin__

plugin_list = __builtin__.set()

for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
    plugin_list.add(module[:-3])
del module