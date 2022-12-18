import sys

if __name__ == "__main__":
    print ("Привет, студент :)")
    
    mes = int(input("Введите число для возведения в степень: "))
    n = int(input("Введите степень: "))
    
    mes = mes ** n
  
    print(f"Итоговый результат: " + str(mes))
