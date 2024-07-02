from django import forms


class FinancialTermSingleFormPost(forms.Form):
    id = forms.IntegerField()
    paymentTerm = forms.JSONField()

    def clean_paymentTerm(self):
        paymentTerm_data = self.cleaned_data.get('paymentTerm')
        required_keys = {'idprazofinanceiro', 'descprazo', 'situacao'}
        if not all(key in paymentTerm_data and paymentTerm_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return paymentTerm_data
    

class FinancialTermRangeFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    termRange = forms.JSONField()

    def clean_termRange(self):
        termRange_data = self.cleaned_data.get('termRange')
        required_keys = {'prazodias', 'perdesconto', 'peracrescimo', 'vlminimo'}
        if not all(key in termRange_data and termRange_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return termRange_data
    

class PaymentSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    infos = forms.JSONField()

    def clean_infos(self):
        infos_data = self.cleaned_data.get('infos')
        required_keys = {'prazodias', 'descpagamento', 'qparcela', 'situacao'}
        if not all(key in infos_data and infos_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return infos_data