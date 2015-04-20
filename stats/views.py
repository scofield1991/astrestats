from django.shortcuts import render, render_to_response, redirect 
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import time
from time import strftime
from datetime import date
from datetime import timedelta
import json
from json import JSONEncoder
# Create your views here.

from stats.models import Point
from stats.models import Point_zn
from stats.models import Zn_limit
from stats.models import Point_limit

def index(request):
    if request.method == 'GET':
        
       #point1=Point_limit.objects.get(point=1)
       #point2=Point_limit.objects.get(point=2)
       zn=Zn_limit.objects.get(id=1)
       zn_start_morning_h=zn.start_morning.strftime('%H:%M')[:2]
       zn_start_morning_m=zn.start_morning.strftime('%H:%M')[3:5]
       zn_end_morning_h=zn.end_morning.strftime('%H:%M')[:2]
       zn_end_morning_m=zn.end_morning.strftime('%H:%M')[3:5]
       zn_start_evening_h=zn.start_evening.strftime('%H:%M')[:2]
       zn_start_evening_m=zn.start_evening.strftime('%H:%M')[3:5]
       zn_end_evening_h=zn.end_evening.strftime('%H:%M')[:2]
       zn_end_evening_m=zn.end_evening.strftime('%H:%M')[3:5]
       point1_limit_m=Point_limit.objects.get(point=1).zn_morning
       point1_limit_e=Point_limit.objects.get(point=1).zn_evening
       point2_limit_m=Point_limit.objects.get(point=2).zn_morning
       point2_limit_e=Point_limit.objects.get(point=2).zn_evening
       #a=Point_zn.objects.filter(point=1).filter(date__gte=dt).filter(time__gte=t)
       #a=Point_zn.objects.filter(point=1).filter(date__gte=dt).filter(date__lte=dte).filter(time__gte=t).filter(time__lte=te)
       con_dict={"start_morning_h":zn_start_morning_h, "start_morning_m":zn_start_morning_m,
        "end_morning_h":zn_end_morning_h, "end_morning_m":zn_end_morning_m, 
        "start_evening_h":zn_start_evening_h, "start_evening_m":zn_start_evening_m,
        "end_evening_h":zn_end_evening_h, "end_evening_m":zn_end_evening_m,
        "point1_limit_m": point1_limit_m, "point1_limit_e": point1_limit_e,
        "point2_limit_m": point2_limit_m, "point2_limit_e":point2_limit_e,'pumba': ['lol',12]}
       try:
           dt_str = request.GET['date1']
           if dt_str:
               con_dict['date1']=dt_str
               dt_begin=datetime.strptime(dt_str,'%d.%m.%Y')
           else:
               dt_begin=date.today()
           diff=timedelta(days=1)
           dt_end=dt_begin+diff
           time_begin_m=Zn_limit.objects.all()[0].start_morning
           time_begin_e=Zn_limit.objects.all()[0].end_morning
           zn_dict={}
           for i in [1,2]:
               lst=[]
               query=Point_zn.objects.filter(point=i).filter(date__gte=dt_begin).filter(date__lte=dt_end).filter(time__gte=time_begin_m).filter(time__lte=time_begin_e)
               for i in range(len(query)):
                   lst.append(a[i].zn)
               zn_dict.update({'zn'+str(i): lst})
           json_zn_dict=json.dumps(zn_dict)
           con_dcit['json_zn_dict']=json_zn_dict
           
           store_address = {'street':'Main #385','city':'San Diego','state':'CA'}
           con_dict['store_address']=store_address
       except:
           pass
           
       #queue= Point.objects.filter(id=1).filter(dtime__gte=date.today()).order_by('dtime')
       return render(request, 'stats/index.html', con_dict)
    if request.method=='POST':
        start_morning=str(request.POST['date11'])+":"+str(request.POST['datem1'])
        end_morning=str(request.POST['date22'])+":"+str(request.POST['datem2'])
        start_evening=str(request.POST['date3'])+":"+str(request.POST['datem3'])
        end_evening=str(request.POST['date4'])+":"+str(request.POST['datem4'])
        zn_morning1=request.POST['value1']
        zn_evening1=request.POST['valuem1']
        zn_morning2=request.POST['value2']
        zn_evening2=request.POST['valuem2']
        p1=Point.objects.get(id=1)
        p2=Point.objects.get(id=2)
        zn=Zn_limit.objects.get(id=1)
        #con_dict={"start_morning":zn.start_morning, "end_morning":zn.end_morning}
        try:
            zn.start_morning=start_morning
            zn.end_morning=end_morning
            zn.start_evening=start_evening
            zn.end_evening=end_evening
            zn.save()
        except:
            pass
        #zn_limit=Zn_limit(start_morning=start_morning, end_morning=end_morning,start_evening=start_evening,end_evening=end_evening)
        #zn_limit.save()
        try:
            point1_limit=Point_limit.objects.get(point=1)
            point2_limit=Point_limit.objects.get(point=2)
            point1_limit.zn_morning=zn_morning1
            point1_limit.zn_evening=zn_evening1
            point2_limit.zn_morning=zn_morning2
            point2_limit.zn_evening=zn_evening2
            point1_limit.save()
            point2_limit.save()
        except:
            pass
        #b=Zn_limit(start_morning="1:30", end_morning="8:00", start_evening="17:00", end_evening='20:00') 
        
        
                
        return redirect('/stats/')
        #return render(request, 'stats/index.html', con_dict)
        
def graph_data(request):
    try:
           dt_str = request.GET['date1']
           if dt_str:
               con_dict['date1']=dt_str
               dt_begin=datetime.strptime(dt_str,'%d.%m.%Y')
           else:
               dt_begin=date.today()
           diff=timedelta(days=1)
           dt_end=dt_begin+diff
           time_begin_m=Zn_limit.objects.all()[0].start_morning
           time_begin_e=Zn_limit.objects.all()[0].end_morning
           zn_dict={}
           for i in [1,2]:
               lst=[]
               query=Point_zn.objects.filter(point=i).filter(date__gte=dt_begin).filter(date__lte=dt_end).filter(time__gte=time_begin_m).filter(time__lte=time_begin_e)
               for i in range(len(query)):
                   lst.append(a[i].zn)
               zn_dict.update({'zn'+str(i): lst})
           json_zn_dict=json.dumps(zn_dict)
           con_dcit['json_zn_dict']=json_zn_dict
           
           store_address = {'street':'Main #385','city':'San Diego','state':'CA'}
           con_dict['store_address']=store_address
        except:
            pass
    return HttpResponse(json_zn_dict)
    

def query(table,point_id, pr):
	queue= Point.objects.filter(point=point_id).filter(dtime__gte=date.today()).filter(param=pr).order_by('dtime')
    #a=Point_zn.objects.filter(point=1).filter(date__gte=dt).filter(date__lte=dte).filter(time__gte=t).filter(time__lte=te)
	return queue
