from django.db import models

from vehicles.models import Vehicle


class ParkingSpot(models.Model):
    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
    spot_number = models.CharField(max_length=15, unique=True, verbose_name='Número da Vaga')
    is_occupied = models.BooleanField(default=False, verbose_name='Ocupado')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.spot_number


class ParkingRecord(models.Model):
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo'
    )

    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga'
    )

    entry_time = models.DateTimeField(auto_now_add=True, verbose_name='Hora de Entrada')
    exit_time = models.DateTimeField(blank=True, null=True, verbose_name='Hora de Saída')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot}'
