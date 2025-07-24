from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cliente, PromotorVenda, Municipio


class ClienteForm(forms.ModelForm):
    """Formulário para cadastro de clientes"""
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=150, label='Nome de usuário')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar senha')
    
    class Meta:
        model = Cliente
        fields = ['municipio', 'promotor', 'limite_credito', 'status_financeiro']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está cadastrado.')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem')
        return password2
    
    def save(self, commit=True):
        # Criar usuário
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password1'],
            tipo_usuario='cliente'
        )
        
        # Criar cliente
        cliente = super().save(commit=False)
        cliente.user = user
        if commit:
            cliente.save()
        return cliente


class PromotorForm(forms.ModelForm):
    """Formulário para cadastro de promotores"""
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=150, label='Nome de usuário')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar senha')
    
    class Meta:
        model = PromotorVenda
        fields = ['municipio', 'comissao', 'meta_mensal']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está cadastrado.')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem')
        return password2
    
    def save(self, commit=True):
        # Criar usuário
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password1'],
            tipo_usuario='promotor'
        )
        
        # Criar promotor
        promotor = super().save(commit=False)
        promotor.user = user
        if commit:
            promotor.save()
        return promotor
