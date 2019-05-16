import csv
import codecs
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Equipment
from .models import Zone
from .forms import EquipmentForm


# Create your views here.
def equipment_list(request, zone_id=None):
    if zone_id:
        try:
            zone = Zone.objects.get(id=zone_id)
        except Zone.DoesNotExist:
            equip_list = []
        else:
            equip_list = zone.equipment_set.all()
    else:
        equip_list = Equipment.objects.all()

    return render(request, 'equipment/list.html', context={'equip_list': equip_list})


def equipment_detail(request, equip_id=None):
    try:
        equip = Equipment.objects.get(id=equip_id)
    except Equipment.DoesNotExist:
        equip = None
    return render(request, 'equipment/detail.html', context={'equip': equip})


def equipment_inc(request):

    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            zone = form.cleaned_data['zone']
            attribute = form.cleaned_data['attribute']
            owner = form.cleaned_data['owner']
            equip = Equipment(name=name, zone=zone, attribute=attribute, owner=owner)
            equip.save()
            return HttpResponseRedirect('/')

    else:
        form = EquipmentForm()

    return render(request, 'equipment/inc.html', {'form': form})


def equipment_detail_upload(request):

    pass


def equipment_detail_download(request):

    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="equipment_detail.csv"'

    writer = csv.writer(response)
    row = Equipment.get_row()
    for i in range(len(row)):
        writer.writerow(row[i])

    return response



