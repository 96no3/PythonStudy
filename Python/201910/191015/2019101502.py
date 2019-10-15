# スプリクトのパスを得る方法
import os

print("script path=",__file__)
print("script dir=",os.path.dirname(__file__))
print("script abspath=",os.path.abspath(__file__))
print("script basename=",os.path.basename(__file__))
print("script exists=",os.path.exists(__file__))
print("script isfile=",os.path.isfile(__file__))
print("script isdir=",os.path.isdir(
    "C:/Users/pcuser/source/repos/Github/PythonStudy/Python/201910/191015"))
