from amocrm import BaseContact, amo_settings, fields

from login_settings import user_email, user_hash, user_domain
amo_settings.set(user_email, user_hash, user_domain) #user_email, hash, domain