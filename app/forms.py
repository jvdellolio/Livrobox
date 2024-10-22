from django import forms
from .models import Livro

class LoginForms(forms.Form):

    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Ex.: João Silva",
            }
        )
    )


    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )

class CadastroForms(forms.Form):

    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Ex.: JoãoSilva",
            }
        )
    )
    email=forms.EmailField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder": "Ex.: joaosilva@gmail.com",
            }
        )
    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )
    )

    senha_2 = forms.CharField(
        label="Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente",
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos em 'Nome de cadastro'")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("O campo das 'Senhas' não correspondem")
        else:
            return senha_2
        
class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = []
        labels = {
            'descrição': 'Descrição',
            'genero': 'Gênero',
            'titulo': 'Título',
            'ano_publicacao': 'Ano da Publicação',
            'usuario': 'Usuário',
            'nota': 'Nota',
            'autor': 'Autor',
            'imagem': 'Imagem',
        }

        widgets = {
            'genero': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'ano_publicacao': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'min': 1000,
                    'max': 9999,
                    'placeholder': 'Ano'
                }
            ),
            'nota': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 5,
                'step': 0.1
            }),
            'imagem': forms.FileInput(attrs={'class':'form-control'}),
            'descrição': forms.Textarea(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
