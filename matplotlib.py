##安装matplotlib
 #找到pip工具的路径（python -m pip --version）
 #更新pip（python -m pip install --upgrade pip）
 #下载matplotlib文件whl格式文件，放在pip文件的目录下
 #在pip路径下，安装 （pip install -u matplotlib-2.2.3-cp37-cp37m-win_amd64.whl）

 #测试
from matplotlib import pyplot
pyplot.plot([1, 2, 3, 4], [1, 2, 3, 4])
pyplot.show()

