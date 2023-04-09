from rest_framework import renderers
import json 
class ResponseRender(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data,accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'success':False,'detail':'Ocurrió un error al realizar la acción','data': data})
        else:
            response = json.dumps({'success':True,'detail':'Acción realizada con éxito','data': data})
        return response