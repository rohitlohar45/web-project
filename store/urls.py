from django.urls import path
from django.views.generic import TemplateView

from .views import (
    CostListView,
    GradeListView,
    MetalListView,
    create_cost,
    create_grade,
    create_metal,
    create_supplier,
    create_yard,
    SupplierListView,
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


    path('update_cost/<str:pk>/', update_cost, name="update_cost"),
    path('delete_cost/<str:pk>/', delete_cost, name="delete_cost"),


    path('update_metal/<str:pk>/', update_metal, name="update_metal"),
    path('delete_metal/<str:pk>/', delete_metal, name="delete_metal"),

    # path('overhead_cost/', create_overheadCost, name='create-overheadcost'),
    path('create_cost/', create_cost, name='create_cost'),
    path('cost-list/', CostListView.as_view(), name='cost-list'),
    path('create_metal/', create_metal, name='create_metal'),
    path('metal-list/', MetalListView.as_view(), name='metal-list'),
    # path("meta/",jsondata,name = "jsondata"),
    path('create-grade/', create_grade, name='create-grade'),
    path('grade-list/', GradeListView.as_view(), name='grade-list'),
    # path("htmx-form/", htmx_form),
    # path("create-grade/cost/", htmx_models),
    path('supplier/yard/<str:pk>/', create_yard, name='supplier'),
    path('htmx/yard/<str:pk>/', detail_yard, name="detail-yard"),
    path('htmx/yard/<str:pk>/update/', update_yard, name="update-yard"),
    path('htmx/yard/<str:pk>/delete/', delete_yard, name="delete-yard"),
    path('htmx/create-yard-form/', create_yard_form, name='create-yard-form'),


    path('update_supplier/<str:pk>/', update_supplier, name="update_supplier"),

    
    # path('material-list/', materialmixlist.as_view(), name='material-list'),
    # path('material-mix-list/', mixmateriallist.as_view(), name='material-mix-list'),
    # path('update_mat_mix_items/<str:pk>/', update_mat_mix_items, name="update_mat_mix_items"),
    # path('delete_material-mixture/<str:pk>/', delete_mat_mix_items, name="delete_mat_mix_items"),
    
    # path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    path('delete_supplier/<str:pk>/', delete_supplier, name="delete_supplier"),
    # path('', TemplateView.as_view(template_name="home.html"), name='create-book'),
    # path('<pk>/', create_book, name='create-book'),
    # path('book/<pk>/', detail_book, name="detail-book"),
    # path('htmx/book/<pk>/update/', update_book, name="update-book"),
    # path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    # path('htmx/create-book-form/', create_book_form, name='create-book-form'),
]
