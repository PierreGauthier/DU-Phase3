{"filter":false,"title":"admin.py","tooltip":"/Webapp/info_chantier/admin.py","undoManager":{"mark":50,"position":50,"stack":[[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","# Register your models here.",""]},{"start":{"row":1,"column":0},"end":{"row":3,"column":27},"action":"insert","lines":["rom myproject.myapp.models import Author","","admin.site.register(Author)"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":35},"end":{"row":1,"column":41},"action":"remove","lines":["Author"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["*"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":32},"end":{"row":1,"column":36},"action":"remove","lines":["","from myproject.myapp.models import *"]},{"start":{"row":0,"column":32},"end":{"row":1,"column":31},"action":"insert","lines":["","from info_chantier import views"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":26},"end":{"row":1,"column":31},"action":"remove","lines":["views"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":27},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":59,"column":43},"action":"insert","lines":["from django.db import models","","# Create your models here.","","class Roadwork(models.Model):","    name = models.CharField(max_length=50)","    date_start = models.DateField()","    date_end = models.DateField()","    city = models.CharField(max_length=50)","    coord = models.CharField(max_length=50)","    object = models.CharField(max_length=1000)","    description = models.CharField(max_length=5000)","    contact = models.ForeignKey('Pro')","    ","class Infos_journalieres(models.Model):","    date = models.DateField()","    parking_access = models.IntegerField()","    walker_access = models.IntegerField()","    traffic_access = models.IntegerField()","    noise_access = models.IntegerField()","    ","class Deviation(models.Model):","    id_roadwork = models.ForeignKey('Roadwork')","    center = models.CharField(max_length=50) ","    path = models.CharField(max_length=500)","    ","class Alert(models.Model):","    id_roadwork = models.ForeignKey('Roadwork')","    timestamp = models.TimeField()","    table = models.CharField(max_length=100)","    field = models.CharField(max_length=100)","    old_value = models.CharField(max_length=100)","    new_value = models.CharField(max_length=100)","    ","class Capteur(models.Model):","    timestamp = models.TimeField()","    type = models.CharField(max_length=50)","    value = models.IntegerField()","    ","class Message(models.Model):","    id_user = models.ForeignKey('User')","    id_roadwork = models.ForeignKey('Roadwork')","    isAnswer = models.BooleanField()","    content = models.CharField(max_length=1000)","    ","class User(models.Model):","    email = models.CharField(max_length=50)","    adress = models.CharField(max_length=200)","    levelinfo = models.IntegerField()","    ","class Pro(models.Model):","    civility  = models.CharField(max_length=5)","    name = models.CharField(max_length=50)","    phone = models.CharField(max_length=50)","    email = models.CharField(max_length=50)"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":20},"end":{"row":3,"column":26},"action":"remove","lines":["Author"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":28},"action":"insert","lines":["Roadwork"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":17,"column":38},"action":"remove","lines":["from django.db import models","","# Create your models here.","","class Roadwork(models.Model):","    name = models.CharField(max_length=50)","    date_start = models.DateField()","    date_end = models.DateField()","    city = models.CharField(max_length=50)","    coord = models.CharField(max_length=50)","    object = models.CharField(max_length=1000)","    description = models.CharField(max_length=5000)","    contact = models.ForeignKey('Pro')"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":29},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":0},"end":{"row":4,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":29},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":5,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":29},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":6,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":29},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":0},"end":{"row":7,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":29},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":8,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":29},"end":{"row":9,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":0},"end":{"row":9,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":0},"end":{"row":10,"column":29},"action":"insert","lines":["admin.site.register(Roadwork)"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":20},"end":{"row":4,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":38},"action":"insert","lines":["Infos_journalieres"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":20},"end":{"row":5,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":29},"action":"insert","lines":["Deviation"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":20},"end":{"row":6,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":25},"action":"insert","lines":["Alert"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":20},"end":{"row":7,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":27},"action":"insert","lines":["Capteur"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":20},"end":{"row":8,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":27},"action":"insert","lines":["Message"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":0},"end":{"row":37,"column":33},"action":"remove","lines":["    ","class Infos_journalieres(models.Model):","    date = models.DateField()","    parking_access = models.IntegerField()","    walker_access = models.IntegerField()","    traffic_access = models.IntegerField()","    noise_access = models.IntegerField()","    ","class Deviation(models.Model):","    id_roadwork = models.ForeignKey('Roadwork')","    center = models.CharField(max_length=50) ","    path = models.CharField(max_length=500)","    ","class Alert(models.Model):","    id_roadwork = models.ForeignKey('Roadwork')","    timestamp = models.TimeField()","    table = models.CharField(max_length=100)","    field = models.CharField(max_length=100)","    old_value = models.CharField(max_length=100)","    new_value = models.CharField(max_length=100)","    ","class Capteur(models.Model):","    timestamp = models.TimeField()","    type = models.CharField(max_length=50)","    value = models.IntegerField()"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":20},"end":{"row":9,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":24},"action":"insert","lines":["User"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":20},"end":{"row":10,"column":28},"action":"remove","lines":["Roadwork"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":23},"action":"insert","lines":["Pro"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":0},"end":{"row":30,"column":43},"action":"remove","lines":["","    ","class Message(models.Model):","    id_user = models.ForeignKey('User')","    id_roadwork = models.ForeignKey('Roadwork')","    isAnswer = models.BooleanField()","    content = models.CharField(max_length=1000)","    ","class User(models.Model):","    email = models.CharField(max_length=50)","    adress = models.CharField(max_length=200)","    levelinfo = models.IntegerField()","    ","class Pro(models.Model):","    civility  = models.CharField(max_length=5)","    name = models.CharField(max_length=50)","    phone = models.CharField(max_length=50)","    email = models.CharField(max_length=50)"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":24},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":33},"end":{"row":1,"column":39},"action":"remove","lines":["models"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["*"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":34},"end":{"row":1,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1422265523458,"hash":"c094ba9ce6f7d10a5b6886ab0a27a18daab56e18"}