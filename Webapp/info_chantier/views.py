#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def nfc(request):
    
    data = {}
    
    data['info'] = {'title':'Informations générales', 'content':'date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date,motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date,motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>'}
    data['deviation'] = {'title':'Déviation', 'content':'date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/'}
    data['abonnement'] = {'title':'Abonnement', 'content':'date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>'}
    data['contact'] = {'title':'Contact', 'content':'date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/>date, motif, etc<br/'}

    return render_to_response('page_chantier.html', {
        'data': data 
    }, context_instance=RequestContext(request))