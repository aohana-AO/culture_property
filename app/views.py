from re import template

from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Bunka
import feedparser
import json
import pprint
from django.views import generic

class IndexView(TemplateView):

    template_name = 'app/index.html'
class TatemonoView(TemplateView):

    template_name = 'app/cultural_tatemono.html'
class NotatemonoView(TemplateView):

    template_name = 'app/cultural_no_tatemono.html'
class KokuhouView(TemplateView):

    template_name = 'app/cultural_kokuhou.html'

    """
class ListView(generic.ListView):
    Bunkaテーブルの一覧表作成
    model = Bunka
    template_name = 'app/list.html'
    """
class ListView:
    model=Bunka


    def lists(request):
        check = request.POST.getlist("office")
        subete = request.POST.get("subete")
        bunnrui = request.POST.getlist("bunnrui")

        if len(bunnrui) == 0 and len(check) == 0 or subete == '全て':
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
        return render(request, 'app/list.html', {'bunka_list': bunka_list})


    def detail(request, pk):
        bunka = get_object_or_404(Bunka, pk=pk)
        return render(request, 'app/detail.html', {'bunka': bunka})



class NewsView(View):
    def get(self, request, *args, **kwargs):
        # RSSのスクレイピング

        url = 'https://news.google.com/news/rss/search/section/q/AED/AED?ned=jp&amp;hl=ja&amp;gl=JP'

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
