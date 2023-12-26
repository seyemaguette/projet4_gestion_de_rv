# Generated by Django 4.2.6 on 2023-12-22 18:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=20, verbose_name='Adresse')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=16, region=None, verbose_name='Telephone')),
                ('role', models.CharField(choices=[('', ''), ('cardiologue', 'cardiologue'), ('dermatologue', 'dermatologue'), ('gynecologue', 'gynecologue'), ('generaliste', 'generaliste'), ('dentiste', 'dentiste'), ('neurologue', 'neurologue'), ('pediatre', 'pediatre'), ('psychiatre', 'psychiatre')], max_length=20, verbose_name='Fonction')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, default='images/avatar.png', upload_to='images/', verbose_name='Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Rv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('patient', models.CharField(max_length=50, verbose_name='Avec Qui')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('date', models.DateField(verbose_name='Date')),
                ('hours', models.TimeField(verbose_name='Heure')),
                ('place', models.CharField(max_length=50, verbose_name='Lieu')),
                ('archive', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rv.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Prenom')),
                ('last_name', models.CharField(max_length=60, verbose_name='Nom')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Age')),
                ('address', models.CharField(max_length=20, verbose_name='Adresse')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=16, null=True, region=None, verbose_name='Telephone')),
                ('archive', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rv.doctor')),
            ],
        ),
    ]