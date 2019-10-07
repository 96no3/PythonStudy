import math

class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)

class Calculator(Stack):
    def __init__(self,*xs):
        super().__init__()
        self._floating_point = 5
        self.op_dic = {}
        self._op_table = [ ("+",2,lambda a,b:a+b),
                      ("-",2,lambda a,b:a-b),
                      ("*",2,lambda a,b:a*b),
                      ("/",2,lambda a,b:a/b),
                      ("%",2,lambda a,b:a%b),
                      ("//",2,lambda a,b:a//b),
                      ("**",2,lambda a,b:a**b),
                      ("root",1,math.sqrt),
                      ("log",1,math.log),
                      ("sin",1,lambda a:math.sin(math.radians(a))),
                      ("cos",1,lambda a:math.con(math.radians(a))),
                      ("tan",1,lambda a:math.tan(math.radians(a))),
                      ("if",3,lambda a,b,c: b if a else c),
                      ("ceil",1,math.ceil),
                      ("floor",1,math.floor)]
        self._op_table.extend(xs)

    @staticmethod
    def err(message=""):
        raise ValueError(message)

    def generate(self,n,f):
        """<高階関数かつクロージャ>
           要素数分スタックからpopして関数を適用しスタックにpushする
           @param n 要素数
           @param f 数式関数オブジェクト
           @return proc 適用処理関数"""
        def proc():
            args = [float(self.pop()) for _ in range(n)]
            args.reverse()
            tmp = f(*args)
            self.push(round(tmp,self._floating_point))
        return proc

    def set_operator_dict(self):                
        self.op_dic = dict([(name,self.generate(n,f)) for name,n,f in self._op_table])
        del self._op_table

    def calc(self,xs):
        print(xs,self._stack)
        if not xs:
            if self.depth() == 1:
                return self.pop()
            else:
                Calculator.err("スタックに値が残っています！")
                
        self.operate(xs[0])
        return self.calc(xs[1:])

    def operate(self,x):
        if x in self.op_dic:
            self.op_dic[x]()
        elif Calculator.validate_num(x):
            self.push(x)
        else:
            Calculator.err(f"unknown operator: {x}")

    @staticmethod
    def input_num_expression():
        """入力を求める関数"""
        return input("後置記法で数式を入力してください:")

    def get_num_expression(self,function):
        """＜高階関数＞入力を求める関数の値を判断する関数
           @param function  入力処理を行う関数
           @return tmp_list 認識可能なlist"""
        while True:
            s = function()
            if s.lower() in {"exit","quit","bye"}:
                break
            try:
                if s == "":
                    Calculator.err()
                tmp_list = s.split(" ")
                tmp_list = list(filter(lambda a:a is not "", tmp_list))                
                self.validate_element(tmp_list)
                return tmp_list
            except:
                print(f"「{s}」は無効な入力値です\n正しい入力値をお願いします")
        return "exit"

    def validate_element(self,xs):
        """<検査関数>有効な要素かどうか検査する関数
           @param xs 入力値の各要素リスト
           @return  各要素リスト"""
        if xs == []:
            return xs
        elif xs[0] in self.op_dic:
            self.validate_element(xs[1:])
        elif Calculator.validate_num(xs[0]):
            self.validate_element(xs[1:])
        else:
            Calculator.err("無効な入力値です")

    @staticmethod
    def validate_num(s):
        """<検査関数>有効な数値かどうか検査する関数
           @param s 文字列
           @return  有効な数値の文字列"""
        if s[0] == "-":
            Calculator.validate_num(s[1:])
        elif s[0] == "+":
            Calculator.validate_num(s[1:])
        elif s.count(".") == 1:
            [a,b] = s.split(".")
            if not a.isdigit() or not b.isdigit():
                Calculator.err()
            return True
        elif not s.isdigit():
            Calculator.err()
        return True

    def test_exec(self):
        self.set_operator_dict()        
        while True:
            num_expression = self.get_num_expression(Calculator.input_num_expression)
            if num_expression == "exit":
                return False            
            try:
                print("\n計算結果>",self.calc(num_expression),"\n")
            except:
                print(f"「{num_expression}」は計算不可能な式です")
                print("正しい入力値をお願いします")
                self.clear()
            
def test():
    calc = Calculator(("r",1,math.sqrt),("s",1,math.sin))
    while calc.test_exec():
        pass
    print("end")

# 実行部分
test()
