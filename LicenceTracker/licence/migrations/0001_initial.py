# Generated by Django 4.1.1 on 2022-09-09 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LicenceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LicenceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='Guest', max_length=50)),
                ('comment', models.TextField(max_length=500)),
                ('purchase_date', models.DateField()),
                ('request_number', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('available_for_reallocation', models.BooleanField(default=False)),
                ('licence_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='licence.licencetype')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='licence.licencestatus')),
            ],
        ),
        migrations.RunSQL("INSERT INTO licence_licencetype (name) VALUES ('Microsoft Office'), ('Visual Studio Professional'), ('Resharper standard'), ('Resharper professional'), ('Resharper ultimate'), ('JetBrains'), ('Telerik UI for WPF'), ('Visual Studio Test Professional'), ('Visio'), ('Tableau');"),
        migrations.RunSQL("INSERT INTO licence_licencestatus (type) VALUES ('Assigned'), ('Unassigned'), ('Assignment in progress');"),
    ]
