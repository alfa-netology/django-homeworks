from django.db import models


class TimestampFields(models.Model):
    """ Базовый класс """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    """
    abstract=True Эта модель не будет использоваться для создания таблицы базы данных. 
    Вместо этого, когда класс используется в качестве базового класса для других моделей, 
    его поля будут добавлены к полям дочернего класса.
    """


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} - {self.project}"
