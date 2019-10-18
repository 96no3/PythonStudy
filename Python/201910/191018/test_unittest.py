import unittest

class Test(unittest.TestCase):
    def test(self):
        v=2+4
        print("result",v)

        # 結果を検証
        self.assertEqual(v,6,"計算")
