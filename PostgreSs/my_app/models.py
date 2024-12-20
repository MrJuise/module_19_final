from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'my_app_user'

class PgAdminTable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    other = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'pg_admin_table'


class PgDb(models.Model):
    title = models.CharField(max_length=30)
    deskription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'pg_db'