身高 = input ('你的身高是（厘米）：')
体重 = input ('你的体重是（公斤）: ')
身高 = float(身高)
体重 = float(体重)
身高=身高/100
BMI = 体重/身高**2 
if BMI < 18.5:
    print(BMI,'体重过轻')
elif BMI >= 18.5 and BMI < 24:
    print(BMI,'体重正常')
elif BMI >= 24 and BMI < 27:
    print(BMI,'过胖')
elif BMI >= 27 and BMI < 30:
    print(BMI,'轻度肥胖')
elif BMI >= 30 and BMI < 35:
     print(BMI,'中度肥胖')
else:
    print(BMI,'重度肥胖')