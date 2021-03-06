# Generated by Django 3.1.4 on 2021-01-13 02:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('building', models.CharField(blank=True, max_length=50, verbose_name='Building and Street')),
                ('street', models.CharField(blank=True, max_length=50, verbose_name='Street')),
                ('town', models.CharField(blank=True, max_length=50, verbose_name='Town')),
                ('county', models.CharField(blank=True, max_length=50, verbose_name='County')),
                ('postcode', models.CharField(blank=True, max_length=10, verbose_name='Postcode')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('property_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('loan_amount', models.IntegerField(verbose_name='Loan Amount')),
                ('property_value', models.IntegerField(verbose_name='Property Value')),
                ('mortgage_type', models.CharField(choices=[('NH', 'New House'), ('RM', 'Remortgage')], default='NH', max_length=2, verbose_name='Mortgage Type')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='initial_enquiry.address')),
                ('personal_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last Name')),
                ('telephone_number', models.CharField(max_length=25, verbose_name='Telephone Number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('preferred_time_to_contact', models.CharField(choices=[('M', '9am - 12pm (Mon-Fri)'), ('EA', '12pm - 3pm (Mon-Fri)'), ('LA', '3pm - 5pm (Mon-Fri)'), ('S', '9am - 2pm (Sat)')], default='M', max_length=2, verbose_name='Preferred Time to Call')),
            ],
            bases=('initial_enquiry.address',),
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('propertydetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='initial_enquiry.propertydetails')),
                ('personaldetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='initial_enquiry.personaldetails')),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name='Date Created')),
                ('has_been_contacted', models.BooleanField(default=False, verbose_name='Has been Contacted?')),
            ],
            bases=('initial_enquiry.personaldetails', 'initial_enquiry.propertydetails'),
        ),
    ]
