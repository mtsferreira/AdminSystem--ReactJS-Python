from django.db import connection
from django.db.models import CharField, Q, ForeignKey
from django.db import models
from rest_framework import status

import json


def call_raw_query(raw_query, params):
    with connection.cursor() as cursor:
        cursor.execute(raw_query, params)
        rows = dict_fetchall(cursor)

    return rows

def call_stored_procedure(procedure_name, params, responseParams=[], singleLine=True):
    cursor = connection.cursor()
    response = {
        'status': False,
        'message': '',
        'type': '',
        'http_status': None,
        'data': {}
    }
    try:
        
        sql = "EXEC {} '{}'".format(procedure_name, json.dumps(params))

        cursor.execute(sql)

        results = cursor.fetchall()

        if results:
            if singleLine:
                results = results[0][0]
                results = json.loads(results)

                if results['Retorno']:

                    response['status'] = False if results['Retorno']['Evento'] == 'Er' else True
                    response['message'] = results['Retorno']['Mensagem']
                    response['type'] = 'success' if results['Retorno']['Evento'] == 'Ok' else 'error' if results['Retorno']['Evento'] == 'Er' else 'warning'
                    response['http_status'] = status.HTTP_500_INTERNAL_SERVER_ERROR if results['Retorno']['Evento'] == 'Er' else status.HTTP_200_OK

            if response['status']:
                if responseParams:
                    for resp in responseParams:
                        response['data'][resp] = results[resp]
                else:
                    response['data'] = results

    finally:
        cursor.close()
    return response

def create_columns_by_list(fields, header_names):

    complete_headers = []
    for count, field in enumerate(fields):
        complete_headers.append([field, header_names[count]])

    return complete_headers

def create_columns_by_model(model, fields, header_names):

    field_names = [field.name for field in model._meta.fields]

    field_names = list(filter(lambda field_name: field_name in fields, field_names))

    complete_headers = []
    for count, field in enumerate(field_names):
        complete_headers.append([field, header_names[count]])

    return complete_headers

def create_model_by_instance(model, dictionary):
    model_fields = {f.name: f for f in model._meta.fields}
    foreign_keys = {f.name for f in model._meta.fields if isinstance(f, ForeignKey)}

    filtered_dictionary = {}
    for k, v in dictionary.items():
        try:
            if k in model_fields and k not in foreign_keys:
                filtered_dictionary[k] = v
            elif k.endswith('_id') and k[:-3] in foreign_keys:
                fk_model = model_fields[k[:-3]].related_model
                filtered_dictionary[k[:-3]] = fk_model.objects.get(pk=v)
            else: 
                fk_model = model_fields[k].related_model
                filtered_dictionary[k] = fk_model.objects.get(pk=v)
        except:
            pass
                
    obj = model.objects.create(**filtered_dictionary)
    
    return True

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def search_all_fields(model, objects, search_term, search_fk=True):
    fields = model._meta.get_fields()

    queries = []
    
    try:
        term = int(search_term)
        pk_field_name = model._meta.pk.name
        queries.append(Q(**{pk_field_name: term}))
    except (ValueError, TypeError):
        pass
    
    for field in fields:
        field_name = field.name
        if isinstance(field, CharField):
            queries.append(Q(**{f"{field_name}__icontains":search_term}))
        elif search_fk and field.is_relation and hasattr(field, "related_model") and issubclass(field.related_model, models.Model):
            related_fields = field.related_model._meta.get_fields()
            for related_field in related_fields:
                if isinstance(related_field, CharField):
                    related_field_name = f"{field_name}__{related_field.name}"
                    queries.append(Q(**{f"{related_field_name}__icontains":search_term}))
    if queries:
        query = queries.pop()

        for item in queries:
            query |= item

        return objects.filter(query).distinct()
    else: 
        return objects.all()

def update_model_with_dict(model_instance, dictionary):
    model_fields = {f.name: f for f in model_instance._meta.fields}
    foreign_keys = {f.name for f in model_instance._meta.fields if isinstance(f, ForeignKey)}

    filtered_dictionary = {}
    for k, v in dictionary.items():
        try:
            if k in model_fields and k not in foreign_keys:
                filtered_dictionary[k] = v
            elif k.endswith('_id') and k[:-3] in foreign_keys:
                fk_model = model_fields[k[:-3]].related_model
                setattr(model_instance, k[:-3], fk_model.objects.get(pk=v))
            elif k in foreign_keys:
                fk_model = model_fields[k].related_model
                setattr(model_instance, k, fk_model.objects.get(pk=v))
        except:
            pass

    for field, value in filtered_dictionary.items():
        try:
            setattr(model_instance, field, value)
        except:
            pass

    model_instance.save()
    return True
    
