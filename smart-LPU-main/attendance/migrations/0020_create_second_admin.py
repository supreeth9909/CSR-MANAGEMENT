from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_second_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    email = "csupreethreddy@gmail.com"
    password = "csr@123"
    
    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            'email': email,
            'is_superuser': True,
            'is_staff': True,
        }
    )
    user.password = make_password(password)
    user.save()

def remove_second_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username="csupreethreddy@gmail.com").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_create_default_user'),
    ]

    operations = [
        migrations.RunPython(create_second_superuser, remove_second_superuser),
    ]
