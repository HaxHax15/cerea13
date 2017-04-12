from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Region(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class City(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Street(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"


class Place(models.Model):
    country = models.ForeignKey(Country, verbose_name="Страна")
    region = models.ForeignKey(Region, verbose_name="Регион")
    city = models.ForeignKey(City, verbose_name="Город")
    street = models.ForeignKey(Street, verbose_name="Улица")
    house = models.CharField(max_length=6, blank=False, null=False, unique=True, verbose_name="Дом")
    building = models.CharField(max_length=4, blank=True, null=True, unique=True, verbose_name="Строение")
    apartments = models.CharField(max_length=6, blank=True, null=True, unique=True, verbose_name="Квартира")
    latitude = models.CharField(max_length=16, blank=True, null=True, unique=True, verbose_name="Широта")
    longitude = models.CharField(max_length=16, blank=True, null=True, unique=True, verbose_name="Долгота")
    description = models.TextField(verbose_name="Описание", max_length=64, blank=False, null=False)

    def __str__(self):
        string = str(self.country)+', '+str(self.region)+', '+str(self.city)+', '+str(self.street)+', '+str(self.house)
        if self.building is not None:
            string = string+', корп. '+str(self.building)
        if self.apartments is not None:
            string = string+', кв. '+str(self.apartments)

        return string

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
