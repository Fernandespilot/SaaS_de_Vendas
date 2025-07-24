"""
Utilitários para formatação e helpers
"""
from decimal import Decimal
from datetime import datetime, timedelta
from django.utils import timezone


def formatar_moeda(valor):
    """Formata um valor decimal para moeda brasileira"""
    if not valor:
        return "R$ 0,00"
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_cpf(cpf):
    """Formata um CPF para o padrão brasileiro"""
    if not cpf:
        return ""
    cpf = str(cpf).replace(".", "").replace("-", "")
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def formatar_telefone(telefone):
    """Formata um telefone para o padrão brasileiro"""
    if not telefone:
        return ""
    telefone = str(telefone).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    return telefone


def calcular_comissao(valor_venda, percentual_comissao):
    """Calcula a comissão baseada no valor de venda e percentual"""
    if not valor_venda or not percentual_comissao:
        return Decimal('0.00')
    return (valor_venda * percentual_comissao) / 100


def dias_uteis_entre_datas(data_inicio, data_fim):
    """Calcula o número de dias úteis entre duas datas"""
    if not data_inicio or not data_fim:
        return 0
    
    dias = 0
    data_atual = data_inicio
    
    while data_atual <= data_fim:
        if data_atual.weekday() < 5:  # Segunda a sexta
            dias += 1
        data_atual += timedelta(days=1)
    
    return dias


def gerar_codigo_pedido():
    """Gera um código único para pedido"""
    agora = timezone.now()
    return f"PED{agora.strftime('%Y%m%d%H%M%S')}"


def validar_cpf(cpf):
    """Valida um CPF brasileiro"""
    if not cpf:
        return False
    
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0
    
    # Verifica se os dígitos estão corretos
    return cpf[9] == str(digito1) and cpf[10] == str(digito2)


def obter_iniciais(nome):
    """Obtém as iniciais de um nome"""
    if not nome:
        return ""
    
    palavras = nome.split()
    if len(palavras) >= 2:
        return f"{palavras[0][0]}{palavras[-1][0]}".upper()
    return nome[0].upper() if nome else ""
