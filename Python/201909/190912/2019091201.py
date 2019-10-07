# 例外処理を行うBMI判定
def input_num():
    while True:
        try:
            weight = float(input("体重(kg)は ？："))
            height = float(input("身長(cm)は ？："))

            if(weight <= 0 or height < 0):
                print("正の整数を入力してください")
            else:
                height = height / 100
                bmi = weight / (height * height)
                return bmi           
            
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except:
            print("入力ミスがあります。再度入力してください。")
        
def check_bmi(bmi):
    result = ""
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi < 25:
        result = "標準体重"
    elif bmi < 30:
        result = "肥満（軽）"
    else:
        result = "肥満（重）"
    print("BMI:",round(bmi,2))
    print("判定:",result)

check_bmi(input_num())
