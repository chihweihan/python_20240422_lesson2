import pyinputplus as pyip

name = pyip.inputStr("請輸入姓名：")
height = pyip.inputFloat("請輸入身高(cm)：")
weight = pyip.inputFloat("糗輸入體重(kg)：")

def bmi(height:float,weight:float):
    return weight / (height / 100) ** 2

def get_status(bmi:float):
    if bmi < 18.5:
        result = "體重過輕"
    elif bmi < 24:
        result = "正常範圍"
    elif bmi < 27:
        result = "體重過重"
    elif bmi < 30:
        result = "輕度肥胖"
    elif bmi < 35:
        result = "中度肥胖"
    else:
        result = "重度肥胖"
    return result

BMI = bmi(height,weight)
print(f"{name}，您的BMI：{BMI}")
print(f"{name}，您屬於：{get_status(BMI)}")