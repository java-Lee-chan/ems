from django import forms

from .models import Equipment


class EquipmentForm(forms.ModelForm):
    name = forms.CharField(
        label='设备名称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': "width: 60%;"}
        )
    )

    attribute = forms.CharField(
        label='设备属性',
        max_length=100,
        widget=forms.widgets.Textarea(
            attrs={'rows': 6, 'cols': 60, 'class': 'form-control'}
        )
    )

    class Meta:
        model = Equipment
        fields = ['name', 'zone', 'attribute', 'owner']

