from django.shortcuts import render, redirect
from .forms import SaleServiceForm

# def crear_venta_servicio(request):
#     if request.method == 'POST':
#         form = SaleServiceForm(request.POST)
#         if form.is_valid():
#             servicio = form.save()
#             servicio.enviar_correo_venta_servicio()  # Aquí se llama al método para enviar el correo electrónico
#             return redirect('pagina_exitosa')  # Redirecciona a una página de éxito o a donde desees
#     else:
#         form = SaleServiceForm()
#     return render(request, 'formulario_venta_servicio.html', {'form': form})

# def crear_venta_servicio(request):
#     if request.method == 'POST':
#         form = SaleServiceForm(request.POST)
#         if form.is_valid():
#             servicio = form.save()
#             # No colocar la llamada al método enviar_correo_venta_servicio dentro del bloque if
#             # de form.is_valid() para asegurar que el correo se envíe incluso si hay un error en el guardado del formulario
#             servicio.enviar_correo_venta_servicio()
#             return redirect('pagina_exitosa')  # Redirecciona a una página de éxito o a donde desees
#     else:
#         form = SaleServiceForm()
#     return render(request, 'formulario_venta_servicio.html', {'form': form})
