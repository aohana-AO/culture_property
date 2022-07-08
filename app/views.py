from re import template

from django.db.models import Q
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Bunka
import feedparser
import json
import pprint
from django.views import generic

class IndexView(ListView):
    model = Bunka
    context_object_name = "bunka_list"
    template_name = 'app/index.html'


class SiteView(TemplateView):
    template_name = 'app/site.html'

class TatemonoView(ListView):
    model = Bunka
    context = Bunka.objects.filter(種類='建造物')
    context_object_name = "bunka_list"
    template_name = 'app/cultural_tatemono.html'

class NotatemonoView(ListView):
    model = Bunka
    context= Bunka.objects.filter(種類='その他')
    context_object_name = "bunka_list"
    template_name = 'app/cultural_no_tatemono.html'

class KokuhouView(ListView):
    model = Bunka
    context = Bunka.objects.filter(文化財分類='国宝')
    context_object_name = "bunka_list"
    template_name = 'app/cultural_kokuhou.html'

    """
class ListView(generic.ListView):
    Bunkaテーブルの一覧表作成
    model = Bunka
    template_name = 'app/List.html'
    """
class ListView(ListView):
    model=Bunka

    def lists(request):
        check = request.POST.getlist("office")
        subete = request.POST.get("subete")
        bunnrui = request.POST.getlist("bunnrui")
        kensakumei = request.POST.get("kensakumei")
        kensakujuusyo = request.POST.get("kensakujuusyo")

        if kensakumei:
            bunka_list = Bunka.objects.filter(
                Q(名称__icontains=kensakumei))
        elif kensakujuusyo:
            bunka_list = Bunka.objects.filter(
                Q(愛媛県松山市住所__icontains=kensakujuusyo)
            )
        elif len(bunnrui) == 0 and len(check) == 0 or subete == '全て':
            bunka_list = Bunka.objects.all()
        elif len(check) == 0 and len(bunnrui) != 0:
            bunka_list = Bunka.objects.filter(文化財分類__in=bunnrui)
            print('------------------')
            print(bunnrui)
        elif len(check) != 0 and len(bunnrui) == 0:
            bunka_list = Bunka.objects.filter(種類__in=check)
            print('------------------')
            print(check)
        else:
            bunka_list = Bunka.objects.filter(種類__in=check,文化財分類__in=bunnrui)
        return render(request, 'app/List.html', {'bunka_list': bunka_list})


    def detail(request, pk):
        bunka = get_object_or_404(Bunka, pk=pk)

        return render(request, 'app/detail.html', {'bunka': bunka},)



class NewsView(View):
    def get(self, request, *args, **kwargs):
        # RSSのスクレイピング

        url = 'https://news.google.com/news/rss/search/section/q/愛媛県文化財/AED?ned=jp&amp;hl=ja&amp;gl=JP'

        d = feedparser.parse(url)
        news = list()

        for i, entry in enumerate(d.entries, 1):
            p = entry.published_parsed
            sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)
            sortkey2 = "%04d.%02d.%02d" % (p.tm_year, p.tm_mon, p.tm_mday)

            tmp = {
                "no": i,
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "sortkey": sortkey,
                "sortkey2": sortkey2
            }

            news.append(tmp)

        news = sorted(news, reverse=True, key=lambda x: x['sortkey'])

        pprint.pprint(news)
        return render(request, 'app/NewsView.html', {'news': news})
