from django import urls
from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    CostListView,
    GradeListView,
    MetalListView,
    Quality_View,
    create_cost,
    create_grade,
    create_metal,
    create_quality,
    create_quality_form,
    create_supplier,
    create_yard,
    SupplierListView,
    delete_quality,
    detail_quality,
    # demoview,
    show_grade,
    # YardListView,
    create_yard_form,
    delete_cost,
    delete_grade,
    delete_metal,
    delete_supplier,
    delete_yard,
    detail_yard,
    # jsondata,
    # htmx_models,
    update_cost,
    update_grade,
    
    update_metal,
    update_quality,
    update_supplier,
    update_yard,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-yard/', create_yard, name='create-yard'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    # path('yard-list/', YardListView.as_view(), name='yard-list'),
    path('update_yard/<str:pk>/', update_yard, name="update_yard"),
    path('delete_yard/<str:pk>/', delete_yard, name="delete_yard"),

    path('update_grade/<str:pk>/', update_grade, name="update_grade"),
    path('delete_grade/<str:pk>/', delete_grade, name="delete_grade"),

    path('obj_list/',Quality_View, name="obj_list"),
    path('chaining/', include('smart_selects.urls')),
    path('update_cost/<str:pk>/', update_cost, name="update_cost"),
    path('delete_cost/<str:pk>/', delete_cost, name="delete_cost"),

    # path('demo/',demoview, name="demo"),
    path('update_metal/<str:pk>/', update_metal, name="update_metal"),
    path('delete_metal/<str:pk>/', delete_metal, name="delete_metal"),

    # path('ajax/load-branches/', load_yard, name='ajax_load_yard'),


    # path('overhead_cost/', create_overheadCost, name='create-overheadcost'),
    path('create_cost/', create_cost, name='create_cost'),
    path('cost-list/', CostListView.as_view(), name='cost-list'),
    path('create_metal/', create_metal, name='create_metal'),
    path('metal-list/', MetalListView.as_view(), name='metal-list'),

    path('create-grade/', create_grade, name='create-grade'),
    path('grade-list/', GradeListView.as_view(), name='grade-list'),
    
    path('supplier/yard/<str:pk>/', create_yard, name='supplier'),
    path('htmx/yard/<str:pk>/', detail_yard, name="detail-yard"),
    path('htmx/yard/<str:pk>/update/', update_yard, name="update-yard"),
    path('htmx/yard/<str:pk>/delete/', delete_yard, name="delete-yard"),
    path('htmx/create-yard-form/', create_yard_form, name='create-yard-form'),

    path('quality_list/', create_quality, name='quality-list'),
    path('htmx/quality/<str:pk>/', detail_quality, name="detail-quality"),
    path('htmx/quality/<str:pk>/update/', update_quality, name="update-quality"),
    path('htmx/quality/<str:pk>/delete/', delete_quality, name="delete-quality"),
    path('htmx/create-quality-form/', create_quality_form, name='create-quality-form'),


    path('update_supplier/<str:pk>/', update_supplier, name="update_supplier"),

    path('delete_supplier/<str:pk>/', delete_supplier, name="delete_supplier"),

]
