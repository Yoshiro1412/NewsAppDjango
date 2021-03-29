from django.db import models

# Create your models here.
class Articulo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/',null=True)

    class Meta:
        abstract = True

class Noticia(Articulo):
    date = models.DateField()

    def __str__(self):
        return self.title

class Proyecto(Articulo):
    STATES = (
        ('P','In Progress'),
        ('F','Finished'),
    )

    TOPICS = (
        ('Waste','Waste'),
        ('Economy','Economy'),
    )
    state = models.CharField(max_length=1,choices=STATES)
    main_topic = models.CharField(max_length=10,choices=TOPICS)

    def __str__(self):
        return self.title

