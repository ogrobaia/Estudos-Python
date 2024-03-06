

from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# iniciar o navegador com Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))
driver.get("https://www.proeis.rj.gov.br/")

# Extrair ID da página
page_id = driver.execute_script("return window.name;")
print("ID da Página:", page_id)

# selecionar CPF
driver.find_element(By.ID, "ddlTipoAcesso").click()
ddlTipoAcesso = driver.find_element(By.ID, "ddlTipoAcesso")
Select_ddlTipoAcesso = Select(ddlTipoAcesso)
Select_ddlTipoAcesso.select_by_visible_text("CPF")

# preenchimento do CPF
driver.find_element(By.ID, "txtLogin").send_keys("12994434784")
driver.find_element(By.ID, "txtSenha").send_keys("inicio@D")
