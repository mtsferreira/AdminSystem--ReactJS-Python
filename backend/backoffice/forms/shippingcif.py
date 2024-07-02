from django import forms

class ShippingCifSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    type = forms.CharField()
    shippingCif = forms.JSONField(required=False)
    shippingCifLocation = forms.JSONField(required=False)

    def clean_shippingCif(self):
        shippingCif_data = self.cleaned_data.get('shippingCif')
        type_data = self.cleaned_data.get('type')
        if type_data == 'updateOrCreate':
            required_keys = {'desfretecif', 'datainicial', 'datafinal', 'perdesconto1', 'perdesconto2', 'situacao'}
            if not all(key in shippingCif_data and shippingCif_data[key] not in [None, ''] for key in required_keys):
                raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return shippingCif_data