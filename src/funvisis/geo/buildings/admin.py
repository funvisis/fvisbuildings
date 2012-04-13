from .models import Building
from django.contrib import admin

import floppyforms as forms

class CustomPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    map_width = 800
    map_height = 400
    #map_srid = 900913  # Use the google projection
    #template_name = 'forms/google_map.html'
    default_lon = 66.90
    default_lat = 10.50
    mouse_position = True

    class Media:
        js = (
            'http://openlayers.org/dev/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
            'http://maps.google.com/maps/api/js?sensor=false',
        )

class BuildingForm(forms.ModelForm):
    location = forms.gis.PointField(widget=CustomPointWidget)
    class Meta:
        model = Building
        #exclude = ("content_type","object_id")
#    class Media:
#        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)
#    formfield_overrides = {
#        models.TextField: {'widget': RichTextEditorWidget},
#    }

    class Meta:
        model = Building
#        exclude = ['name']


class BuildingAdmin(admin.ModelAdmin):
    form = BuildingForm

admin.site.register(Building, BuildingAdmin)
