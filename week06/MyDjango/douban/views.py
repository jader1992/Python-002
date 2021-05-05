from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import T1
from django.db.models import Avg

def books_short(request):
    t1 = T1.objects.using('douban')
    shorts = t1.all()

    # 评论数量
    counter = shorts.count()

    # 平均星级
    star_avg = f" {t1.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向
    send_avg = f" {t1.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = t1.values('sentiment')
    conditions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**conditions).count()

    # 反向数量
    conditions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**conditions).count()

    return render(request, 'result.html', locals())
