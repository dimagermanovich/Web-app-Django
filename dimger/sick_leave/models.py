from django.db import models



class tableIncapables(models.Model):
    lastName = models.CharField('Фамилия', max_length=50)
    firstName = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=50)

    def get_absolute_url(self):
        return f'/sick_leave/incapable/{self.id}'

    def __str__(self):
        return self.lastName + " " + self.firstName + " " + self.patronymic


class table(models.Model):
    incapable = models.ForeignKey(tableIncapables, on_delete=models.CASCADE)
    number_of_list = models.IntegerField('Номер листка нетрудоспособного', max_length=12)
    name_of_organization = models.CharField('Название организации', max_length=50)
    work = models.CharField('Должность', max_length=50)
    ache = models.CharField('Болезнь',  max_length=100)
    begin_date = models.DateField('Начало больничного')
    end_date = models.DateField('Конец больничного')

    def __str__(self):
        return self.ache


    def get_absolute_url(self):
        return f'/sick_leave/{self.id}'





