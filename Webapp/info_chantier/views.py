#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
from django import forms
from info_chantier.models import *
    

def nfc(request):
    
    chantier_test = Roadwork.objects.get(pk=1)
    
    print(chantier_test.name)
    
    
    data = []
    
    data.append({
            'id':'info',
            'style':'',
            'title':'infos',
            'header':'<h2>Refection de la chaussée</h2><h4>Rue de la tour d\'Auvergne</h4>',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'dev',
            'style':'background-image:url('+generateMapUrl()+')',
            'title':'infos',
            'header':'Déviation',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'off',
            'icon':svg2string('info')
        })
    data.append({
            'id':'azerty',
            'style':'',
            'title':'infos',
            'header':'dsfs',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'fjjrn',
            'style':'',
            'title':'infos',
            'header':'sdfsdf',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'ferrf',
            'style':'',
            'title':'infos',
            'header':'zerzer',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'dev',
            'style':'background-image:url('+generateMapUrl()+')',
            'title':'infos',
            'header':'Déviation',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'off',
            'icon':svg2string('info')
        })
    data.append({
            'id':'azerty',
            'style':'',
            'title':'infos',
            'header':'dsfs',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'fjjrn',
            'style':'',
            'title':'infos',
            'header':'sdfsdf',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'ferrf',
            'style':'',
            'title':'infos',
            'header':'zerzer',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'dev',
            'style':'background-image:url('+generateMapUrl()+')',
            'title':'infos',
            'header':'Déviation',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'off',
            'icon':svg2string('info')
        })
    data.append({
            'id':'azerty',
            'style':'',
            'title':'infos',
            'header':'dsfs',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'fjjrn',
            'style':'',
            'title':'infos',
            'header':'sdfsdf',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'ferrf',
            'style':'',
            'title':'infos',
            'header':'zerzer',
            'content':'<h4>Du tant au tant</h4>bledfksdf sdkfsdkfhdjhzjk fsjdhfsk djfhs kdfjzhjdhf kzjhfd skjdf kjhdsfjh',
            'divider':'on',
            'icon':svg2string('info')
        })


    return render_to_response('page_chantier.html', {
        'data': data 
    }, context_instance=RequestContext(request))
    
    
def subscrib(request):
    return render_to_response('page_subscrib.html', {}, context_instance=RequestContext(request))
    
def walk(request):
    return render_to_response('page_walkthroughs.html', {}, context_instance=RequestContext(request))
    
def svg2string(name):
    
    f = open(os.path.join(settings.STATICFILES_DIRS[0],'images/'+name+'.svg'), 'r')
    return f.read()
    
    
def generateMapUrl():
    
    return "https://maps.googleapis.com/maps/api/staticmap?zoom=3&size=600x300&path=color:0x0000ff|weight:5|40.737102,-73.990318|40.749825,-73.987963|40.752946,-73.987384|40.755823,-73.986397"