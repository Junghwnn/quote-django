from django.db import migrations

def seed_quotes(apps, schema_editor):
    Quote = apps.get_model('quotes', 'Quote')
    quotes = [('The only way to do great work is to love what you do.', 'Steve Jobs'), ("Code is like humor. When you have to explain it, it's bad.", 'Cory House'), ('First, solve the problem. Then, write the code.', 'John Johnson'), ('Simplicity is the soul of efficiency.', 'Austin Freeman'), ('Fix the cause, not the symptom.', 'Steve Maguire')]
    for text, author in quotes:
        Quote.objects.get_or_create(text=text, author=author)

class Migration(migrations.Migration):
    dependencies = [('quotes', '0001_initial')]
    operations = [migrations.RunPython(seed_quotes, migrations.RunPython.noop)]
