"""
    Модели приложения.
"""
from django.db import models

"""
"ownerName" type="string"
"serialNumber" type="uint64"
"modelYear" type="uint64"
"code" type="string"
"vehicleCode" type="string"
"engine"
    "capacity" type="uint16"
    "numCylinders" type="uint8"
    "maxRpm" type="uint16"
    "manufacturerCode" type="char"
"fuelFigures"
    "speed" type="uint16"
    "mpg" type="float"
    "usageDescription" type="string"
"performanceFigures"
    "octaneRating" type="uint16"
"acceleration"
    "mph" type="uint16"
    "seconds" type="float"
    "manufacturer" type="string"
    "model" type="string"
    "activationCode" type="string"
"""


class Engine(models.Model):
    """
        Модель двигателя
    """
    capacity = models.PositiveIntegerField(verbose_name='capacity')
    num_cylinders = models.PositiveSmallIntegerField(verbose_name='numCylinders')
    max_rpm = models.PositiveIntegerField(verbose_name='maxRpm')
    manufacturer_code = models.CharField(verbose_name='manufacturerCode', max_length=1)


class FuelFigures(models.Model):
    """
        Топливные характеристики
    """
    speed = models.PositiveIntegerField(verbose_name='speed')
    mpg = models.FloatField(verbose_name='mpg')
    usage_description = models.PositiveSmallIntegerField(verbose_name='usageDescription')


class PerformanceFigures(models.Model):
    """
        Характеристики мощности
    """
    octane_rating = models.PositiveSmallIntegerField(verbose_name='octaneRating')


class Acceleration(models.Model):
    """
        Скоростные характеристики
    """
    mph = models.PositiveSmallIntegerField(verbose_name='mph')
    seconds = models.FloatField(verbose_name='seconds')
    manufacturer = models.TextField(verbose_name='manufacturer')
    model = models.TextField(verbose_name='manufacturer')
    activation_code = models.TextField(verbose_name='activationCode')


class Car(models.Model):
    """
        Модель атомобиля
    """
    owner_name = models.TextField(verbose_name='ownerName')
    serial_number = models.PositiveSmallIntegerField(verbose_name='serialNumber')
    model_year = models.BigIntegerField(verbose_name='modelYear')
    code = models.TextField(verbose_name='code')
    vehicle_code = models.TextField(verbose_name='vehicleCode')
    engine = models.ForeignKey(Engine, on_delete=models.PROTECT, verbose_name='engine')
    fuel_figures = models.ForeignKey(FuelFigures, on_delete=models.PROTECT, verbose_name='fuelFigures')
    performance_figures = models.ForeignKey(
        PerformanceFigures, on_delete=models.PROTECT, verbose_name='performanceFigures')
    acceleration = models.ForeignKey(Acceleration, on_delete=models.PROTECT, verbose_name='acceleration')