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
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h1>Réféction de la chaussée<h1>',
            'subtitle':'<h3>Rue de la tour d\'Auvergne</h3>',
            'header':'<h4>du <em>26 février</em> 2015 au <em>03 mars</em> 2015</h4>',
            'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin scelerisque mauris id est convallis, eget aliquam lectus consectetur. Maecenas feugiat vehicula justo vitae facilisis. Pellentesque egestas rutrum sem, ut auctor sem ultrices finibus. Nunc massa tortor, ultrices vitae libero non, tempus efficitur purus. Vivamus iaculis nec urna vitae porttitor. Integer. ',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'entreprise',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h2>Colas Centre-Ouest</h2>',
            'subtitle':'<h4>Entreprise de VRD</h4>',
            'header':'Siège Social',
            'content':'2 Rue Gspard Coriolis, 44307 Nantes<br/>02 28 01 02 03',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'moa',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h2>Nantes Métropole</h2>',
            'subtitle':'<h4>Maitre d\'oeuvre</h4>',
            'header':'Développement urbain',
            'content':'5 rue Vasco de Gama<br/>02 28 01 02 03',
            'divider':'on',
            'icon':svg2string('info')
        })
    data.append({
            'id':'dev',
            'topstyle':'background-color:#009988',
            'bottomstyle':'style=background-image:url('+generateMapUrl()+');height:200px; onclick=location.href=\'http://maps.google.com?q=894%20Granville%20Street%20Vancouver%20BC%20V6Z%201K3\'',
            'title':'<h5><b>Déviations</b> par Rue Arthur III</h5>',
            'subtitle':'<h5><b>3,2</b> Kilomètres pour <b>4</b> minutes</h5>',
            'header':'',
            'content':'',
            'divider':'off',
            'icon':svg2string('info')
        })
    data.append({
            'id':'info',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h1>Réféction de la chaussée<h1>',
            'subtitle':'<h3>Rue de la tour d\'Auvergne</h3>',
            'header':'<h4>du <em>26 février</em> 2015 au <em>03 mars</em> 2015</h4>',
            'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin scelerisque mauris id est convallis, eget aliquam lectus consectetur. Maecenas feugiat vehicula justo vitae facilisis. Pellentesque egestas rutrum sem, ut auctor sem ultrices finibus. Nunc massa tortor, ultrices vitae libero non, tempus efficitur purus. Vivamus iaculis nec urna vitae porttitor. Integer. ',
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
    
def end(request):
    return render_to_response('page_end.html', {}, context_instance=RequestContext(request))
    
def svg2string(name):
    
    f = open(os.path.join(settings.STATICFILES_DIRS[0],'images/'+name+'.svg'), 'r')
    return f.read()
    
    
def generateMapUrl():
    
    return "https://maps.googleapis.com/maps/api/staticmap?center=47.2062432,-1.5619455&zoom=16&size=600x300&path=color:0x0000ff|weight:5|47.208105,%20-1.562444|47.206786,%20-1.562101|47.207180,%20-1.559301|47.206138,%20-1.559043|47.205759,%20-1.561908"