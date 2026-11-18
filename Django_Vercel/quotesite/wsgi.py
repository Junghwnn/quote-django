import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotesite.settings')
application = get_wsgi_application()
# Initialize the writable, temporary database on Vercel cold starts.
if os.environ.get('VERCEL'):
    import fcntl
    from django.core.management import call_command
    with open('/tmp/quote-app-migrate.lock', 'w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        call_command('migrate', interactive=False, verbosity=0)
app = application
