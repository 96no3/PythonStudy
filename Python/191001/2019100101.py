import math

class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        try:
            tmp = self._stack.pop()
            return tmp
        except IndexError:
            print("スタックが空です\n")

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack) 

# ノードを構成するデータ構造
class Node(Stack):
    # コンストラクタ(与えられた式expressionを持つノードを構成する)
    def __init__(self, expression):
        super().__init__()
        #Stack.__init__(self)
        self.expression = expression # 式(二分木への分割後は演算子または項)
        self.left = None  # 左の子ノード
        self.right = None # 右の子ノード
        self._floating_point = 5
        self._max_priority = 9
        self.op_dic = {}
        self.op_pri_dic = {}
        self.op_num_dic = {}
        self.set_operator_dict()

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
            #print("debug00:",args)
            tmp = f(*args)
            tmp = round(tmp,self._floating_point)
            #print("debug01:",tmp)
            self.expression = [str(tmp)]
        return proc
    
    def set_operator_dict(self):
        _op_table = ( ("+",1,2,lambda a,b:a+b),
                      ("-",1,2,lambda a,b:a-b),
                      ("*",2,2,lambda a,b:a*b),
                      ("/",2,2,lambda a,b:a/b),
                      ("%",2,2,lambda a,b:a%b),
                      ("//",2,2,lambda a,b:a//b),
                      ("**",3,2,lambda a,b:a**b),
                      ("root",4,1,math.sqrt),
                      ("log",4,1,math.log),
                      ("sin",4,1,lambda a:math.sin(math.radians(a))),
                      ("cos",4,1,lambda a:math.con(math.radians(a))),
                      ("tan",4,1,lambda a:math.tan(math.radians(a))),
                      ("ceil",4,1,math.ceil),
                      ("floor",4,1,math.floor),
                      ("(",5,0,None),
                      (")",5,0,None) )
        
        self.op_pri_dic = dict([(name,pri) for name,pri,n,f in _op_table])
        self.op_num_dic = dict([(name,n) for name,pri,n,f in _op_table])
        self.op_dic = dict([(name,self.generate(n,f)) for name,pri,n,f in _op_table])
        del _op_table

    @staticmethod
    def validate_bracket_balance(expression):
        """<検証メソッド>式expression内の括弧の対応を確認する
         @param expression 式
         @raise 開き括弧と閉じ括弧が同数でない場合はエラー"""
        nest = 0 # 丸括弧の深度(くくられる括弧の数を計上するために用いる)
        for i in expression:
            if i == "(":
                nest += 1
            elif i == ")":
                nest -= 1
                # 最後の文字以外で閉じ丸括弧が現れた場合、最も外側には丸括弧がないと判断する
                if nest < 0:
                    break
        if nest != 0:
            # 式中に開かれていない/閉じられていない括弧があるので、エラーとする
            raise Exception("unbalanced bracket: {}".format(expression))

    def parse(self):
        """中置記法の式expressionを二分木へと分割するメソッド"""
        # 式expressionから最も外側にある丸括弧を取り除く
        self.expression = Node.__remove_outer_most_bracket(self.expression)
        # 式expressionから演算子を探して位置を取得する
        pos_operator = self.get_operator_position(self.expression)

        if pos_operator < 0:
            # 式expressionに演算子が含まれない場合、expressionは項であるとみなす
            # (左右に子ノードを持たないノードとする)
            self.left = None
            self.right = None
            return

        if pos_operator == 0:
            self.parse_preorder()
            return
        elif self.expression[-1] in self.op_dic:
            if self.expression[-1] == ")":
                pass
            else:
                self.parse_postorder()
                return           

        # 演算子の左側を左の部分式としてノードを作成する
        self.left = Node(self.expression[:pos_operator])
        # 左側のノード(部分式)について、再帰的に二分木へと分割する        
        self.left.parse()

        # 演算子の右側を右の部分式としてノードを作成する
        self.right = Node(self.expression[pos_operator + 1:])
        # 右側のノード(部分式)について、再帰的に二分木へと分割する        
        self.right.parse()

        # 残った演算子部分をこのノードに設定する        
        self.expression = [self.expression[pos_operator]]

    def parse_preorder(self):
        # 式expressionから最も外側にある丸括弧を取り除く
        self.expression = Node.__remove_outer_most_bracket(self.expression)        

    def parse_postorder(self):
        #print(self.expression,self._stack)
        if len(self.expression) == 1:
            self.operate_final(self.expression[0])
            if self.depth() == 1:
                self.clear()
                return
            else:
                Node.err("スタックに値が残っています")
        self.operate(self.expression[0])
        del self.expression[0]
        return self.parse_postorder()

    def operate(self,x):
        if x in self.op_num_dic:
            if self.op_num_dic[x] == 2:
                tmp_right = self.pop()
                tmp_left = self.pop()
                tmp_expression = [x]
                tmp = Node(tmp_expression)
                if isinstance(tmp_right,Node):
                    tmp.right = tmp_right
                else:
                    tmp.right = Node([tmp_right])
                if isinstance(tmp_left,Node):
                    tmp.left = tmp_left
                else:
                    tmp.left = Node([tmp_left])
                self.push(tmp)
            else: # self.op_num_dic[x] == 1
                tmp_right = self.pop()
                tmp_expression = [x]
                tmp = Node(tmp_expression)
                if isinstance(tmp_right,Node):
                    tmp.right = tmp_right
                else:
                    tmp.right = Node([tmp_right])               
                self.push(tmp)
            
        elif Node.validate_num(x):
            self.push(x)
        else:
            Node.err(f"unknown operator: {x}")

    def operate_final(self,x):
        if x in self.op_num_dic:
            if self.op_num_dic[x] == 2:
                tmp_right = self.pop()
                tmp_left = self.pop()
                if isinstance(tmp_right,Node):
                    self.right = tmp_right
                else:
                    self.right = Node([tmp_right])
                if isinstance(tmp_left,Node):
                    self.left = tmp_left
                else:
                    self.left = Node([tmp_left])
                self.expression = [x]                
                self.push(self)
            else: # self.op_num_dic[x] == 1
                tmp_right = self.pop()
                if isinstance(tmp_right,Node):
                    self.right = tmp_right
                else:
                    self.right = Node([tmp_right])
                self.expression = [x]
                self.push(self)
            
        elif Node.validate_num(x):
            self.expression = [x]
            self.push(x)            
        else:
            Node.err(f"unknown operator: {x}")
            
    @staticmethod
    def __remove_outer_most_bracket(expression):
        """式expressionから最も外側にある丸括弧を取り除いて返すメソッド"""
        has_outer_most_bracket = False # 最も外側に括弧を持つかどうか
        nest = 0 # 丸括弧の深度(式中で開かれた括弧が閉じられたかどうか調べるために用いる)

        if expression[0] == "(":
            # 0文字目が開き丸括弧の場合、最も外側に丸括弧があると仮定する
            has_outer_most_bracket = True
            nest = 1
            
        for i in range(1, len(expression)):
            if expression[i] == "(":
                nest += 1
                # 0文字目が開き丸括弧の場合、最も外側に丸括弧があると仮定する
                if i == 0:
                    has_outer_most_bracket = True

            elif expression[i] == ")":
                nest -= 1
                # 最後の文字以外で開き丸括弧がすべて閉じられた場合、最も外側には丸括弧がないと判断する
                if nest == 0 and i < len(expression) - 1:
                    has_outer_most_bracket = False
                    break

        # 最も外側に丸括弧がない場合は、与えられた文字列をそのまま返す
        if not has_outer_most_bracket:
            return expression
        
        # 文字列の長さが2未満の場合は、つまり空の丸括弧"()"なのでエラーとする
        if len(expression) <= 2:
            raise Exception(f"empty bracket: {expression}")
        
        # 最初と最後の文字を取り除く(最も外側の丸括弧を取り除く)
        expression = expression[1:-1]

        # 取り除いた後の文字列の最も外側に括弧が残っている場合
        if expression[:1] == "(" and expression[-1:] == ")":
            # 再帰的に呼び出して取り除く
            expression = Node.__remove_outer_most_bracket(expression)

        # 取り除いた結果を返す
        return expression

    def get_operator_position(self,expression):
        """式から最も右側にあり、かつ優先順位が低い演算子を探して位置を返すメソッド
         @param  expression 式
         @return pos_operator 演算子の位置(演算子がない場合は-1を返す)"""        
        if not expression or len(expression) == 0:
            return -1

        pos_operator = -1 # 現在見つかっている演算子の位置(初期値として-1=演算子なしを設定)
        current_priority = self._max_priority # 現在見つかっている演算子の優先順位
        nest = 0 # 丸括弧の深度(括弧でくくられていない部分の演算子を「最も優先順位が低い」と判断するために用いる)

        for i in range(len(expression)):
            priority = 0 # 演算子の優先順位(値が低いほど優先順位が低いものとする)
            # 文字が丸括弧の場合は、括弧の深度を設定する
            if expression[i] == "(":
                nest += 1
                continue
            elif expression[i] == ")":
                nest -= 1
                continue
            # 文字が演算子かどうか検証し、演算子の場合は演算子の優先順位を設定する
            elif expression[i] in self.op_pri_dic:
                priority = self.op_pri_dic[expression[i]]
            # それ以外の文字の場合は何もしない
            else:
                continue
            
            # 括弧の深度が0(丸括弧でくくられていない部分)かつ、
            # 現在見つかっている演算子よりも優先順位が同じか低い場合
            # (優先順位が同じ場合は、より右側に同じ優先順位の演算子があることになる)
            if nest == 0 and priority <= current_priority:
                # 最も優先順位が低い演算子とみなし、その位置を保存する
                current_priority = priority
                pos_operator = i
                
        # 見つかった演算子の位置を返す
        return pos_operator

    def traverse_postorder(self):
        """後行順序訪問(帰りがけ順)で二分木を巡回して
         すべてのノードの演算子または項を表示するメソッド"""
        # 左右に子ノードをもつ場合、表示する前にノードを再帰的に巡回する
        if self.left:
            self.left.traverse_postorder()
        if self.right:
            self.right.traverse_postorder()
        # 巡回を終えた後でノードの演算子または項を表示する
        print(self.expression[0] + " ", end = "")

    def traverse_inorder(self):
        """中間順序訪問(通りがけ順)で二分木を巡回して
         すべてのノードの演算子または項を表示するメソッド"""
        # 左右に項を持つ場合、読みやすさのために項の前に開き括弧を補う
        if self.left and self.right:
            print("(", end = "")

        # 表示する前に左の子ノードを再帰的に巡回する
        if self.left:
            self.left.traverse_inorder()
            print(" ", end = "")

        # 左の子ノードの巡回を終えた後でノードの演算子または項を表示する
        print(self.expression[0], end = "")

        # 表示した後に右の子ノードを再帰的に巡回する
        if self.right:
            print(" ", end = "")
            self.right.traverse_inorder()

        # 左右に項を持つ場合、読みやすさのために項の後に閉じ括弧を補う
        if self.left and self.right:
            print(")", end = "")

    def traverse_preorder(self):
        """先行順序訪問(行きがけ順)で二分木を巡回して
         すべてのノードの演算子または項を表示するメソッド"""
        # 巡回を始める前にノードの演算子または項を表示する
        # (読みやすさのために項の後に空白を補って表示する)
        if self.left and self.right:
            print("(", end = "")

        print(self.expression[0] + " ", end = "")

        # 左右に子ノードをもつ場合、表示した後にノードを再帰的に巡回する
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()
        
        if self.left and self.right:
            print(")", end = "")

    def calculate(self):
        """現在のノードの演算子と左右の子ノードの値から、ノードの値を計算するメソッド
         @retval True  ノードの値が計算できた(計算結果はexpressionに文字列として代入)
         @retval False ノードの値が計算できない(記号を含む場合など)"""
        # 左右に子ノードを持たない場合、現在のノードは部分式ではなく項であり、
        # それ以上計算できないのでTrueを返す
        if not self.left and not self.right:
            return True        

        # 左右の子ノードについて、再帰的にノードの値を計算する
        if self.left:
            self.left.calculate()
        if self.right:
            self.right.calculate()    
        if self.left:
            if Node.validate_num(self.left.expression[0]):
                #print("dl:",self.left.expression)
                self.push(float(self.left.expression[0]))
        if self.right:
            if Node.validate_num(self.right.expression[0]):
                #print("dr:",self.right.expression)
                self.push(float(self.right.expression[0]))
        #print("d00:",self.expression)       
        # 現在のノードの演算子に応じて左右の子ノードの値を演算し、
        # 演算した結果を文字列に変換して再度expressionに代入することで現在のノードの値とする
        if self.expression[0] in self.op_dic:
            self.op_dic[self.expression[0]]()
        else:
            return False

        # 左右の子ノードの値から現在のノードの値が求まったため、
        # このノードは左右に子ノードを持たない値のみのノードとする
        self.left = None
        self.right = None
        
        # 計算できたため、Trueを返す
        return True

    @staticmethod
    def input_num_expression():
        """入力を求める関数"""
        return input("数式を入力してください:")
    
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
                    Node.err()
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
        elif xs[0] in self.op_pri_dic:
            self.validate_element(xs[1:])
        elif Node.validate_num(xs[0]):
            self.validate_element(xs[1:])
        else:
            Node.err("無効な入力値です")

    @staticmethod
    def validate_num(s):
        """<検査関数>有効な数値かどうか検査する関数
           @param s 文字列
           @return  有効な数値の文字列"""
        if s[0] == "-":
            Node.validate_num(s[1:])
        elif s[0] == "+":
            Node.validate_num(s[1:])
        elif s.count(".") == 1:
            [a,b] = s.split(".")
            if not a.isdigit() or not b.isdigit():
                return False
            return True
        elif not s.isdigit():
            return False
        return True
    
    def test_exec(self):
        #self.set_operator_dict()        
        while True:
            num_expression = self.get_num_expression(Node.input_num_expression)
            if num_expression == "exit":
                return False            
            try:
                # 入力された式における括弧の対応数をチェックする
                Node.validate_bracket_balance(num_expression)

                # 二分木の根(root)ノードを作成し、式全体を格納する
                root = Node(num_expression)
                #root.set_operator_dict()
                print(f"数式要素: {root.expression}")

                # 根ノードに格納した式を二分木へと分割する
                root.parse()

                # 分割した二分木を帰りがけ順で巡回して表示(後置記法/逆ポーランド記法)
                print("\n後置記法: ", end = "")
                root.traverse_postorder()
                print()

                # 分割した二分木を通りがけ順で巡回して表示(中置記法)
                print("中置記法: ", end = "")
                root.traverse_inorder()
                print()

                # 分割した二分木を行きがけ順で巡回して表示(前置記法/ポーランド記法)
                print("前置記法: ", end = "")
                root.traverse_preorder()
                print()

                # 分割した二分木から式全体の値を計算する
                if root.calculate():
                    # 計算できた場合はその値を表示する
                    print(f"\n計算結果: {root.expression}\n")
                else:
                    print("calculated expression: ", end = "")
                    root.traverse_inorder()
                    print()
            except:
                print(f"「{num_expression}」は計算不可能な式です")
                print("正しい入力値をお願いします")
                self.clear()
            
def test():
    node = Node([])
    while node.test_exec():
        pass
    print("end")

# 実行部分
test()