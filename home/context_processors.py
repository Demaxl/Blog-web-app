# Pass variables to base template
from .models import User

def message_processor(request):
    # Gets the default value of the profile_photo field
    default_pfp = User._meta.get_field('profile_photo').get_default()

    return {
        "default_pfp": default_pfp
    }
