from django.urls import path
from .views import eCommerceView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path(
        "app/ecommerce/dashboard/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_dashboard.html")),
        name="app-ecommerce-dashboard",
    ),
    path(
        "app/ecommerce/product/list/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_product_list.html")),
        name="app-ecommerce-product-list",
    ),
    path(
        "app/ecommerce/product/add/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_product_add.html")),
        name="app-ecommerce-product-add",
    ),
    path(
        "app/ecommerce/product/category/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_category_list.html")),
        name="app-ecommerce-product-category-list",
    ),
    path(
        "app/ecommerce/order/list/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_order_list.html")),
        name="app-ecommerce-order-list",
    ),
    path(
        "app/ecommerce/order/details/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_order_details.html")),
        name="app-ecommerce-order-details",
    ),
    path(
        "app/ecommerce/customer_all/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_customer_all.html")),
        name="app-ecommerce-customer-all",
    ),
    path(
        "app/ecommerce/customer/details/overview/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_customer_details_overview.html" )),
        name="app-ecommerce-customer-details-overview",
    ),
    path(
        "app/ecommerce/customer/details/security/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_customer_details_security.html")),
        name="app-ecommerce-customer-details-security",
    ),
    path(
        "app/ecommerce/customer/details/billing/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_customer_details_billing.html")),
        name="app-ecommerce-customer-details-billing",
    ),
    path(
        "app/ecommerce/customer/details/notifications/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_customer_details_notifications.html" )),
        name="app-ecommerce-customer-details-notifications",
    ),
    path(
        "app/ecommerce/manage_reviews/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_manage_reviews.html")),
        name="app-ecommerce-manage-reviews",
    ),
    path(
        "app/ecommerce/referrals/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_referral.html")),
        name="app-ecommerce-referrals",
    ),
    path(
        "app/ecommerce/settings/details/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_detail.html")),
        name="app-ecommerce-settings-detail",
    ),
    path(
        "app/ecommerce/settings/payments/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_payments.html")),
        name="app-ecommerce-settings-payments",
    ),
    path(
        "app/ecommerce/settings/checkout/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_checkout.html")),
        name="app-ecommerce-settings-checkout",
    ),
    path(
        "app/ecommerce/settings/shipping/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_shipping.html")),
        name="app-ecommerce-settings-shipping",
    ),
    path(
        "app/ecommerce/settings/locations/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_locations.html")),
        name="app-ecommerce-settings-locations",
    ),
    path(
        "app/ecommerce/settings/notifications/",
        login_required(eCommerceView.as_view(template_name="app_ecommerce_settings_notifications.html")),
        name="app-ecommerce-settings-notifications",
    ),
    path('shop/new/', views.shop_create, name='shop_create'),
]
