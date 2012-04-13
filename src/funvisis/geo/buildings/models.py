# -*- coding: utf-8 -*-
from django.contrib.gis.db import models

# Create your models here.

class Building(models.Model):

    # Building identification and location
    name_or_number = models.CharField(
        max_length=50, verbose_name=u'Nombre o Nº')
    floors = models.IntegerField(verbose_name=u'Nº de pisos')
    semi_basements = models.IntegerField(verbose_name=u'Nº de semi-sótanos')
    basements = models.IntegerField(verbose_name=u'Nº de sótanos')
    state = models.CharField(max_length=50, verbose_name=u'Estado')
    city = models.CharField(max_length=100, verbose_name=u'Ciudad')
    municipality = models.CharField(
        max_length=100, verbose_name=u'Municipio')
    parish = models.CharField(max_length=100, verbose_name=u'Parroquia')
    urbanization = models.CharField(
        max_length=100, verbose_name=u'Urb., Barrio')
    sector = models.CharField(
        max_length=100, verbose_name=u'Sector')
    street = models.CharField(
        max_length=100, verbose_name=u'Calle, Vereda, otro', blank=True)
    square = models.CharField(
        max_length=100, verbose_name=u'Manzana Nº', blank=True)
    plot = models.CharField(
        max_length=100, verbose_name=u'Nº Parcela', blank=True)
    #coord_x = models.FloatField(
    #    verbose_name=u'4.13 Coord. X', null=True, blank=True)
    #coord_y = models.FloatField(
    #    verbose_name=u'4.14 Coord. Y', null=True, blank=True)
    #time_zone = models.IntegerField(verbose_name=u'Huso')
    location = models.PointField(srid=4368, verbose_name=u'Ubicación geográfica')
    
    
    # Building usage    
    governmental = models.BooleanField(verbose_name=u'Gubernamental')
    firemen = models.BooleanField(verbose_name=u'Bomberos')
    civil_defense = models.BooleanField(verbose_name=u'Protección Civil')
    police = models.BooleanField(verbose_name=u'Policial')
    military = models.BooleanField(verbose_name=u'Militar')
    popular_housing = models.BooleanField(verbose_name=u'Vivienda Popular')
    single_family = models.BooleanField(verbose_name=u'Vivienda Unifamiliar')
    multifamily = models.BooleanField(verbose_name=u'Vivienda Multifamiliar')

    medical_care = models.BooleanField(verbose_name=u'Médico-Asistencial')
    educational = models.BooleanField(verbose_name=u'Educativo')
    sports_recreational = models.BooleanField(
        verbose_name=u'Deportivo-Recreativo')
    cultural = models.BooleanField(verbose_name=u'Cultural')

    industrial = models.BooleanField(verbose_name=u'Industrial')
    commercial = models.BooleanField(verbose_name=u'Comercial')
    office = models.BooleanField(verbose_name=u'Oficina')
    religious = models.BooleanField(verbose_name=u'Religioso')

    other = models.CharField(
        verbose_name=u'Otro (Especifique)', max_length='50', blank=True)


    # Building age    
    year = models.IntegerField(
        verbose_name=u'Año de construcción', null=True, blank=True)
    year_range = models.CharField(
        max_length=20, verbose_name = u'Rango del año de construcción',
        choices=(
            ('<1939', 'Antes de 1939'),
            ('[1940, 1947]', 'Entre 1940 y 1947'),
            ('[1948, 1955]', 'Entre 1948 y 1955'),
            ('[1956, 1967]', 'Entre 1956 y 1967'),
            ('[1968, 1982]', 'Entre 1968 y 1982'),
            ('[1983, 1998]', 'Entre 1983 y 1998'),
            ('[1999, 2001]', 'Entre 1999 y 2001'),
            ('>2001', 'Después de 2001'),))
    
    # Ground conditions    
    building_at = models.CharField(
        max_length='10', verbose_name=u'Edificación en',
        choices=(
            ('planicie', 'Planicie'),
            ('ladera', 'Ladera'),
            ('base', 'Base'),
            ('cima', 'Cima'),))

    # 32.5 means (20º - 45º)
    # 67.5 means > 45º
    ground_slope = models.CharField(
        max_length='10', verbose_name=u'Pendiente del terreno',
        choices=(
            ('[20, 45]', '20º - 45º'),
            ('>45', 'Mayor a 45º'),),
        blank=True)
    ground_over = models.BooleanField(
        verbose_name=u'Localizada sobre la mitad superior de la ladera',
        choices=(
            (True, u'Sí'),
            (False, u'No')))
    talus_slope = models.CharField(
        max_length='10', verbose_name=u'Pendiente del talud',
        choices=(
            ('[20, 45]', '20º - 45º'),
            ('>45', 'Mayor a 45º'),), # Al limpiar la base de datos,
                                     # cambiar el promedio por los
                                     # rangos adecuados.
        blank=True)
    talus_separation_gt_H = models.BooleanField(
        verbose_name=u'Separación al talud',
        choices=(
            (False, 'Menor a H del Talud'),
            (True, 'Mayor a H del Talud')))
    drainage = models.BooleanField(
        verbose_name=u'Drenajes',
        choices=(
            (True, u'Sí'),
            (False, u'No')))

    # 9. Structural type    
    gates_of_concrete = models.BooleanField(
        verbose_name=u'Pórticos de concreto armado')
    gates_of_concrete_block_walls_filled_with_clay_concrete = \
        models.BooleanField(
        verbose_name=u'Pórticos de concreto armado rellenos con paredes' \
            ' de bloques de arcilla de concreto')
    reinforced_concrete_walls_in_two_horizontal_directions = \
        models.BooleanField(
        verbose_name=u'Muros de concreto armado en dos direcciones horizontales')
    systems_with_reinforced_concrete_walls_in_one_direction = \
        models.BooleanField(
        verbose_name=u'Sistemas con muros de concreto' \
            u' armado en una sola dirección, como algunos sistemas del tipo túnel')
    steel_frames = models.BooleanField(
        verbose_name=u'Pórticos de acero')
    steel_frames_with_hollow = models.BooleanField(
        verbose_name=u'Pórticos de acero con perfiles tabulares')
    diagonalized_steel_frames = models.BooleanField(
        verbose_name=u'Pórticos diagonalizados')
    gates_of_steel_trusses = models.BooleanField(
        verbose_name=u'Pórticos de acero con cerchas')
    pre_built_systems_based_on_large_panels_or_frames = models.BooleanField(
        verbose_name=u'Sistemas pre-fabricados a base de' \
            u' grandes paneles o de pórticos')
    confined_load_bearing_mosonry = models.BooleanField(
        verbose_name=u'Sistemas cuyos elementos portantes' \
            u'sean mampostería confinada')
    confined_load_bearing_mosonry_floors = models.IntegerField(
        verbose_name=u'Pisos', blank=True, null=True)
    not_confined_load_bearing_masonry = models.BooleanField(
        verbose_name=u'Sistemas cuyos elementos portantes' \
            u' sean muros de mampostería no confinada')
    not_confined_load_bearing_mosonry_floors = models.IntegerField(
        verbose_name=u'Pisos', blank=True, null=True)
    mixed_systems_frames_bearing_mosonry = models.BooleanField(
        verbose_name=u'Sistemas  mixtos de pórticos y de' \
            u' mampostería de baja calidad de construcción.')
    mixed_systems_frames_bearing_mosonry_floors = models.IntegerField(
        verbose_name=u'Pisos', blank=True, null=True)
    one_floor_adobe_house = models.BooleanField(
        verbose_name=u'Viviendas de bahareque de un piso')
    precarious_housing = models.BooleanField(
        verbose_name=u'Viviendas de construcción precaria' \
            u'(tierra, madera, zinc, etc.)')


    # 10. Floor scheme
    floor_scheme = models.CharField(
        verbose_name=u'', max_length='20',
        choices=(
            ('H', u'H'),
            ('T', u'T'),
            ('U o C', u'U ó C'), 
            ('L', u'L'),
            ('cajon', u'Cajón'),
            ('regular', u'Regular'),
            ('esbeltez horizontal', u'Esbeltez horizontal'),
            ('ninguno', u'Ninguno'),),
        blank=False)

    # 11. Lifting scheme
    lifting_scheme = models.CharField(
        verbose_name=u'', max_length=20,
        choices=(
            ('T', u'T'),
            (u'pirámide invertida', u'Pirámide invertida'),
            ('piramidal', u'Piramidal'),
            ('U', 'U'),
            ('L', u'L'),
            ('rectangular', u'\u25AF'),
            ('esbeltez vertical', u'Esbeltez, vertical'),
            ('ninguno', u'Ninguno'),),
        blank=False)
        
    # 12. Irregularities
    no_high_beams_on_one_or_two_directions = models.BooleanField(
        verbose_name=u'Ausencia de vigas altas en una o dos direcciones')
    presence_of_at_least_one_soft_or_weak_mezzanine = models.BooleanField(
        verbose_name=u'Presencia de al menos un entrepiso débil o blando')
    presence_of_short_columns = models.BooleanField(
        verbose_name=u'Presencia de columnas cortas')
    discontinuity_lines_of_columns = models.BooleanField(
        verbose_name=u'Discontinuidad de ejes de columnas')
    significant_openings_in_slabs = models.BooleanField(
        verbose_name=u'Aberturas significativas en losas')
    strong_asymmetry_in_plant_mass_or_stiffness = models.BooleanField(
        verbose_name=u'Fuerte asimetría de masas o rigideces en planta')
    one_direction_wall_abscense = models.BooleanField(
        verbose_name=u'Ausencia de muros en una dirección')
    attaching_slab_slab = models.BooleanField(
         verbose_name='12.8 Adosamiento: Losa contra losa') # REVISAR
    attaching_slab_column = models.BooleanField(
         verbose_name='12.9 Adosamiento: Columna contra losa') # REVISAR
    #attaching_slab_slab_column = models.CharField(
    #    max_length=15,
    #    verbose_name=u'Tipo de adosamiento',
    #    choices=(
    #        ('ninguno', 'Ninguno'),
    #        ('slab_slab', 'Losa contra losa'), # Limpiar la base de
                                               # datos para cambiar
                                               # slab_slab a losa
                                               # contra losa
    #        ('column_slab', 'Columna contra losa'),))
    separation_between_buildings = models.IntegerField(
        verbose_name=u'Separación entre edificios (cm)',
        help_text='Colocar algun valor, así sea cero (0)',
        null=True,
        blank=True
        )
