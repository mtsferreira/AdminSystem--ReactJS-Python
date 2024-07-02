from django import forms
import re

class CompanyFormPost(forms.Form):
    companyId = forms.IntegerField()
    company = forms.JSONField()

    def clean_company(self):
        company_data = self.cleaned_data.get('company')
        required_keys = {'bairro', 'cep', 'cnpj', 'codibge', 'fantasia', 'idempresa', 'logradouro', 'numero', 'razao'}
        if not all(key in company_data and company_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return company_data
    

class LocalSaleSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    localSale = forms.JSONField()

    def clean_localSale(self):
        localSale_data = self.cleaned_data.get('localSale')
        required_keys = {'cnpj', 'razao', 'fantasia', 'cep', 'logradouro', 'numero', 'bairro', 'codibge', 'coderp', 'situacao'}
        if not all(key in localSale_data and localSale_data[key] not in [None, '', 'S/N'] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return localSale_data
    
    
class LocalSaleConfigSingleFormPost(forms.Form):
    id = forms.IntegerField()
    config = forms.JSONField()
    
    def clean_config(self):
        localsale_config_data = self.cleaned_data.get('config')
        required_keys = {'idfretecif', 'preco', 'desccomposto', 'descvolume', 'diasvalidade', 'coddeperp', 'prazomedio', 'desccooperado', 'desclocal', 'deslimite'}
        if not all(key in localsale_config_data and localsale_config_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return localsale_config_data
    

class LocalSaleEmailSingleFormPost(forms.Form):
    localSaleId = forms.IntegerField()
    localSaleEmail = forms.JSONField()
    
    def clean_localSaleEmail(self):
        localsale_email_data = self.cleaned_data.get('localSaleEmail')
        
        required_keys = {'idtipoemail_id', 'emailresposta', 'assunto', 'corpo', 'assinatura'}
        if not all(key in localsale_email_data and localsale_email_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, localsale_email_data['emailresposta']):
            raise forms.ValidationError('Formato inválido de e-mail')
        
        return localsale_email_data