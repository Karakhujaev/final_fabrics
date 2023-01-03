# Generated by Django 4.1.3 on 2023-01-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics_main', '0007_auto_20221215_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregory',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='caregory',
            name='name_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='name_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Maxsulot nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Maxsulot nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='subject_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='subject_uz',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlovha'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlovha'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_uz',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='caregory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
