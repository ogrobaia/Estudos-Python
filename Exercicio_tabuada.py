n = int(input("Informe qual valor deseja inserir: "))
operação = input("Digite a operação a realizar (+,-,* ou /):")
x = 1

  
while x <= 10:
    if operação == "+":
      print(f"{n} {operação} {x} = {n + x}")
      x = x + 1           
    elif operação == "*":
      print(f"{n} {operação} {x} = {n * x}")
      x = x + 1     
    elif operação == "-":
      print(f"{n} {operação} {x} = {n - x}")
      x = x + 1    
    elif operação == "/":
      print(f"{n} {operação} {x} = {n / x}")
      x = x + 1    
    else:
      print("Operação inválida!")
    resultado = 0
print(f" tabuada de:{n} ")

