from django.db import models


class Historia(models.Model):
    PENDIENTE = 'pendiente'
    APROBADA = 'aprobada'
    USADA = 'usada'
    RECHAZADA = 'rechazada'

    ESTADO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (APROBADA, 'Aprobada'),
        (USADA, 'Usada en teatro'),
        (RECHAZADA, 'Rechazada'),
    ]

    nombre = models.CharField(max_length=150, blank=True, default='')
    titulo = models.CharField(max_length=300, default='')
    lugar_origen = models.CharField(max_length=200)
    tradicion = models.TextField(default='')
    historia = models.TextField()
    personajes = models.CharField(max_length=300)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=PENDIENTE)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_envio']

    def __str__(self):
        nombre_display = self.nombre or 'Anónimo'
        return f"{nombre_display} - {self.lugar_origen} ({self.estado})"
