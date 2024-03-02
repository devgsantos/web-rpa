from selenium import webdriver
from selenium.webdriver.common.by import By
from resources.logger import Logger
import time

# CARREGAR O WEBDRIVER PARA O NAVEGADOR DESEJADOR
driver = webdriver.Firefox()

# ABRIR A PÁGINA DESEJADA
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
log = Logger


def main():
    send_text = 'Selenium'
    # PRINT DE INICIALIZAÇÃO DA APLICAÇÃO EM LOG
    log.create_log('INFO', f"Página da web iniciada -> {title}")

    # TEMPO DE ESPERO IMPLICITO PARA CARREGAMENTO DOS ELEMENTOS
    driver.implicitly_wait(0.5)

    # LOCALIZAR OS ELEMENTSO DESEJADOS DA PÁGINA
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # PREENCHIMENTO DE INPUT DE TEXTO
    text_box.send_keys(send_text)
    log.create_log('WARNING', f"Texto inserido no input -> {send_text}")

    # TEMPO DE ESPERO IMPLICITO PARA CARREGAMENTO DOS ELEMENTOS
    # time.sleep(10)

    # AÇÃO DE CLIQUE EM BOTÃO
    submit_button.click()
    log.create_log('INFO', 'Botão de submissão clicado.')

    # CAPTURAR TEXTO DE ELEMENTO
    message = driver.find_element(by=By.ID, value="message")
    text = message.text

    print(text, title)
    log.create_log('WARNING', f"Resposta recebida da página -> {text}")

    driver.quit()

    log.create_log('INFO', 'Página fechada.')
    log.create_log('INFO', 'Automação finalizada.')


if __name__ == '__main__':
    main()
