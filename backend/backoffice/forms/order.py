from django import forms

class OrderTypeSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    orderType = forms.JSONField()

    def clean_orderType(self):
        orderType_data = self.cleaned_data.get('orderType')
        required_keys = {'coderp', 'destipopedido', 'situacao', 'idfretecif', 'desccomposto'}
        if not all(key in orderType_data and orderType_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return orderType_data