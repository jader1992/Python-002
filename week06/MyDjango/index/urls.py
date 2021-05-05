from django.urls import path, re_path, register_converter
from . import views, converters

# URL变量类型：str，int, slug, uuid, path

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConvert, 'yyyy')

urlpatterns = [
    # 路由是从上到下一次加载

    path('', views.index),

    # 变量类型路由
    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    # 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'), #给我们的路径保定了一个名字urlyear


    # 自定义过滤器
    path('<yyyy:year>', views.year),


    path('books', views.books, name="books")
]