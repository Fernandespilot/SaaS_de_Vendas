"""
Formulários para o app de pedidos
"""
from django import forms
from .models import Pedido, ItemPedido
from apps.produtos.models import Produto
from apps.usuarios.models import User

class PedidoForm(forms.ModelForm):
    """Formulário para pedidos"""
    
    class Meta:
        model = Pedido
        fields = ['usuario', 'observacoes']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observações sobre o pedido...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = User.objects.filter(
            tipo_usuario='cliente'
        )
        self.fields['usuario'].empty_label = "Selecione o cliente"

class ItemPedidoForm(forms.ModelForm):
    """Formulário para itens do pedido"""
    
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'step': 1,
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(
            ativo=True,
            estoque__gt=0
        )
        self.fields['produto'].empty_label = "Selecione o produto"
    
    def clean_quantidade(self):
        """Valida a quantidade do produto"""
        quantidade = self.cleaned_data.get('quantidade')
        produto = self.cleaned_data.get('produto')
        
        if produto and quantidade:
            if quantidade > produto.estoque:
                raise forms.ValidationError(
                    f'Quantidade máxima disponível: {produto.estoque}'
                )
        
        return quantidade

class PedidoStatusForm(forms.ModelForm):
    """Formulário para atualizar status do pedido"""
    
    class Meta:
        model = Pedido
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
