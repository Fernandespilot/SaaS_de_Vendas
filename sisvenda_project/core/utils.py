from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from decimal import Decimal
import uuid
from datetime import datetime

User = get_user_model()


def gerar_codigo_pedido():
    """Gera um código único para o pedido"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_part = str(uuid.uuid4())[:8].upper()
    return f"PED-{timestamp}-{random_part}"


def enviar_notificacao_status(pedido):
    """Envia notificação por email sobre mudança de status do pedido"""
    try:
        # Notificar cliente
        if pedido.cliente and pedido.cliente.user.email:
            subject = f'Atualização do seu pedido {pedido.codigo}'
            message = render_to_string('core/emails/status_pedido.html', {
                'pedido': pedido,
                'cliente': pedido.cliente,
                'status_display': pedido.get_status_display(),
            })
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [pedido.cliente.user.email],
                fail_silently=True,
                html_message=message
            )
        
        # Notificar promotor
        if pedido.promotor and pedido.promotor.user.email:
            subject = f'Atualização do pedido {pedido.codigo}'
            message = render_to_string('core/emails/status_pedido_promotor.html', {
                'pedido': pedido,
                'promotor': pedido.promotor,
                'status_display': pedido.get_status_display(),
            })
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [pedido.promotor.user.email],
                fail_silently=True,
                html_message=message
            )
            
    except Exception as e:
        # Log do erro (em produção, usar logging adequado)
        print(f"Erro ao enviar notificação: {e}")


def calcular_comissao(pedido):
    """Calcula a comissão do promotor para um pedido"""
    if not pedido.promotor:
        return Decimal('0.00')
    
    valor_total = pedido.valor_total
    percentual_comissao = pedido.promotor.comissao_percentual / 100
    
    return valor_total * percentual_comissao


def verificar_estoque_disponivel(pedido):
    """Verifica se há estoque disponível para todos os itens do pedido"""
    itens_sem_estoque = []
    
    for item in pedido.itens.all():
        if item.produto.estoque < item.quantidade:
            itens_sem_estoque.append({
                'produto': item.produto,
                'quantidade_solicitada': item.quantidade,
                'estoque_disponivel': item.produto.estoque
            })
    
    return itens_sem_estoque


def atualizar_estoque(pedido, operacao='reduzir'):
    """Atualiza o estoque dos produtos do pedido"""
    for item in pedido.itens.all():
        produto = item.produto
        
        if operacao == 'reduzir':
            produto.estoque -= item.quantidade
        elif operacao == 'aumentar':
            produto.estoque += item.quantidade
        
        produto.save()


def get_dashboard_stats(user):
    """Retorna estatísticas para o dashboard baseado no tipo de usuário"""
    from .models import Pedido, Cliente, PromotorVenda, Produto
    
    stats = {}
    
    if user.tipo_usuario == 'promotor':
        try:
            promotor = PromotorVenda.objects.get(user=user)
            stats = {
                'clientes_area': Cliente.objects.filter(
                    municipio__in=promotor.municipios_cobertura.all()
                ).count(),
                'pedidos_mes': Pedido.objects.filter(
                    promotor=promotor,
                    data_pedido__month=timezone.now().month
                ).count(),
                'pedidos_pendentes': Pedido.objects.filter(
                    promotor=promotor,
                    status='pendente'
                ).count(),
            }
        except PromotorVenda.DoesNotExist:
            pass
    
    elif user.tipo_usuario == 'cliente':
        try:
            cliente = Cliente.objects.get(user=user)
            stats = {
                'pedidos_total': Pedido.objects.filter(cliente=cliente).count(),
                'pedidos_pendentes': Pedido.objects.filter(
                    cliente=cliente,
                    status__in=['pendente', 'aprovado_estoque', 'aprovado_vendas']
                ).count(),
                'pedidos_concluidos': Pedido.objects.filter(
                    cliente=cliente,
                    status='concluido'
                ).count(),
            }
        except Cliente.DoesNotExist:
            pass
    
    elif user.tipo_usuario == 'gerente_estoque':
        stats = {
            'pedidos_avaliar': Pedido.objects.filter(status='pendente').count(),
            'pedidos_programar': Pedido.objects.filter(status='aprovado_vendas').count(),
            'entregas_hoje': Pedido.objects.filter(
                data_entrega_programada=timezone.now().date(),
                status='programado'
            ).count(),
            'produtos_estoque_baixo': Produto.objects.filter(estoque__lt=10).count(),
        }
    
    elif user.tipo_usuario == 'gerente_vendas':
        stats = {
            'pedidos_avaliar': Pedido.objects.filter(status='aprovado_estoque').count(),
            'vendas_mes': Pedido.objects.filter(
                data_pedido__month=timezone.now().month,
                status='concluido'
            ).count(),
            'clientes_total': Cliente.objects.count(),
            'promotores_total': PromotorVenda.objects.count(),
        }
    
    elif user.tipo_usuario == 'gerenciador':
        stats = {
            'total_promotores': PromotorVenda.objects.count(),
            'total_clientes': Cliente.objects.count(),
            'total_produtos': Produto.objects.count(),
            'pedidos_total': Pedido.objects.count(),
        }
    
    return stats


def formatar_moeda(valor):
    """Formata valor para moeda brasileira"""
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def formatar_telefone(telefone):
    """Formata número de telefone"""
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    return telefone


def formatar_cpf(cpf):
    """Formata CPF"""
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def validar_cpf(cpf):
    """Valida CPF"""
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Validação do primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != dv1:
        return False
    
    # Validação do segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto
    
    return int(cpf[10]) == dv2


def get_status_color(status):
    """Retorna a cor do badge baseado no status"""
    colors = {
        'pendente': 'warning',
        'aprovado_estoque': 'info',
        'reprovado_estoque': 'danger',
        'aprovado_vendas': 'primary',
        'reprovado_vendas': 'danger',
        'programado': 'success',
        'processado': 'success',
        'concluido': 'success',
        'cancelado': 'secondary',
    }
    return colors.get(status, 'secondary')


def get_proximos_vencimentos():
    """Retorna pedidos com entrega programada para os próximos dias"""
    from .models import Pedido
    from datetime import timedelta
    
    hoje = timezone.now().date()
    proximos_7_dias = hoje + timedelta(days=7)
    
    return Pedido.objects.filter(
        data_entrega_programada__range=[hoje, proximos_7_dias],
        status='programado'
    ).order_by('data_entrega_programada')


def criar_usuario_admin_padrao():
    """Cria usuário admin padrão se não existir"""
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@sisvenda.com',
                password='admin123',
                first_name='Administrador',
                last_name='Sistema',
                tipo_usuario='gerenciador'
            )
            print("Usuário admin criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário admin: {e}")
