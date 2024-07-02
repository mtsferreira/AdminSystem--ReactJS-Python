from django import forms

class ProductStructureSingleFormPost(forms.Form):
    id = forms.IntegerField()
    productStructure = forms.JSONField()

    def clean_productStructure(self):
        productStructure_data = self.cleaned_data.get('productStructure')
        required_keys = {'categoria', 'percomissao', 'perdescmaximo'}
        if not all(key in productStructure_data and productStructure_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return productStructure_data
    
class ProductLinesSingleFormPost(forms.Form):
    id = forms.IntegerField()
    type = forms.CharField()
    productLines = forms.JSONField(required=False)
    productLinesStructure = forms.JSONField(required=False)

    def clean_productLines(self):
        productLines_data = self.cleaned_data.get('productLines')
        type_data = self.cleaned_data.get('type')
        if type_data == 'updateProductLine':
            required_keys = {'deslinha', 'estrutura', 'situacao'}
            if not all(key in productLines_data and productLines_data[key] not in [None, ''] for key in required_keys):
                raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return productLines_data