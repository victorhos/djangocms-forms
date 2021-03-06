# Generated by Django 2.2.12 on 2020-05-21 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0005_formfield_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_forms_formdefinition', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='formdefinition',
            name='form_template',
            field=models.CharField(blank=True, choices=[('djangocms_forms/form_template/bootstrap.html', 'Bootstrap'), ('djangocms_forms/form_template/default.html', 'Default')], default='djangocms_forms/form_template/bootstrap.html', max_length=150, verbose_name='Form Template'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('textarea', 'Text Area'), ('email', 'Email'), ('number', 'Number'), ('phone', 'Phone'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkbox_multiple', 'Multi Checkbox'), ('select', 'Drop down'), ('radio', 'Radio'), ('file', 'File Upload'), ('date', 'Date'), ('time', 'Time'), ('password', 'Password'), ('hidden', 'Hidden')], default='text', max_length=100, verbose_name='Field Type'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
    ]
