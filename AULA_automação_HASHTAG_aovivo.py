# Passo a passo do projeto

# Passo 1 - Entrar no Sistema
# Passo 2 - pip install pyautogui
import time
import pyautogui

# clicar - pyautogui.click
# escrever - pyautogui.write
# apertar uma tecla - pyautogui.press
# apertar - pyautogui.hotkey
pyautogui.PAUSE = 0.2

# Apertar uma tecla do windows (comando + barra de espaço)
pyautogui.press("win")
# digitar o nome do programa(chrome)
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

#digitar o link
link = "https://simulado.estacio.br/alunos/"
pyautogui.write(link)

# apertar enter
pyautogui.press("enter")

# esperar 5 segundos
time.sleep(2)

# Passo 2
pyautogui.click(x=3153, y=514)

# Digitar o ID
pyautogui.write("202104342446")

# click TAB
pyautogui.press("tab")
# pyautogui.press("tab")

# Digitar a Senha
pyautogui.write("DD2132")

# apertar enter
pyautogui.click(x=3150, y=649)
# pyautogui.press("enter")

## importar base de dados
## pip install pandas numpy openpyxl 
## import pandas 
## tagela = pandas.read_csv("produtos.csv")  TEM QUE ESTAR NA MESMA PASTA    
## print(tabela)



# digitar o link
# apertar enter  