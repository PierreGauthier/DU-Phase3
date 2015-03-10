#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
from django import forms
from info_chantier.models import *
from django.http import HttpResponseRedirect
    

def nfc(request):
    
     #chantier_test = Roadwork.objects.get(pk=1)
    
    #print(chantier_test.name)
    
    
    data = []
    
    data.append({
            'id':'Information générales',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h1>Réfection de la chaussée<h1>',
            'subtitle':'<h3>Rue de la tour d\'Auvergne</h3>',
            'header':'<h4>du <em>26 février</em> 2015 au <em>03 mars</em> 2015</h4>',
            'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin scelerisque mauris id est convallis, eget aliquam lectus consectetur. Maecenas feugiat vehicula justo vitae facilisis. Pellentesque egestas rutrum sem, ut auctor sem ultrices finibus. Nunc massa tortor, ultrices vitae libero non, tempus efficitur purus. Vivamus iaculis nec urna vitae porttitor. Integer. ',
            'divider':'on',
            'icon':'warning sign'
        })
    data.append({
            'id':'État de la jounrnée',
            'topstyle':'',
            'bottomstyle':'',
            'title':'',
            'subtitle':'',
            'header':'',
            'content':'''<center class="resize" height=0.1 >
                            <i class="ui icon car resize" height=0.08 style="margin-right:10%;color:#FF3333;"></i>
                            <i class="ui icon home" style="margin-right:10%;color:#FFCCCC;"></i>
                            <span style="color:#FFCC33;">P</span>
                        </center></br>
                        <center class="resize" height=0.02 style="width:100%" >
                            <span style="margin-right:15%;">Circulation</span>
                            <span style="margin-right:5%;">Habitation</span>
                            Stationnement
                        </center></br></br>''',
            'divider':'off',
            'icon':'flag outline'
        })
    data.append({
            'id':'Entreprise',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h2 style="display:inline;">Colas Centre-Ouest</h2><img src="/static/images/LOGO_colas.png" style="float:right;width:30%;"/>',
            'subtitle':'</br><h4 style="display:inline;">Entreprise de VRD</h4>',
            'header':'Siège Social',
            'content':'2 Rue Gspard Coriolis, 44307 Nantes<br/>02 28 01 02 03',
            'divider':'on',
            'icon':'road'
        })
    data.append({
            'id':'Maitrise d\'ouvrage',
            'topstyle':'',
            'bottomstyle':'',
            'title':'<h2 style="display:inline;">Nantes Métropole</h2><img src="/static/images/nantes_metropole2.png" style="float:right;width:30%;"/>',
            'subtitle':'</br><h4 style="display:inline;">Maitre d\'oeuvre</h4>',
            'header':'Développement urbain',
            'content':'5 rue Vasco de Gama<br/>02 28 01 02 03',
            'divider':'on',
            'icon':'university'
        })
    data.append({
            'id':'Déviation',
            'topstyle':'background-color:#009988',
            'bottomstyle':'style="background:url('+generateMapUrl()+') no-repeat center center;-webkit-background-size: cover;-moz-background-size: cover;-o-background-size: cover;background-size: cover;height:200px;" onclick="location.href=\'http://maps.google.com?q=894%20Granville%20Street%20Vancouver%20BC%20V6Z%201K3\'"''',
            'title':'</br><h5><b>Déviations</b> par Rue Arthur III</h5>',
            'subtitle':'<h5><b>3,2</b> Kilomètres pour <b>4</b> minutes</h5></br>',
            'header':'',
            'content':'',
            'divider':'off',
            'icon':'level up'
        })
    data.append({
            'id':'Questions',
            'topstyle':'background-color:#777777',
            'bottomstyle':'',
            'title':'<i class="ui icon white big comment inline" style="width:10%;position:relative;"></i><h2 style="color:white;margin-left:15%;margin-top:-25px;width:80%;position:relative;">Jusqu\'à quand le concasseur sera-t-il utilisé ?</h2></br>',
            'subtitle':'',
            'header':'',
            'content':'</br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae purus tincidunt, scelerisque dui in, vestibulum dolor. Sed accumsan mattis elit et dictum. Fusce in felis eget nunc vulputate faucibus vitae et est.<div class="ui divider"></div><input class="resize3" height=0.04 type="text" placeholder="Posez votre question ici ..." style="border:none;width:100%;" />',
            'divider':'off',
            'icon':'comments'
        })
    data.append({
            'id':'Abonnement',
            'topstyle':'',
            'bottomstyle':'',
            'title':'',
            'subtitle':'',
            'header':'',
            'content':'</br><p class="resize" height=0.025 style="margin-right:15%;" >Je souhaite reçevoir gratuitement un suivi personnalisé du chantier</p></br></br>',
            'divider':'off',
            'icon':'mail'
        })
    return render_to_response('page_chantier.html', {
        'data': data 
    }, context_instance=RequestContext(request))
    
    
def subscrib(request):
    return render_to_response('page_subscrib.html', {}, context_instance=RequestContext(request))
    
def walk(request):
    return render_to_response('page_walkthroughs.html', {}, context_instance=RequestContext(request))
    
def unset(request):
    return render_to_response('unsetcookie.html', {}, context_instance=RequestContext(request))
    
def end(request):
    return render_to_response('page_end.html', {}, context_instance=RequestContext(request))
    
def testmail(request):
    sendMail('Chantier de la rue Arthur III','Bonjour, \nLa rue sera fermé aujourd\'hui de 13h à 15h \n Indawo',['p_gauthier@live.fr'])
    return render_to_response('page_end.html', {}, context_instance=RequestContext(request))
    
def svg2string(name):
    
    f = open(os.path.join(settings.STATICFILES_DIRS[0],'images/'+name+'.svg'), 'r')
    return f.read()
    
    
def newUser(request, email, phone):
    
    print('-----'+phone+'------');
    u = _User(phone=str(phone), email=email, address="123321", levelinfo=1)
    return HttpResponseRedirect("/")
    
def generateMapUrl():
    
    return "https://maps.googleapis.com/maps/api/staticmap?center=47.2062432,-1.5619455&zoom=16&size=300x300&path=color:0x0000ff|weight:5|47.208105,%20-1.562444|47.206786,%20-1.562101|47.207180,%20-1.559301|47.206138,%20-1.559043|47.205759,%20-1.561908"
    
def sendMail(obj,msg,dest):
    
    mailserver = smtplib.SMTP_SSL('smtp.googlemail.com', 465) #smtplib.SMTP('smtp.gmail.com', 587)
    #mailserver.ehlo()
   # mailserver.starttls()
    #mailserver.ehlo()
    mailserver.login('borneindawo@gmail.com', 'du-phase3')
    for d in dest :
        print(d)
        message = MIMEMultipart()
        message['From'] = 'borneindawo@gmail.com'
        message['To'] = d
        message['Subject'] = obj 
        message.attach(MIMEText(msg))
        mailserver.sendmail('borneindawo@gmail.com', d, message.as_string())
    mailserver.quit()
    
    