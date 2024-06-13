from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class News(models.Model):
    author = models.ForeignKey(Author, default=1, on_delete=models.SET_DEFAULT,
                               verbose_name=pgettext_lazy('Author', 'Author'))
    type = models.CharField(max_length=7, choices=TYPE, verbose_name=pgettext_lazy('Type', 'Type'))
    time_in = models.DataTimeField(auto_now_add=True, verbose_name=pgettext_lazy('Time_in', 'Time_in'))
    category = models.ManyToManyField(Category, through='PostCategory',
                                      verbose_name=pgettext_lazy('Category', 'Category'))
    title = models.CharField(max_length=255, verbose_name=pgettext_lazy('Title', 'Title'))
    text = models.TextField(verbose_name=pgettext_lazy('Text', 'Text'))
    rating = models.IntegerField(default=0, verbose_name=pgettext_lazy('Rating', 'Rating'))


    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()