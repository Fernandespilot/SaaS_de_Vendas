"""
Serviços para notificações por email
"""
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model
import logging

User = get_user_model()
logger = logging.getLogger(__name__)


class EmailService:
    """Serviço para envio de emails"""
    
    @staticmethod
    def enviar_email_simples(destinatario, assunto, mensagem):
        """Envia um email simples"""
        try:
            send_mail(
                subject=assunto,
                message=mensagem,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[destinatario],
                fail_silently=False,
            )
            logger.info(f"Email enviado para {destinatario}: {assunto}")
            return True
        except Exception as e:
            logger.error(f"Erro ao enviar email para {destinatario}: {e}")
            return False
    
    @staticmethod
    def enviar_email_html(destinatario, assunto, template, context):
        """Envia um email com template HTML"""
        try:
            html_content = render_to_string(template, context)
            text_content = strip_tags(html_content)
            
            msg = EmailMultiAlternatives(
                subject=assunto,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[destinatario]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            logger.info(f"Email HTML enviado para {destinatario}: {assunto}")
            return True
        except Exception as e:
            logger.error(f"Erro ao enviar email HTML para {destinatario}: {e}")
            return False
    
    @staticmethod
    def notificar_novo_pedido(pedido):
        """Notifica sobre um novo pedido"""
        # Notificar gerente de estoque
        gerentes_estoque = User.objects.filter(tipo_usuario='gerente_estoque', is_active=True)
        for gerente in gerentes_estoque:
            EmailService.enviar_email_html(
                destinatario=gerente.email,
                assunto=f"Novo Pedido - {pedido.codigo}",
                template='emails/novo_pedido.html',
                context={
                    'pedido': pedido,
                    'usuario': gerente,
                    'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
                }
            )
    
    @staticmethod
    def notificar_pedido_aprovado(pedido):
        """Notifica sobre pedido aprovado"""
        # Notificar cliente
        EmailService.enviar_email_html(
            destinatario=pedido.cliente.user.email,
            assunto=f"Pedido Aprovado - {pedido.codigo}",
            template='emails/pedido_aprovado.html',
            context={
                'pedido': pedido,
                'cliente': pedido.cliente,
                'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
            }
        )
        
        # Notificar promotor
        EmailService.enviar_email_html(
            destinatario=pedido.promotor.user.email,
            assunto=f"Pedido Aprovado - {pedido.codigo}",
            template='emails/pedido_aprovado_promotor.html',
            context={
                'pedido': pedido,
                'promotor': pedido.promotor,
                'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
            }
        )
    
    @staticmethod
    def notificar_pedido_cancelado(pedido, motivo=""):
        """Notifica sobre pedido cancelado"""
        # Notificar cliente
        EmailService.enviar_email_html(
            destinatario=pedido.cliente.user.email,
            assunto=f"Pedido Cancelado - {pedido.codigo}",
            template='emails/pedido_cancelado.html',
            context={
                'pedido': pedido,
                'cliente': pedido.cliente,
                'motivo': motivo,
                'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
            }
        )
        
        # Notificar promotor
        EmailService.enviar_email_html(
            destinatario=pedido.promotor.user.email,
            assunto=f"Pedido Cancelado - {pedido.codigo}",
            template='emails/pedido_cancelado_promotor.html',
            context={
                'pedido': pedido,
                'promotor': pedido.promotor,
                'motivo': motivo,
                'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
            }
        )
    
    @staticmethod
    def notificar_entrega_programada(pedido):
        """Notifica sobre entrega programada"""
        EmailService.enviar_email_html(
            destinatario=pedido.cliente.user.email,
            assunto=f"Entrega Programada - {pedido.codigo}",
            template='emails/entrega_programada.html',
            context={
                'pedido': pedido,
                'cliente': pedido.cliente,
                'url_pedido': f"{settings.SITE_URL}/pedidos/{pedido.id}/"
            }
        )
    
    @staticmethod
    def notificar_produto_estoque_baixo(produto):
        """Notifica sobre produto com estoque baixo"""
        gerentes_estoque = User.objects.filter(tipo_usuario='gerente_estoque', is_active=True)
        for gerente in gerentes_estoque:
            EmailService.enviar_email_html(
                destinatario=gerente.email,
                assunto=f"Estoque Baixo - {produto.nome}",
                template='emails/estoque_baixo.html',
                context={
                    'produto': produto,
                    'usuario': gerente,
                    'url_produto': f"{settings.SITE_URL}/produtos/{produto.id}/"
                }
            )
