from django.shortcuts import render,HttpResponse
from joblib import load
from .forms import RunForm,WinForm,tosWinForm,tosdicForm
# import joblib
# from sklearn.externals import joblib
model = load('savedmodels/model.joblib')
modelwin = load('savedmodels/modelwin.joblib')
modeltoswin= load('savedmodels/modeltoswin.joblib')
modeltosdic= load('savedmodels/modeltosdic.joblib')
# with open('/home/kali/Desktop/IPL_predictions/IPL_predictions/savedmodels/model_pkl' , 'rb') as f:
#     lr = pickle.load(f)
# Create your views here.
def runs(request):
    
    # a=model.predict([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,45]])
    # print(a)
    if request.method == 'POST':
        f=RunForm(request.POST)
        if f.is_valid():
            stedm=f.cleaned_data['n3']
            tem1=f.cleaned_data['team1']
            tem2=f.cleaned_data['team2']
            teamcode={'CSK':0,'DD':1,'GT':2,'KKR':3,'KTK':4,'LSG':5,'MI':6,'PBKS':7,'PWI':8,'RCB':9,'RPS':10,'RR':11,'SRH':12,'field':1, 'bat':0}
            arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            arr[26]=stedm
            arr[teamcode[tem1]]=1
            arr[teamcode[tem2]+13]=1
            a=model.predict([arr])
            # print(a)
            # return(render(request,'runspage.html'))'
            return(render(request,'runspage.html',{'a':f,'ans':int(a)}))
    f=RunForm()
    return(render(request,'runspage.html',{'a':f}))

def winner(request):
    ans='?'
    if request.method == 'POST':
        f=WinForm(request.POST)
        if f.is_valid():
            team1=f.cleaned_data['team1']
            team2=f.cleaned_data['team2']
            tosw=f.cleaned_data['teamtoswin']
            tosd=f.cleaned_data['teamtos']
            stem=f.cleaned_data['stdem']
            arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            teamcode={'CSK':0, 'DD':1, 'GL':2, 'KBKP':3, 'KTK':4, 'KKR':5, 'MI':6, 'PW':7, 'RR':8, 'RCB':9,
            'SRH':10,'field':1, 'bat':0}
            arr[23]=tosw
            arr[24]=tosd
            arr[22]=stem
            arr[(11+teamcode[team2])]=1
            arr[(teamcode[team1])]=1
            # pred=np.array(arr)
            ass=modelwin.predict([arr])
            print(tosd)
            if ass == 0:
                # print(tosd)
                ans=team1
            else:
                ans=team2
        return(render(request,'matchwin.html',{'a':f,'ans':ans}))
    f=WinForm()
    return(render(request,'matchwin.html',{'a':f,'ans':ans}))

def toswinner(request):
    ans='?'
    if request.method == 'POST':
        f=tosWinForm(request.POST)
        if f.is_valid():
            team1=f.cleaned_data['team1']
            team2=f.cleaned_data['team2']
            # tosw=f.cleaned_data['teamtoswin']
            # tosd=f.cleaned_data['teamtos']
            stem=f.cleaned_data['stdem']
            arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            teamcode={'CSK':0, 'DD':1, 'GL':2, 'KBKP':3, 'KTK':4, 'KKR':5, 'MI':6, 'PW':7, 'RR':8, 'RCB':9,
            'SRH':10,'field':1, 'bat':0}
            arr[22]=stem
            arr[(11+teamcode[team2])]=1
            arr[(teamcode[team1])]=1
            # pred=np.array(arr)
            ass=modeltoswin.predict([arr])
            if ass == 0:
                ans = team1
            else:
                ans = team2
        return(render(request,'tosswin.html',{'a':f,'ans':ans}))
    f=tosWinForm()
    return(render(request,'tosswin.html',{'a':f,'ans':ans}))

def tosdic(request):
    ans='?'
    if request.method == 'POST':
        f=tosdicForm(request.POST)
        if f.is_valid():
            team1=f.cleaned_data['team1']
            team2=f.cleaned_data['team2']
            # tosw=f.cleaned_data['teamtoswin']
            # tosd=f.cleaned_data['teamtos']
            stem=f.cleaned_data['stdem']
            arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            teamcode={'CSK':0, 'DD':1, 'GL':2, 'KBKP':3, 'KTK':4, 'KKR':5, 'MI':6, 'PW':7, 'RR':8, 'RCB':9,
            'SRH':10,'field':1, 'bat':0}
            arr[23]=stem
            arr[(11+teamcode[team2])]=1
            arr[(teamcode[team1])]=1
            # pred=np.array(arr)
            ass=modeltosdic.predict([arr])
            if ass == 0:
             ans='Bat'
            else:
             ans='field'
        return(render(request,'tosdic.html',{'a':f,'ans':ans}))
    f=tosdicForm()
    return(render(request,'tosdic.html',{'a':f,'ans':ans}))
