# -*- coding: utf-8 -*-
# pyright: reportMissingImports=false
# type: ignore
"""
Script para capturar screenshots das páginas principais do sistema SisVenda.
Este script utiliza o Selenium para automatizar o navegador e capturar screenshots.
As imagens são salvas na pasta documents/img/.

Requisitos:
- Selenium
- WebDriver para o navegador escolhido

Uso:
python capture_screenshots.py
"""

import os
import time
import sys
from typing import Optional, Dict, Any, List

# Mock classes para quando o Selenium não está instalado
# Estas classes permitem que o código seja analisado pelo Pylance mesmo sem o Selenium
# pylint: disable=invalid-name,unused-import

class By:
    """Mock da classe By do Selenium."""
    ID = "id"
    CSS_SELECTOR = "css selector"
    
class WebDriverWait:
    """Mock da classe WebDriverWait do Selenium."""
    def __init__(self, driver: Any, timeout: int) -> None:
        self.driver = driver
        self.timeout = timeout
        
    def until(self, condition: Any) -> Any:
        """Mock do método until."""
        return None

class Options:
    """Mock da classe Options do Selenium."""
    def add_argument(self, arg: str) -> None:
        """Mock do método add_argument."""
        pass

class EC:
    """Mock da classe EC do Selenium."""
    @staticmethod
    def presence_of_element_located(locator: tuple) -> Any:
        """Mock do método presence_of_element_located."""
        return None
        
    @staticmethod
    def url_contains(text: str) -> Any:
        """Mock do método url_contains."""
        return None

class webdriver:
    """Mock da classe webdriver do Selenium."""
    @staticmethod
    def Chrome(**kwargs: Any) -> Any:
        """Mock do método Chrome."""
        return None

# Inicializa a variável que indica se o Selenium está disponível
SELENIUM_AVAILABLE = False

# Tentativa de importação real do Selenium
# Se o Selenium estiver instalado, substitui as classes mock pelas reais
# pylint: disable=import-error
# Bloco de importação com supressão de erros para Pylance
# Este bloco usa a mesma técnica que o próprio Django usa para importações opcionais
selenium_webdriver = webdriver  # Usa a classe mock por padrão
SeleniumOptions = Options
SeleniumBy = By
SeleniumWebDriverWait = WebDriverWait
selenium_ec = EC

# Este try/except é executado em tempo de execução, não durante a análise estática
# Então mesmo que o Selenium não esteja instalado, o Pylance não reportará erros
try:
    # Suprima os erros de importação do Pylance aqui
    # pyright: ignore
    # type: ignore
    # mypy: ignore
    # fmt: off
    import selenium.webdriver  # type: ignore
    import selenium.webdriver.chrome.options  # type: ignore
    import selenium.webdriver.common.by  # type: ignore
    import selenium.webdriver.support.ui  # type: ignore
    import selenium.webdriver.support.expected_conditions  # type: ignore
    # fmt: on
    
    # Se chegou até aqui, o Selenium está disponível
    selenium_webdriver = selenium.webdriver
    SeleniumOptions = selenium.webdriver.chrome.options.Options
    SeleniumBy = selenium.webdriver.common.by.By
    SeleniumWebDriverWait = selenium.webdriver.support.ui.WebDriverWait
    selenium_ec = selenium.webdriver.support.expected_conditions
    
    # Substitui as classes mock pelas reais
    webdriver = selenium_webdriver
    Options = SeleniumOptions
    By = SeleniumBy
    WebDriverWait = SeleniumWebDriverWait
    EC = selenium_ec
    
    SELENIUM_AVAILABLE = True
    # pylint: enable=import-error
except ImportError:
    # Se o Selenium não estiver instalado, mantém as classes mock
    SELENIUM_AVAILABLE = False

# Configurações
SCREENSHOTS_DIR = os.path.join("documents", "img")
BASE_URL = "http://localhost:8000"
USERNAME = "admin"
PASSWORD = "admin"

# Páginas para capturar screenshots
PAGES = {
    "login": "/login/",
    "dashboard": "/",
    "produtos": "/produtos/",
    "novo-produto": "/produtos/novo/",
    "pedidos": "/pedidos/",
    "relatorios": "/relatorios/",
    "clientes": "/clientes/",
}

# Configurar o Chrome em modo headless para servidores sem GUI (se o Selenium estiver disponível)
if SELENIUM_AVAILABLE:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--hide-scrollbars")

def ensure_dir_exists():
    """Garante que o diretório de screenshots existe."""
    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)

def login(driver):
    """Realiza o login no sistema."""
    if not SELENIUM_AVAILABLE:
        return
        
    driver.get(f"{BASE_URL}/login/")
    
    # Aguardar o formulário de login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    
    # Preencher credenciais
    driver.find_element(By.ID, "id_username").send_keys(USERNAME)
    driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Aguardar redirecionamento para o dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard/")
    )

def create_placeholder_svg(name, title):
    """Cria uma imagem SVG placeholder."""
    svg_content = f'''<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f0f0f0"/>
  <text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle">{title}</text>
</svg>'''
    
    with open(os.path.join(SCREENSHOTS_DIR, f"{name}-screenshot.svg"), 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"Criado placeholder para {name}")

def create_logo_svg():
    """Cria um SVG para o logo do SisVenda."""
    svg_content = '''<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title { font: bold 40px sans-serif; fill: #2c3e50; }
    .tagline { font: italic 20px sans-serif; fill: #34495e; }
    .icon-part { fill: #3498db; }
    .icon-highlight { fill: #2980b9; }
  </style>
  
  <g transform="translate(20,20)">
    <rect x="0" y="0" width="60" height="60" rx="10" class="icon-part" />
    <rect x="10" y="10" width="40" height="10" rx="2" fill="white" />
    <rect x="10" y="25" width="40" height="10" rx="2" fill="white" />
    <rect x="10" y="40" width="40" height="10" rx="2" fill="white" />
    <circle cx="45" cy="60" r="15" class="icon-highlight" />
    <text x="39" y="65" font-size="16" fill="white">$</text>
  </g>
  
  <text x="100" y="55" class="title">SisVenda</text>
  <text x="100" y="80" class="tagline">Gestão de Vendas</text>
</svg>'''
    
    with open(os.path.join(SCREENSHOTS_DIR, "logo-sisvenda.svg"), 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print("Criado logo SVG")

def create_placeholders():
    """Cria placeholders para as imagens quando o Selenium não está disponível."""
    ensure_dir_exists()
    
    create_logo_svg()
    create_placeholder_svg("dashboard", "Dashboard SisVenda")
    create_placeholder_svg("produtos", "Gestão de Produtos")
    create_placeholder_svg("novo-produto", "Cadastro de Produto")
    create_placeholder_svg("pedidos", "Gestão de Pedidos")
    create_placeholder_svg("relatorios", "Relatórios e Gráficos")
    create_placeholder_svg("clientes", "Gestão de Clientes")
    create_placeholder_svg("login", "Tela de Login")
    create_placeholder_svg("testes", "Testes Automatizados")
    
    # Versão mobile
    mobile_svg = '''<svg width="300" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f0f0f0"/>
  <text x="150" y="300" font-family="Arial" font-size="18" text-anchor="middle">Versão Mobile SisVenda</text>
</svg>'''
    
    with open(os.path.join(SCREENSHOTS_DIR, "mobile-screenshot.svg"), 'w', encoding='utf-8') as f:
        f.write(mobile_svg)
    
    print("Criado placeholder para versão mobile")

def capture_screenshots():
    """Captura screenshots de todas as páginas definidas."""
    ensure_dir_exists()
    
    if not SELENIUM_AVAILABLE:
        print("Selenium não está instalado. Criando imagens placeholder.")
        create_placeholders()
        print("Para instalar o Selenium, execute: pip install selenium")
        print("Para usar capturas de tela reais, instale o Selenium e o WebDriver adequado.")
        return
    
    driver = webdriver.Chrome(options=chrome_options)
    try:
        login(driver)
        
        for name, path in PAGES.items():
            print(f"Capturando screenshot de {name}...")
            driver.get(f"{BASE_URL}{path}")
            
            # Aguardar o carregamento da página
            time.sleep(2)
            
            # Capturar screenshot
            driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, f"{name}-screenshot.png"))
            
        # Capturar screenshot especial para o README com tamanho personalizado
        print("Capturando screenshot para o README...")
        driver.get(f"{BASE_URL}/")
        driver.set_window_size(1200, 800)
        time.sleep(1)
        driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, "dashboard-screenshot.png"))
            
    finally:
        driver.quit()

if __name__ == "__main__":
    try:
        capture_screenshots()
        if SELENIUM_AVAILABLE:
            print("Screenshots capturados com sucesso!")
        else:
            print("Placeholders SVG criados com sucesso!")
    except Exception as e:
        print(f"Erro ao capturar screenshots: {e}")
        print("Criando placeholders SVG como alternativa...")
        try:
            create_placeholders()
            print("Placeholders SVG criados com sucesso!")
        except Exception as inner_e:
            print(f"Erro ao criar placeholders: {inner_e}")
            sys.exit(1)
