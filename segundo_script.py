from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar o driver do Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))
driver.get("https://www.proeis.rj.gov.br/")

# Clicar no botão de escala
driver.find_element(By.ID, "btnEscala").click()

# Clicar no botão de nova inscrição
driver.find_element(By.ID, "btnNovaInscricao").click()

# Selecionar a opção no dropdown de convênios
ddl_convenios = Select(driver.find_element(
    By.ID, "ddlConvenios"))
# Insira o valor da opção desejada aqui
ddl_convenios.select_by_value("28 BPM - RAS")

# Selecionar a opção no dropdown de data do evento
ddl_data_evento = Select(driver.find_element(
    By.ID, "ddlConvenios"))
# Insira o valor da opção desejada aqui
ddl_data_evento.select_by_value("2024-02-10")

# Fechar o navegador do Selenium
