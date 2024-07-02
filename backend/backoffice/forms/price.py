from django import forms

class PriceRulesSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    priceRules = forms.JSONField()

    def clean_priceRules(self):
        priceRules_data = self.cleaned_data.get('priceRules')
        required_keys = {'desregra', 'peracrescimo', 'perdesconto', 'datainicial', 'datafinal'}
        if not all(key in priceRules_data and priceRules_data[key] not in [None, '', 'Invalid Date'] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return priceRules_data
    
class PriceSingleFormPost(forms.Form):
    id = forms.IntegerField(required=False)
    price = forms.JSONField()
    
    def clean_price(self):
        price_data = self.cleaned_data.get('price')
        required_keys = {'idprecoregra', 'perdesconto', 'idvolume'}
        if not all(key in price_data and price_data[key] not in [None, '', 'Invalid Date'] for key in required_keys):
            raise forms.ValidationError('Preencha todos os campos obrigatorios (*)')
        
        return price_data