# Automação de acesso ao site cproeis
# cpf do usuaro 129.944.347-84

# Passo 2 - pip install pyautogui
import time
import pyautogui

# apertar - pyautogui.hotkey
pyautogui.PAUSE = 0.4

# esperar 1 segundos
time.sleep(1)

#### Com a pagina ja Aberta inserir os dados de inscrição 

# clicar em Escala
pyautogui.click(x=2094, y=486)
# clicar em Nova Inscrição
pyautogui.click(x=2137, y=436)
# clicar em Convênio
pyautogui.click(x=2094, y=535)

# Mover o Mouse
pyautogui.moveTo(x=2211, y=402)

# Rolar o Scroll
pyautogui.scroll(-810)

# Click em 28Bpm
pyautogui.click(x=2114, y=336)

# click em data do evento
pyautogui.click(x=2101, y=625)

# Selecionar o Evento (verificar a posição de cada evento nas "DIMENSÕES DA TELA USADA")
# 1 
# 2
pyautogui.click(x=2205, y=366)
# 3
# 4 
# 5
# 6
# 7
# 8
# 9
# 10
# 11

# Rolar o Scroll
pyautogui.scroll(-500)

# Click em FILTRAR 
# pyautogui.click(x=3200, y=799)

# click em CPA
# pyautogui.click()