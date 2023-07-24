from selenium import webdriver
from selenium.webdriver.common.by import By
from botcity.maestro import *

from selenium.webdriver.firefox.service import Service
from time import sleep


def main():
    try:
        # Setando o caminho do WebDriver do Firefox
        service = Service(executable_path=r"geckodriver.exe")

        # Código utilizando Selenium puro, sem nenhuma dependência do framework BotCity 
        bot = webdriver.Firefox(service=service)

        # Acessando página Practice Test Automation
        bot.get("https://practicetestautomation.com/practice-test-login/")

        # Buscando pelo elemento input de nome de usuário
        input_username = bot.find_element(By.ID, "username")
        # Ação de digitar
        input_username.send_keys("student")

        # Buscando pelo elemento input de senha
        input_password = bot.find_element(By.ID, "password")
        # Ação de digitar
        input_password.send_keys("Password123")

        # Buscando pelo elemento botão submit
        input_button = bot.find_element(By.ID, "submit")
        # Ação de clicar
        input_button.click()

        # Aguarda 3 segundos para garantir que carregou a página com resultado
        sleep(3)

        # Busca pela confirmação de login
        logged = bot.find_element(By.CSS_SELECTOR, ".post-title")
        print(logged.text)        

        # Busca pelo elemento botão log out
        logout = bot.find_element(By.CSS_SELECTOR, ".wp-block-button__link")
        # Ação de clicar
        logout.click()

        # Busca pelo titulo login para garantir que fez o logout
        bot.find_element(By.CSS_SELECTOR, "#login > h2:nth-child(1)")

    except Exception as ex:
        # Busca pelo elemento de mensagem de erro
        error_alert = bot.find_element(By.ID, "error")
        print(error_alert.text)
        print(ex)

    finally:
        # Finaliza fechando o navegador
        bot.quit()
        print("Finally")

if __name__ == "__main__":
    main()
