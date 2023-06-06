from django.forms import ModelForm
from .models import Solicitud

class SolicitudForm(ModelForm):    
    class Meta:
        model = Solicitud
        fields = ['idsolicitud','descripcion','usuario_idusuario','estado', 'aprobacion_idaprobacion']
