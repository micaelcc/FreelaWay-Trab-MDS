from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # criar path, view e template
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.sair, name='sair'),

    # urls referente ao processo de recup. senha
    #o próprio django vai criar um mecanismo para recuperar a senha e mostrar nesse template especificado.
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),

    # pagina após o usuario inserir seu email para recuperar senha, confirma email enviado.
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),

    # pagina especifica onde o usuário vai redefinir de fato sua senha.
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),

    # página exibida após a senha ter sido redefinida com sucesso.
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]