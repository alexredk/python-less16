nomera={"alexa":"9","inga":"6","dasha":"3","gera":"13","liza":"22"}
for z,x in nomera.items():
    print("-"*40)
    print(f"Его зовут {z} , и его\ее любимое число : ")
    for task in x:
        print(f"\t\/{task}")
    print("-"*40)
