from django import forms

class GraphicsGrouperFormPost(forms.Form):
    grouper = forms.JSONField()

    def clean_grouper(self):
        grouper_data = self.cleaned_data.get('grouper')
        required_keys = {'titulo', 'descricao', 'situacao', 'iddashtipografico', 'iddashgrafico_grupo'}
        if not all(key in grouper_data and grouper_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return grouper_data