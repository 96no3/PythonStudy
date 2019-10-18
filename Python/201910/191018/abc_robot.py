from abc import ABCMeta, abstractmethod

# 抽象基底クラスの定義
class MazeRobot(metaclass=ABCMeta):

    @abstractmethod
    def init_robot(self):
        pass

    @abstractmethod
    def choose_dir(self):
        pass
