from abc_robot import MazeRobot

class MazeRobotTest(MazeRobot):
    # 抽象基底クラスの継承で@abstractmethodは必ずオーバーライドが必要
    def init_robot(self):
        print("ロボットを初期化します")

    #def choose_dir(self):
    #    print("前進します")

robot=MazeRobotTest()
robot.init_robot()
