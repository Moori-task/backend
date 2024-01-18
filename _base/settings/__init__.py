from decouple import config

settings = config('SETTINGS', default='').lower()

if settings == 'production':
    from .production import *
elif settings == 'testing':
    from .testing import *
else:
    from .development import *
