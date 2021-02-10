from django.db import models

class Author(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=200,unique = True)
    dob = models.CharField(max_length=200)

    class Meta:
        app_label = 'Quotes'

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=200,unique = True)
    def __str__(self):
        return self.tag_name


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote_text = models.CharField(max_length=200)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text


class QuoteJunction(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote