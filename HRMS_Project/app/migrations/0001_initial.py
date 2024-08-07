# Generated by Django 4.2.4 on 2024-03-04 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=15)),
                ('joining_date', models.DateField()),
                ('designation', models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('QA', 'Quality Assurance'), ('UI/UX', 'UI/UX Designer'), ('Full Stack Developer', 'Full Stack Developer'), ('Backend Developer', 'Backend Developer')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Casual Leave', 'Casual Leave'), ('Sick Leave', 'Sick Leave'), ('Marriage Leave', 'Marriage Leave'), ('Annual Leave', 'Annual Leave'), ('Emergency Leave', 'Emergency Leave')], max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_approved', models.BooleanField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('manually_updated', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]
