from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Cliente, Produto, Pedido, PromotorVenda, Municipio, GrupoProduto, ItemPedido

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Form customizado para criação de usuários"""
    first_name = forms.CharField(max_length=150, required=True, label='Nome')
    last_name = forms.CharField(max_length=150, required=True, label='Sobrenome')
    email = forms.EmailField(required=True, label='Email')
    telefone = forms.CharField(max_length=15, required=False, label='Telefone')
    cpf = forms.CharField(max_length=14, required=False, label='CPF')
    tipo_usuario = forms.ChoiceField(
        choices=[
            ('cliente', 'Cliente'),
            ('promotor', 'Promotor de Vendas'),
        ],
        required=True,
        label='Tipo de Usuário'
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telefone', 
                 'cpf', 'tipo_usuario', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ClienteForm(forms.ModelForm):
    """Form para cadastro de clientes"""
    # Campos do usuário
    first_name = forms.CharField(max_length=150, required=True, label='Nome')
    last_name = forms.CharField(max_length=150, required=True, label='Sobrenome')
    email = forms.EmailField(required=True, label='Email')
    telefone = forms.CharField(max_length=15, required=False, label='Telefone')
    cpf = forms.CharField(max_length=14, required=False, label='CPF')
    username = forms.CharField(max_length=150, required=True, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Senha')
    
    class Meta:
        model = Cliente
        fields = ['municipio', 'endereco', 'limite_credito', 'status_financeiro']
        labels = {
            'municipio': 'Município',
            'endereco': 'Endereço',
            'limite_credito': 'Limite de Crédito',
            'status_financeiro': 'Status Financeiro',
        }
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3}),
            'limite_credito': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    
    def save(self, commit=True):
        # Criar usuário primeiro
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            telefone=self.cleaned_data['telefone'],
            cpf=self.cleaned_data['cpf'],
            tipo_usuario='cliente'
        )
        
        # Criar cliente
        cliente = super().save(commit=False)
        cliente.user = user
        
        if commit:
            cliente.save()
        
        return cliente


class PromotorForm(forms.ModelForm):
    """Form para cadastro de promotores"""
    # Campos do usuário
    first_name = forms.CharField(max_length=150, required=True, label='Nome')
    last_name = forms.CharField(max_length=150, required=True, label='Sobrenome')
    email = forms.EmailField(required=True, label='Email')
    telefone = forms.CharField(max_length=15, required=False, label='Telefone')
    cpf = forms.CharField(max_length=14, required=True, label='CPF')
    username = forms.CharField(max_length=150, required=True, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Senha')
    
    class Meta:
        model = PromotorVenda
        fields = ['municipios_cobertura', 'comissao_percentual']
        labels = {
            'municipios_cobertura': 'Municípios de Cobertura',
            'comissao_percentual': 'Percentual de Comissão (%)',
        }
        widgets = {
            'municipios_cobertura': forms.CheckboxSelectMultiple(),
            'comissao_percentual': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'municipios_cobertura':
                field.widget.attrs.update({'class': 'form-control'})
    
    def save(self, commit=True):
        # Criar usuário primeiro
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            telefone=self.cleaned_data['telefone'],
            cpf=self.cleaned_data['cpf'],
            tipo_usuario='promotor'
        )
        
        # Criar promotor
        promotor = super().save(commit=False)
        promotor.user = user
        
        if commit:
            promotor.save()
            self.save_m2m()
        
        return promotor


class ProdutoForm(forms.ModelForm):
    """Form para cadastro de produtos"""
    
    class Meta:
        model = Produto
        fields = [
            'codigo', 'nome', 'grupo', 'custo', 'margem_lucro', 
            'estoque', 'percentual_promocao', 'impostos', 'ativo'
        ]
        labels = {
            'codigo': 'Código',
            'nome': 'Nome',
            'grupo': 'Grupo',
            'custo': 'Custo',
            'margem_lucro': 'Margem de Lucro (%)',
            'estoque': 'Estoque',
            'percentual_promocao': 'Percentual de Promoção (%)',
            'impostos': 'Impostos (%)',
            'ativo': 'Ativo',
        }
        widgets = {
            'custo': forms.NumberInput(attrs={'step': '0.01'}),
            'margem_lucro': forms.NumberInput(attrs={'step': '0.01'}),
            'percentual_promocao': forms.NumberInput(attrs={'step': '0.01'}),
            'impostos': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'ativo':
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-check-input'})


class PedidoForm(forms.ModelForm):
    """Form para criação de pedidos"""
    
    class Meta:
        model = Pedido
        fields = ['cliente', 'observacoes']
        labels = {
            'cliente': 'Cliente',
            'observacoes': 'Observações',
        }
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        promotor = kwargs.pop('promotor', None)
        super().__init__(*args, **kwargs)
        
        if promotor:
            # Filtrar apenas clientes da área do promotor
            self.fields['cliente'].queryset = Cliente.objects.filter(
                municipio__in=promotor.municipios_cobertura.all()
            )
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ItemPedidoForm(forms.ModelForm):
    """Form para itens de pedido"""
    
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']
        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(ativo=True)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FiltroRelatorioForm(forms.Form):
    """Form para filtros de relatórios"""
    TIPO_RELATORIO_CHOICES = [
        ('produtos_estoque_baixo', 'Produtos com Estoque Baixo'),
        ('produtos_promocao', 'Produtos em Promoção'),
        ('produtos_por_grupo', 'Produtos por Grupo'),
        ('vendas_promotor', 'Vendas por Promotor'),
        ('comissoes', 'Relatório de Comissões'),
        ('pedidos_periodo', 'Pedidos por Período'),
    ]
    
    tipo_relatorio = forms.ChoiceField(
        choices=TIPO_RELATORIO_CHOICES,
        required=True,
        label='Tipo de Relatório'
    )
    
    data_inicio = forms.DateField(
        required=False,
        label='Data Início',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    data_fim = forms.DateField(
        required=False,
        label='Data Fim',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    grupo_produto = forms.ModelChoiceField(
        queryset=GrupoProduto.objects.all(),
        required=False,
        label='Grupo de Produto',
        empty_label='Todos os grupos'
    )
    
    promotor = forms.ModelChoiceField(
        queryset=PromotorVenda.objects.all(),
        required=False,
        label='Promotor',
        empty_label='Todos os promotores'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
