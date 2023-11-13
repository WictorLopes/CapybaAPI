from django.urls import path
from .views import login, logout, register, itemList, editUser, sendEmail, validateEmail, restrictedItemList


urlpatterns = [
    path('register/', register.register_user, name='register_user'),
    path('login/', login.login_user, name='login_user'),
    path('logout/', logout.logout_user, name='logout_user'),
    path('items/', itemList.ItemList.as_view(), name='item_list'),
    path('edit-profile/', editUser.EditUserProfile.as_view(), name='edit_user_profile'),
    path('send-email-confirmation-token/', sendEmail.send_email_confirmation_token, name='send_email_confirmation_token'),
    path('validate-email-confirmation-token/', validateEmail.validate_email_confirmation_token, name='validate_email_confirmation_token'),
    path('restricted-items/', restrictedItemList.RestrictedItemList.as_view(), name='restricted_item_list'),
]
