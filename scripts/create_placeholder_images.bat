@echo off
REM Script para criar imagens de exemplo para o repositório
REM Este script cria imagens de placeholder para uso no README

echo Criando diretório de imagens...
if not exist "documents\img" mkdir documents\img

echo Criando imagens placeholder...

REM Criar arquivo SVG para o logo
echo ^<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg"^> > documents\img\logo-sisvenda.svg
echo   ^<style^> >> documents\img\logo-sisvenda.svg
echo     .title { font: bold 40px sans-serif; fill: #2c3e50; } >> documents\img\logo-sisvenda.svg
echo     .tagline { font: italic 20px sans-serif; fill: #34495e; } >> documents\img\logo-sisvenda.svg
echo     .icon-part { fill: #3498db; } >> documents\img\logo-sisvenda.svg
echo     .icon-highlight { fill: #2980b9; } >> documents\img\logo-sisvenda.svg
echo   ^</style^> >> documents\img\logo-sisvenda.svg
echo   ^<g transform="translate(20,20)"^> >> documents\img\logo-sisvenda.svg
echo     ^<rect x="0" y="0" width="60" height="60" rx="10" class="icon-part" /^> >> documents\img\logo-sisvenda.svg
echo     ^<rect x="10" y="10" width="40" height="10" rx="2" fill="white" /^> >> documents\img\logo-sisvenda.svg
echo     ^<rect x="10" y="25" width="40" height="10" rx="2" fill="white" /^> >> documents\img\logo-sisvenda.svg
echo     ^<rect x="10" y="40" width="40" height="10" rx="2" fill="white" /^> >> documents\img\logo-sisvenda.svg
echo     ^<circle cx="45" cy="60" r="15" class="icon-highlight" /^> >> documents\img\logo-sisvenda.svg
echo     ^<text x="39" y="65" font-size="16" fill="white"^>$^</text^> >> documents\img\logo-sisvenda.svg
echo   ^</g^> >> documents\img\logo-sisvenda.svg
echo   ^<text x="100" y="55" class="title"^>SisVenda^</text^> >> documents\img\logo-sisvenda.svg
echo   ^<text x="100" y="80" class="tagline"^>Gestão de Vendas^</text^> >> documents\img\logo-sisvenda.svg
echo ^</svg^> >> documents\img\logo-sisvenda.svg

REM Criar placeholders para screenshots
echo ^<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg"^> > documents\img\dashboard-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\dashboard-screenshot.svg
echo   ^<text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle"^>Dashboard SisVenda^</text^> >> documents\img\dashboard-screenshot.svg
echo ^</svg^> >> documents\img\dashboard-screenshot.svg

echo ^<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg"^> > documents\img\produtos-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\produtos-screenshot.svg
echo   ^<text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle"^>Gestão de Produtos^</text^> >> documents\img\produtos-screenshot.svg
echo ^</svg^> >> documents\img\produtos-screenshot.svg

echo ^<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg"^> > documents\img\relatorios-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\relatorios-screenshot.svg
echo   ^<text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle"^>Relatórios e Gráficos^</text^> >> documents\img\relatorios-screenshot.svg
echo ^</svg^> >> documents\img\relatorios-screenshot.svg

echo ^<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg"^> > documents\img\pedidos-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\pedidos-screenshot.svg
echo   ^<text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle"^>Gestão de Pedidos^</text^> >> documents\img\pedidos-screenshot.svg
echo ^</svg^> >> documents\img\pedidos-screenshot.svg

echo ^<svg width="300" height="600" xmlns="http://www.w3.org/2000/svg"^> > documents\img\mobile-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\mobile-screenshot.svg
echo   ^<text x="150" y="300" font-family="Arial" font-size="18" text-anchor="middle"^>Versão Mobile SisVenda^</text^> >> documents\img\mobile-screenshot.svg
echo ^</svg^> >> documents\img\mobile-screenshot.svg

echo ^<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg"^> > documents\img\testes-screenshot.svg
echo   ^<rect width="100%" height="100%" fill="#f0f0f0"/^> >> documents\img\testes-screenshot.svg
echo   ^<text x="400" y="250" font-family="Arial" font-size="24" text-anchor="middle"^>Testes Automatizados^</text^> >> documents\img\testes-screenshot.svg
echo ^</svg^> >> documents\img\testes-screenshot.svg

echo Convertendo SVGs para PNGs (se possível)...
echo Para concluir a criação das imagens, você precisará converter os SVGs para PNG.

echo Imagens de placeholder criadas com sucesso!
echo Você pode gerar imagens reais usando o script capture_screenshots.py
