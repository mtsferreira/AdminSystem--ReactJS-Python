from django import forms

class MessagePortalSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    portalMessage = forms.JSONField()

    def clean_portalMessage(self):
        portal_message_data = self.cleaned_data.get('portalMessage')
        required_keys = {'mensagem', 'datainicial', 'datafinal'}
        if not all(key in portal_message_data and portal_message_data[key] not in [None, '', 'Invalid Date'] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return portal_message_data