# -*- coding: utf-8 -*-

from .models import Building
from django.contrib import admin

from fvislib.utils.decorators import conditional_fieldsets

#import floppyforms as forms

#class CustomPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    #map_width = 800
    #map_height = 400
    #map_srid = 900913  # Use the google projection
    #template_name = 'forms/google_map.html'
    #default_lon = 66.90
    #default_lat = 10.50
    #mouse_position = True

    #class Media:
        #js = (
            #'http://openlayers.org/dev/OpenLayers.js',
            #'floppyforms/js/MapWidget.js',
            #'http://maps.google.com/maps/api/js?sensor=false',
        #)

#class BuildingForm(forms.ModelForm):
    #location = forms.gis.PointField(widget=CustomPointWidget)
    #class Meta:
        #model = Building
        #exclude = ("content_type","object_id")
#    class Media:
#        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)
#    formfield_overrides = {
#        models.TextField: {'widget': RichTextEditorWidget},
#    }

#    class Meta:
#        model = Building
#        exclude = ['name']

@conditional_fieldsets
class BuildingAdmin(admin.ModelAdmin):

    fieldsets_base = (
        (
            u'Identificación y ubicación del edificio',
            {
                'fields': (
                    'name_or_number',
                    'floors',
                    'semi_basements',
                    'basements',
                    'state',
                    'city',
                    'municipality',
                    'parish',
                    'urbanization',
                    'sector',
                    'street',
                    'square',
                    'plot',
                    'location',
                    #'coord_x',
                    #'coord_y',
                    )}),
        (
            u'Uso de la edificación',
            {
                'fields': (
                    'governmental',
                    'firemen',
                    'civil_defense',
                    'police',
                    'military',
                    'popular_housing',
                    'single_family',
                    'multifamily',
                    'medical_care',
                    'educational',
                    'sports_recreational',
                    'cultural',
                    'industrial',
                    'commercial',
                    'office',
                    'religious',
                    'other')}),
        (
            u'Año de la construcción', {
                'fields': (
                    'year',
                    'year_range')}),
        (
            u'Condición del terreno',
            {
                'fields':
                    ('building_at',
                     'ground_slope',
                     'ground_over',
                     'talus_slope',
                     'talus_separation_gt_H',
                     'drainage')}),
        (
            u'Tipo estructural',
            {
                'fields': (
                    'gates_of_concrete',
                    'gates_of_concrete_block_walls_filled_with_clay_concrete',
                    'reinforced_concrete_walls_in_two_horizontal_directions',
                    'systems_with_reinforced_concrete_walls_in_one_direction',
                    'steel_frames',
                    'steel_frames_with_hollow',
                    'diagonalized_steel_frames',
                    'gates_of_steel_trusses',
                    'pre_built_systems_based_on_large_panels_or_frames',
                    'confined_load_bearing_mosonry',
                    'confined_load_bearing_mosonry_floors',
                    'not_confined_load_bearing_masonry',
                    'not_confined_load_bearing_mosonry_floors',
                    'mixed_systems_frames_bearing_mosonry',
                    'mixed_systems_frames_bearing_mosonry_floors',
                    'one_floor_adobe_house',
                    'precarious_housing',)}),
        (
            u'Esquema de planta',
            {
                'fields': (
                    'floor_scheme',)}),
        (
            u'Esquema de elevación',
            {
                'fields': (
                    'lifting_scheme',)}),

        (
            u'Irregularidades',
            {
                'fields': (
                    'no_high_beams_on_one_or_two_directions',
                    'presence_of_at_least_one_soft_or_weak_mezzanine',
                    'presence_of_short_columns',
                    'discontinuity_lines_of_columns',
                    'significant_openings_in_slabs',
                    'strong_asymmetry_in_plant_mass_or_stiffness',
                    'one_direction_wall_abscense',
                    'attaching_slab_slab',
                    'attaching_slab_column',
                    'separation_between_buildings',)}),
        )

    fieldsets_super = ()

    conditioned_fieldsets = [
        (
            lambda request: True,
            fieldsets_base),

        (
            lambda request: \
                request.user.is_superuser or \
                request.user.groups.filter(name="supervisores") or \
                request.user.groups.filter(name="revisores"),
            fieldsets_super),
        ]

    def usage_list_display(self, obj):
        text_length = 50
        usage_fields = [
            'governmental',
            'firemen',
            'civil_defense',
            'police',
            'military',
            'popular_housing',
            'single_family',
            'multifamily',
            'medical_care',
            'educational',
            'sports_recreational',
            'cultural',
            'industrial',
            'commercial',
            'office',
            'religious',]
        result = ', '.join(
            [
                Building._meta.get_field(_).verbose_name
                for _ in usage_fields
                if getattr(obj, _)] + [obj.other])

        return result

    list_display = (
        'city',
        'urbanization',
        'usage_list_display',
        )

    # list_filter = (
    #      'inspector',
    #     'city',)

    search_fields = [
        '=city',
        'urbanization']

    def save_model(self, request, obj, form, change): # The logged
                                                      # user is going
                                                      # to be the
                                                      # inspector
        if not change: # Only adding sets the inspector
            obj.inspector = request.user.fvisuser
        obj.save()

    def queryset(self, request):

        if request.user.groups.filter(name='supervisores') or \
                request.user.is_superuser:
            return Building.objects.all()

        return Building.objects.filter(inspector=request.user.fvisuser)


    class Media:
        js = ('js/admin/custom.js', )

