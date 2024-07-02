from django import forms

class CustomerProfileFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    profile = forms.JSONField()

    def clean_profile(self):
        profile_data = self.cleaned_data.get('profile')
        required_keys = {'limitecredito'}
        if not all(key in profile_data and profile_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return profile_data
    

class CustomerSellerSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    customerSellerId = forms.IntegerField(required=False)
    customerSeller = forms.JSONField()
    
    
    def clean_customerSeller(self):
        customerSeller_data = self.cleaned_data.get('customerSeller')
        required_keys = {'idcascata', 'idvolume'}
        if not all(key in customerSeller_data and customerSeller_data[key] not in [None, ''] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return customerSeller_data