from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
   
    
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/<int:projet_id>/', views.detail_projet, name='detail_projet'),

    # Page courte (aperçu des services)
    path('services/', views.services, name='services'),
    path('annonces/', views.annonces_list, name='annonces'),

    path('annonce/<int:annonce_id>/', views.annonce_detail, name='annonce_detail'),
    path('annonces/', views.annonces_list, name='annonces_list'),

    # Page détaillée (celle que tu as montrée)
    path('services/detail/', views.services_view, name='services_detail'),
   
    
    path("paiement/<int:produit_id>/", views.paiement_stripe, name="paiement_stripe"),
    path("paiement/success/", views.paiement_success, name="paiement_success"),
    path("paiement/cancel/", views.paiement_cancel, name="paiement_cancel"),
   
    path('produits/', views.produits_list, name='produits_list'),
    path('produit/<int:produit_id>/', views.product_detail, name='product_detail'),  # <- virgule ici !
    path("commande/<int:id>/", views.passer_commande, name="passer_commande"),
    path('urgence/', views.urgence_view, name='urgence'),
    path("submit-commentaire/", views.submit_commentaire, name="submit_commentaire"),
    path("client/register/", views.client_register, name="client_register"),
    path("client/login/", views.client_login, name="client_login"),
    path("client/profile/", views.client_profile, name="client_profile"),
    path("messages/", views.messages_client, name="messages_client"),
    path('client/messages/', views.messages_client, name='messages_client'),
    path('client/logout/', views.client_logout, name='client_logout'),
    path("contact/", views.contact_client, name="contact_client"),
    path("admin/send-mail/", views.admin_send_mail, name="admin_send_mail"),
    path("admin/messages/", views.admin_messages, name="admin_messages"),
    path("admin-hexa/login/", views.login_admin, name="login_admin"),
    path("hexa/login/", views.login_hexa, name="login_hexa"),
    path("hexa/dashboard/", views.dashboard_hexa, name="dashboard_hexa"),
    path("hexa/envoyer-message/", views.envoyer_message, name="envoyer_message"),
    path('commande/<int:produit_id>/', views.order_view, name='order_view'),
    path('commande/recu/<int:order_id>/', views.order_receipt, name='order_receipt'),
    path('commande/download/<int:order_id>/', views.download_order_pdf, name='download_order_pdf'),
    path('order/<int:product_id>/', views.order_product, name='order_product'),
    path('commande/<int:id>/', views.passer_commande, name='order_product'),
    path("like/<int:pk>/", views.like_produit, name="like"),
    path('services/detail/', views.dev_page, name='dev_page'),
   
    path("like/<int:id>/", views.like_toggle, name="like_toggle"),
     
    path('detail/web-mobile/', views.service_web_mobile, name='service_web_mobile'),
    path('detail/marketing/', views.service_marketing, name='service_marketing'),
    path('detail/maintenance/', views.service_maintenance, name='service_maintenance'),
    path('detail/ai/', views.service_ai, name='service_ai'),
    
    path("repondre/<int:message_id>/", views.repondre_message, name="repondre_message"),



    



    


   












    
    

    path("chatbot_ai/", views.chatbot_ai, name="chatbot_ai"),
]
