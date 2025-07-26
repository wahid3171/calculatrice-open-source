def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "❌ خطأ : لا يمكن القسمة على 0"

def puissance(a, b):
    return a ** b

def calculatrice():
    print("=== آلة حاسبة بسيطة ===")
    print("📘 العمليات المتاحة : + - * / ^")

    while True:
        try:
            a = float(input("🔢 أدخل الرقم الأول : "))
            b = float(input("🔢 أدخل الرقم الثاني : "))
            operateur = input("🔧 اختر العملية (+, -, *, /, ^) : ")

            if operateur == '+':
                print("✅ النتيجة :", addition(a, b))
            elif operateur == '-':
                print("✅ النتيجة :", soustraction(a, b))
            elif operateur == '*':
                print("✅ النتيجة :", multiplication(a, b))
            elif operateur == '/':
                print("✅ النتيجة :", division(a, b))
            elif operateur == '^':
                print("✅ النتيجة :", puissance(a, b))
            else:
                print("❌ عملية غير معروفة")

            encore = input("🔁 هل تريد إجراء عملية أخرى ؟ (o/n) : ")
            if encore.lower() != 'o':
                print("📌 إلى اللقاء !")
                break

        except ValueError:
            print("⚠️ خطأ في الإدخال، يرجى إدخال أرقام صحيحة.")

calculatrice()