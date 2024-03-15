from django.shortcuts import render 
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
from garantias.models import Garantia

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from inventario.models import Product
from garantias.models import ServicioConGarantia
from clienteAtencion.models import cite, contacts

from sesiones.forms import CiteForm

from .utils import is_admin_or_empleado, is_cliente


def inicio(request):
    return render(request, 'inicio.html', {
        #context
    })

@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def agendar(request):
    user_cites = cite.objects.filter(user=request.user)
    #user_vehicles = Vehicle.objects.filter(user=request.user)
    #servicios = Service.objects.all()
    return render(request, 'agendar.html', {'cites': user_cites})

def asignarR(request):
    return render(request, 'asignarR.html', {
        #context
    })

@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def contactos(request):
    contactos = contacts.objects.all()
    return render(request, 'contactos.html', {'contactos': contactos})
    
@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def crear_cita(request):
    services = ServicioConGarantia.objects.all()
    user = request.user  # Obtener el usuario autenticado

    # Obtener los datos del usuario actualmente autenticado
    user_data = {
        'client_name': user.first_name,  # Suponiendo que el nombre de usuario es el nombre del cliente
        'client_email': user.email,
        'client_id': user.identification,
        # Completa los otros campos del usuario según sea necesario
    }

    if request.method == 'POST':
        form = CiteForm(request.POST)
        if form.is_valid():
            cite = form.save(commit=False)
            cite.user = request.user
            
            # Obtener la fecha y la hora seleccionadas por el usuario
            datetime_selected = form.cleaned_data['date']
            time_selected = form.cleaned_data['time']

            # Calcular la hora de finalización de la cita
            end_time = datetime_selected + timedelta(hours=1)

            if cite.__class__.objects.filter(date=datetime_selected, time__hour=time_selected.hour).exists():
                form.add_error('time', "Ya hay una cita agendada en esta hora. Por favor, selecciona otra hora.")
            else:
                cite.save()
                return redirect('agendar')
        else:
            form = CiteForm(request.POST or None)  # Pasa los datos iniciales si el formulario no es válido
    else:
        form = CiteForm(initial=user_data)
    return render(request, 'crear_cita.html', {'form': form, 'services': services})


def eliminar_cita(request, cita_id):
    cita = get_object_or_404(cite, id=cita_id)

    if request.method == 'POST':
        cita.delete()
        return redirect('agendar')  # Redirigir a donde quieras después de eliminar la cita

    return render(request, 'eliminar_cita.html', {'cita': cita})

@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def reagendar_cita(request, cita_id):
    services = ServicioConGarantia.objects.all()
    cita = get_object_or_404(cite, id=cita_id)
    user = request.user

    if request.method == 'POST':
        form = CiteForm(request.POST)
        if form.is_valid():
            new_cite = form.save(commit=False)
            new_cite.user = user

            datetime_selected = form.cleaned_data['date']
            time_selected = form.cleaned_data['time']

            # Calcular la hora de finalización de la cita
            end_time = datetime_selected + timedelta(hours=1)

            if cite.objects.filter(date=datetime_selected, time__hour=time_selected.hour).exclude(id=cita.id).exists():
                form.add_error('time', "Ya hay una cita agendada en esta hora. Por favor, selecciona otra hora.")
            else:
                cita.delete()  # Eliminar la cita original
                new_cite.save()  # Guardar la nueva cita
                return redirect('agendar')
    else:
        # Obtener los datos iniciales del formulario
        initial_data = {
            'client_name': cita.client_name,
            'client_email': cita.client_email,
            'client_id': cita.client_id,
            'brand': cita.brand,
            'year': cita.year,
            'model': cita.model,
            'color': cita.color,
            'plate_number': cita.plate_number,
            'notes': cita.notes,
            'service': cita.service,
            'date': cita.date,
            'time': cita.time,
        }
        form = CiteForm(initial=initial_data)

    return render(request, 'reagendar_cita.html', {'form': form, 'services': services})


def contactosInicio(request):
    return render(request, 'contactosInicio.html', {
        #context
    })
    
    
def index(request):
    return render(request, 'index.html', {
        #context
    })
    
def indexr(request):
    return render(request, 'indexr.html', {
        #context
    })
    
@login_required
@user_passes_test(is_cliente, login_url='/login/')    
def Menu(request):
    return render(request, 'Menu.html', {
        #context
    })
    
def menuAdmin(request):
    return render(request, 'MenuAdmin.html', {
        #context
    })

@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def ver_inventario(request):
    productos = Product.objects.all()
    return render(request, 'ver_inventario.html', {'productos': productos})
    # return render(request, 'ver_inventario.html', {
    #     #context
    #})
    

@login_required
@user_passes_test(is_cliente, login_url='/login/') 
def ver_servicios(request):
    servicios = ServicioConGarantia.objects.all()
    return render(request, 'ver_servicios.html', {'servicios': servicios})





class ReporteGarantiaPDF(View):
    def get(self, request, *args, **kwargs):
        # Obtener parámetros de filtro desde la solicitud
        fecha_vencimiento = request.GET.get('fecha_vencimiento', None)
        estados = request.GET.get('estados', None)

        # Construir la consulta de base de datos con los filtros aplicados
        queryset = Garantia.objects.all()
        if fecha_vencimiento:
            queryset = queryset.filter(fecha_vencimiento=fecha_vencimiento)
        if estados:
            queryset = queryset.filter(estados=estados)

        # Obtener todas las garantías según los filtros aplicados
        garantias = queryset

        # Cargar la plantilla HTML
        template_path = 'reporte-garantias-pdf.html'  # Asegúrate de que coincida con el nombre de tu template
        template = get_template(template_path)
        context = {'garantias': garantias}

        # Crear el objeto HttpResponse con las cabeceras de PDF adecuadas.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="informe_garantias.pdf"'

        # Generar el PDF utilizando xhtml2pdf
        pisa_status = pisa.CreatePDF(template.render(context), dest=response)

        # Si el PDF se generó correctamente, devuelve la respuesta
        if pisa_status.err:
            return HttpResponse('Error al generar el PDF', status=500)
        return response