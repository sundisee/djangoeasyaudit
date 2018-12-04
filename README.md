# djangoeasyaudit
django easy audit 
Quickstart
1. Install Django Easy Audit by running pip install django-easy-audit.

    Alternatively, you can download the latest release from GitHub, unzip it, and place the folder 'easyaudit' in the root of your project.

2. Add 'easyaudit' to your INSTALLED_APPS like this:

    INSTALLED_APPS = [
    ...
    'easyaudit',
]
3. Add Easy Audit's middleware to your MIDDLEWARE (or MIDDLEWARE_CLASSES) setting like this:

    MIDDLEWARE = (
    ...
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
)
4. Run python manage.py migrate easyaudit to create the app's models.
