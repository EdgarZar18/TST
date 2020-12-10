from django.db import models

class Registro(models.Model):
        nombres_aparato = (
        ('ABRELATA','abrelata'),
        ('ARROCERA','arrocera'),
        ('ASADOR','asador'),
        ('ASPIRADORA','aspiradora'),
        ('BANO_MARIA','bano_maria'),
        ('BASCULA','bascula'),
        ('BATERIA','bateria'),
        ('BATIDORA','batidora'),
        ('CAFETERA','cafetera'),
        ('CAFETERA','cafetera'),
        ('CALEFACTOR','calefactor'),
        ('CALENTADOR_BIBERONES','calentador_biberones'),
        ('CEPILLO_VAPOR','cepillo_vapor'),
        ('CHOCOMILERO','chocomilero'),
        ('CUCHILLO_ELECTRICO','cuchillo_electrico'),
        ('DEPILADORA','depiladora'),
        ('DESPACHADOR_AGUA','despachador_agua'),
        ('EMPACADORA_VACIO','empacadora_vacio'),
        ('ENFRIADOR_AGUA','enfriador_agua'),
        ('ENFRIADOR_VINOS','enfriador_vinos'),
        ('ENFRIDADOR_CERVEZA','enfridador_cerveza'),
        ('ESPUMADOR_LECHE','espumador_leche'),
        ('EXPRIMIDOR_JUGOS','exprimidor_jugos'),
        ('EXTRACTOR_JUGO','extractor_jugo'),
        ('FABRICA_HIELO','fabrica_hielo'),
        ('FOODSAVER','foodsaver'),
        ('FRAZADA_CALENTAMIENTO','frazada_calentamiento'),
        ('FREIDORA','freidora'),
        ('FUENTE_CHOCOLATE','fuente_chocolate'),
        ('GENERADOR_VAPOR','generador_vapor'),
        ('GRANITERA','granitera'),
        ('HERVIDOR_AGUA','hervidor_agua'),
        ('HIDROLAVADORA','hidrolavadora'),
        ('HORNO_GAS','horno_gas'),
        ('HORNO_ELECTRICO','horno_electrico'),
        ('LICUADORA','licuadora'),
        ('MAQUINA_HELADOS','maquina_helados'),
        ('MAQUINA_RASPADOS','maquina_raspados'),
        ('MICROONDAS','microondas'),
        ('MOLINO_CAFE','molino_cafe'),
        ('MOLINO_CARNE','molino_carne'),
        ('MOTOR_BRIDA_C','motor_brida_c'),
        ('MOTOR_USO_GRAL','motor_uso_gral'),
        ('NO_BREAK','no_break'),
        ('OLLA_EXPRESS','olla_express'),
        ('OLLA_MULTIUSOS','olla_multiusos'),
        ('PALOMERA','palomera'),
        ('PANERA','panera'),
        ('PANINI','panini'),
        ('PARRILLA','parrilla'),
        ('PICADORA','picadora'),
        ('PLANCHA','plancha'),
        ('PLANCHA_CABELLO','plancha_cabello'),
        ('PROCESADOR_ALIMENTOS','procesador_alimentos'),
        ('PULIDORA','pulidora'),
        ('PURIFICADOR_AIRE','purificador_aire'),
        ('RASURADORA','rasuradora'),
        ('REBANADORA','rebanadora'),
        ('REGULADOR_VOLTAJE','regulador_voltaje'),
        ('ROSTISERO','rostisero'),
        ('SANDWICHERAS','sandwicheras'),
        ('SARTEN_ELECTRICO','sarten_electrico'),
        ('SECADORA','secadora'),
        ('TETERA','tetera'),
        ('TOSTADOR','tostador'),
        ('TURBO_BATIDOR','turbo_batidor'),
        ('VAPORERA','vaporera'),
        ('VASO_LICUADORA','vaso_licuadora'),
        ('VENTILADOR','ventilador'),
        ('VITRINA','vitrina'),
        ('WAFFLERA','wafflera'),
        ('OTROS','otros'),
        )
    
        tipos_de_servicio = (('GARANTIA','garantia'),('COSTO','costo'),)

        estado_aparato = (
            ('RAYADO','rayado'),
            ('ROTO','ROTO'),
            ('ACCESORIOS_COMPLETOS','accesorios completos'),
            ('GOLPEADO','golpeado'),
            ('SUCIO','sucio'),
        )

        nombre = models.CharField(max_length=100, verbose_name="nombre")
        apellido = models.CharField(max_length=100, verbose_name="apellido")
        direcccion = models.CharField(max_length=100, verbose_name="direccion")
        colonia = models.CharField(max_length=60, verbose_name="colonia")
        estado = models.CharField(max_length=40, verbose_name="estado")
        telefono = models.CharField(max_length=10, verbose_name="telefono")
        celular = models.CharField(max_length=10, verbose_name="celular")
        correo = models.EmailField(max_length=60, verbose_name="correo")
        aparato = models.CharField(max_length=80, verbose_name="aparato", choices=(nombres_aparato))
        marca = models.CharField(max_length=50, verbose_name="marca")
        modelo = models.CharField(max_length=50, verbose_name="modelo")
        tipo_servicio = models.CharField(max_length=50,choices=tipos_de_servicio)
        descripcion_falla = models.TextField(max_length=1000, verbose_name="descripcion_falla")
        #evidencia_falla =models.ImageField(verbose_name="evidencia_falla",upload_to="servicios")
        observaciones = models.CharField(max_length=1000, verbose_name="observaciones")
        #ticket_compra =models.ImageField(verbose_name="ticket_compra",upload_to="servicios")
        created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")

