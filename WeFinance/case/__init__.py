# __init__.py


from .Certification import login,signup,logout,user_info
from .Information import get_profile,update_profile

from .BankCardManagement import get_card_list,add_card,delete_card,update_card

from .RealNameVerification import submit_real_name,get_real_name_info,photo_image,change_photo

from .BorrowProducts import get_borrow_products_list,get_product_info

from .LoanApplication import submit_application,get_chosen_loan_application,get_my_loan_application,upload_loan_application_material

from .Contract import generate_loan_contract,signature_contract,get_chosen_contract_info,get_disbursed_contract_info

from .Repayment import get_credit_score,get_quota_limit,repayment

from .Investmentproduct import get_investment_info,get_investment_products_list

from .Investmentoperation import invest,get_invest_list,get_my_invest_info,get_investments_summary

__all__ = ['login','signup','logout','user_info',
           'get_profile','update_profile',
           'get_card_list','add_card','update_card','delete_card',
           'submit_real_name','get_real_name_info','photo_image','change_photo',
           'get_product_info','get_borrow_products_list',
           'submit_application','get_my_loan_application','get_chosen_loan_application','upload_loan_application_material',
           'generate_loan_contract','signature_contract','get_chosen_contract_info','get_disbursed_contract_info',
           'get_credit_score','get_quota_limit','repayment',
           'get_investment_products_list','get_investment_info',
           'invest','get_invest_list','get_my_invest_info','get_investments_summary']