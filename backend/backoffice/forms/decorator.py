from functools import wraps
from django.http import JsonResponse

from .customer import *
from .discount import *
from .localsale import *
from .financial import *
from .layout import *
from .margin import *
from .messages import *
from .order import *
from .price import *
from .product import *
from .salesregion import *
from .shippingcif import *

def validate_form(form_name):
    def decorator(view_method):
        @wraps(view_method)
        def _wrapped_view(instance, request, *args, **kwargs):
            # Aqui usamos eval para obter a classe do formulário
            FormClass = eval(form_name)
            form = FormClass(request.data)
            
            if form.is_valid():
                return view_method(instance, request, *args, **kwargs)
            else:
                form_error = form.errors
                error_message = form_error[next(iter(form_error))][0]
                
                # return JsonResponse({"status": False, "message": form.errors}, status=400)
                return JsonResponse({"status": False, "message": error_message if error_message != 'This field is required.' else 'Preencha todos os campos obrigatorios (*)' }, status=400)
           
        return _wrapped_view
    return decorator

