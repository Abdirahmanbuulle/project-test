while True:
    print("\n---- Smart Calculator ----")

    num1 = float(input("أدخل الرقم الأول: "))
    num2 = float(input("أدخل الرقم الثاني: "))

    if num1 < 0:
        print("تنبيه: الرقم الأول سالب.")
    else:
        print("الرقم الأول موجب.")

    if num2 < 0:
        print("تنبيه: الرقم الثاني سالب.")
    else:
        print("الرقم الثاني موجب.")


    print("\nاختر العملية:")
    print("+  للجمع")
    print("-  للطرح")
    print("*  للضرب")
    print("/  للقسمة")
    print("** للأس (رفع العدد لقوة)")

    op = input("أدخل رمز العملية: ")


    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "خطأ: لا يمكن القسمة على صفر!"
    elif op == "**":
        result = num1 ** num2
    else:
        result = "عملية غير صحيحة!"

    print("\nالناتج =", result)

    print("\nمقارنة الرقمين:")
    if num1 > num2:
        print("الرقم الأول أكبر من الرقم الثاني.")
    elif num1 < num2:
        print("الرقم الأول أصغر من الرقم الثاني.")
    else:
        print("الرقمين متساويين.")

    again = input("\nهل تريد إجراء عملية أخرى؟ (y/n): ")
    if again.lower() != "y":
        print("تم إنهاء البرنامج.")
        break