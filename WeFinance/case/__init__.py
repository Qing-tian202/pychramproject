# __init__.py


from .Certification import login
from .Certification import signup
from .Certification import logout
from .Certification import user_info
from .Information import get_profile
from .Information import update_profile
from .BankCardManagement import get_card_list
from .BankCardManagement import add_card
from .BankCardManagement import update_card
from .BankCardManagement import delete_card
from .RealNameVerification import submit_real_name
from .RealNameVerification import get_real_name_info
from .RealNameVerification import photo_image
from .RealNameVerification import change_photo

__all__ = ['login','signup','logout','user_info',
           'get_profile','update_profile',
           'get_card_list','add_card','update_card','delete_card',
           'submit_real_name','get_real_name_info','photo_image','change_photo']