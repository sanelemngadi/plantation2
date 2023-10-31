from django import forms
from appointments.models import PlantationAppointmentsModel

class PlantationAppointmentForm(forms.ModelForm):
    class Meta:
        model = PlantationAppointmentsModel
        fields = "__all__"

        exclude = ("user", "appointment_done", "price_per_sqm", "fumigator", "paid", "appointment_service_completed", "assigned")

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "fumigation_area": forms.NumberInput(attrs={"placeholder": "Total area in square meters"})
        }

class PlantationAssignUserForm(forms.ModelForm):
    class Meta:
        model = PlantationAppointmentsModel
        fields = ("fumigator",)