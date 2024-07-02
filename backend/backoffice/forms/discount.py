from django import forms


class CascadeDiscountSingleFormPost(forms.Form):
    id = forms.IntegerField()
    discount = forms.JSONField()

    def clean_discount(self):
        discount_data = self.cleaned_data.get('discount')
        required_keys = {'idcascata', 'descascata'}
        if not all(key in discount_data and discount_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return discount_data
    

class CascadeDiscountTermFormPost(forms.Form):
    id = forms.IntegerField()
    discount = forms.JSONField()

    def clean_discount(self):
        discount_data = self.cleaned_data.get('discount')
        required_keys = {'idcascata', 'sigla', 'permaximo', 'tipocascata'}
        if not all(key in discount_data and discount_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return discount_data