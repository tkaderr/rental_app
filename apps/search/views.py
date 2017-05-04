# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ..search.search import get_query, normalize_query
from ..add_item.models import Product, Tag

# Create your views here.

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        print "query"
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['name','description','tags__name'])

        found_entries = Product.objects.filter(entry_query).distinct()

    return render(request, 'search/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },)
