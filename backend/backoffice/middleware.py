import json

class ConvertBooleanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            try:
                # Verifique se o corpo da solicitação é um JSON válido
                data = json.loads(request.body.decode('utf-8'))
                self.convert_values(data)
                request._body = json.dumps(data).encode('utf-8')
            except json.JSONDecodeError:
                pass
        elif request.method == 'GET' or request.method == 'DELETE':
            try:
                data = request.GET.copy()
                self.convert_values(data)
                request.GET = data
            except:
                pass

        response = self.get_response(request)
        return response

    def convert_values(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    if value.lower() == 'true':
                        data[key] = True
                    elif value.lower() == 'false':
                        data[key] = False
                    elif value.lower() == 'null':
                        data[key] = None
                elif isinstance(value, dict):
                    self.convert_values(value)
                elif isinstance(value, list):
                    for item in value:
                        self.convert_values(item)
        elif isinstance(data, list):
            for item in data:
                self.convert_values(item)
