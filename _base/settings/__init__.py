from decouple import config

poshtiban_settings = config('POSHTIBAN_SETTINGS', default='').lower()

if poshtiban_settings == 'production':
    from .production import *
elif poshtiban_settings == 'testing':
    from .testing import *
else:
    from .development import *
