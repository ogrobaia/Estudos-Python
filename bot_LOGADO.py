
### importar para automatizar na Web
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

### entrar no site 

driver = webdriver.Firefox()
driver.get("https://www.proeis.rj.gov.br/FrmMenuVoluntario.aspx")
