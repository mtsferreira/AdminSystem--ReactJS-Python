from django import forms

class SalesRegionSingleFormPost(forms.Form):
    id = forms.IntegerField()
    type = forms.CharField()
    salesRegion = forms.JSONField(required=False)
    infos = forms.JSONField(required=False)

    def clean_salesRegion(self):
        salesregion_data = self.cleaned_data.get('salesRegion')
        type_data = self.cleaned_data.get('type')
        if type_data == 'updateDescription':
            required_keys = {'desregiao', 'situacao'}
            if not all(key in salesregion_data and salesregion_data[key] not in [None, ''] for key in required_keys):
                raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return salesregion_data