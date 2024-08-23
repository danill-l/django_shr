from django.db import models

# Create your models here.
# class Type(models.Model):

#     name = models.CharField(max_length=120, null=False)

#     def __str__(self):
#         return self.name


# class Mushroom(models.Model):

#     image = models.ImageField(upload_to='images/', null=True)
#     name = models.CharField(max_length=120, null=False)
#     latin = models.CharField(max_length=50, null=False)
#     syn = models.CharField(max_length=120, null=True)
#     description = models.TextField(null=False)
#     is_it_good = models.CharField(max_length=50, null=False)
#     type = models.ForeignKey('Type', on_delete=models.DO_NOTHING)

#     def __str__(self):
#         return self.name
    
# INSERT INTO "mushroom_list_type"(name)
# VALUES
# ('Съедобные грибы'),
# ('Условно-съедобные грибы'),
# ('Несъедобные грибы'),
# ('Ядовитые грибы');
# INSERT INTO mushroom_list_type(name)
# VALUES
# ('Съедобные грибы'),
# ('Условно-съедобные грибы'),
# ('Несъедобные грибы'),
# ('Ядовитые грибы');