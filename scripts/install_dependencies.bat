@echo off
REM Script para instalar as dependências necessárias para o script capture_screenshots.py

echo Instalando dependências para captura de screenshots...
pip install selenium

echo.
echo Dependências instaladas com sucesso!
echo.
echo Para capturar screenshots, você também precisará instalar um webdriver compatível com seu navegador:
echo - Chrome WebDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
echo - Firefox WebDriver (GeckoDriver): https://github.com/mozilla/geckodriver/releases
echo.
echo Após instalar o webdriver, adicione-o ao PATH do sistema ou coloque-o na pasta do projeto.
echo.
echo Para mais informações, visite: https://selenium-python.readthedocs.io/installation.html
echo.
pause
