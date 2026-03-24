from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    admins = [
        ("Chimbilicharan@gmail.com", "Charan@1835"),
        ("csupreethreddy@gmail.com", "csr@123"),
    ]
    
    for email, password in admins:
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

def remove_default_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username__in=["Chimbilicharan@gmail.com", "csupreethreddy@gmail.com"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_makeupattendancerecord_marked_via'),
    ]

    operations = [
        migrations.RunPython(create_default_superuser, remove_default_superuser),
    ]
