# Generated by Django 4.2.3 on 2023-07-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Unnamed", max_length=100)),
                ("profile_pic", models.ImageField(blank=True, null=True, upload_to="")),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("occupation", models.CharField(blank=True, max_length=100, null=True)),
                ("birth_date", models.DateField(null=True)),
                ("is_married", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]