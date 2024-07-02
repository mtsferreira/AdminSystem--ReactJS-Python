from django import forms

class MarginsSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    margins = forms.JSONField()

    def clean_margins(self):
        margins_data = self.cleaned_data.get('margins')
        required_keys = {'desmargem', 'situacao', 'perminproduto', 'perminpedido', 'perdesproduto', 'perdespedido'}
        if not all(key in margins_data and margins_data[key] not in [None, '', 'Invalid Date'] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return margins_data