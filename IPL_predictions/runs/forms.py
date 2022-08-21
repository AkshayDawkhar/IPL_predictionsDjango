from django import forms
teamName = (('SRH','Sunrisers Hyderabad'),('MI','Mumbai Indians'),('GT','Gujarat Lions'),('GT','Gujarat Titans'),('RPS','Rising Pune Supergiant'),('RCB','Royal Challengers Bangalore'),
        ('KKR','Kolkata Knight Riders'),('DD','Delhi Daredevils'),('PBKS','Kings XI Punjab'),('PBKS','Punjab Kings'),
        ('CSK','Chennai Super Kings'),('RR','Rajasthan Royals'),('DD','Deccan Chargers'),(
       'KTK','Kochi Tuskers Kerala'),('RPS','Rising Pune Supergiants'),('PWI','Pune Warriors India'),('LSG','Lucknow Super Giants',)
       ,('DD','Delhi Capitals',))
# stdmname=(('M. Chinnaswamy Stadium, Bangalore','M. Chinnaswamy Stadium, Bangalore'),(
#        'Punjab Cricket Association Stadium, Mohali','Punjab Cricket Association Stadium, Mohali'),(
#        'Feroz Shah Kotla, Delhi','Feroz Shah Kotla, Delhi',),( 'Eden Gardens, Kolkata','Eden Gardens, Kolkata'),(
#        'Wankhede Stadium, Mumbai','Wankhede Stadium, Mumbai'),( 'Sawai Mansingh Stadium, Jaipur','Sawai Mansingh Stadium, Jaipur'),(
#        'Rajiv Gandhi International Cricket Stadium, Hyderabad','Rajiv Gandhi International Cricket Stadium, Hyderabad'),(
#        'M. A Chidambaram Stadium, Chennai','M. A Chidambaram Stadium, Chennai'),(
#        'DY Patil Stadium, Navi Mumbai','DY Patil Stadium, Navi Mumbai'),( 'Newlands, Cape Town','Newlands, Cape Town'),(
#        ("St George's Park, Port Elizabeth","St George's Park, Port Elizabeth"), 'Kingsmead, Durban', 'Kingsmead, Durban'),(
#        'SuperSport Park, Centurion','SuperSport Park, Centurion'),( 'Buffalo Park, East London','Buffalo Park, East London'),(
#        'New Wanderers Stadium, Johannesburg','New Wanderers Stadium, Johannesburg'),(
#        'De Beers Diamond Oval, Kimberley','De Beers Diamond Oval, Kimberley'),(
#        'OUTsurance Oval, Bloemfontein','OUTsurance Oval, Bloemfontein'),( 'DY Patil Stadium, Mumbai','DY Patil Stadium, Mumbai'),(
#        'Brabourne Stadium, Mumbai','Brabourne Stadium, Mumbai'),( 'M. A. Chidambaram Stadium, Chennai','M. A. Chidambaram Stadium, Chennai'),(
#        'Sardar Patel Stadium, Ahmedabad','Sardar Patel Stadium, Ahmedabad'),( 'Barabati Stadium, Cuttack','Barabati Stadium, Cuttack'),(
#        'Vidarbha Cricket Association Stadium, Nagpur','Vidarbha Cricket Association Stadium, Nagpur'),(
#        'HPCA Cricket Stadium, Dharamsala','HPCA Cricket Stadium, Dharamsala'),(
#        'Jawaharlal Nehru Stadium, Kochi','Jawaharlal Nehru Stadium, Kochi'),(
#        'Holkar Cricket Stadium, Indore','Holkar Cricket Stadium, Indore'),( 'HPCA Stadium, Dharamsala', 'HPCA Stadium, Dharamsala'),(
#        'ACA-VDCA Stadium, Visakhapatnam','ACA-VDCA Stadium, Visakhapatnam'),(
#        'Subrata Roy Sahara Stadium, Pune','Subrata Roy Sahara Stadium, Pune'),(
#        'Raipur International Cricket Stadium, Raipur','Raipur International Cricket Stadium, Raipur'),(
#        'JSCA International Cricket Stadium, Ranchi','JSCA International Cricket Stadium, Ranchi'),(
#        'Sheikh Zayed Stadium, Abu Dhabi','Sheikh Zayed Stadium, Abu Dhabi'),( 'Sharjah Cricket Stadium','Sharjah Cricket Stadium'),(
#        'Dubai International Cricket Stadium','Dubai International Cricket Stadium'),( 'MCA Stadium, Pune','MCA Stadium, Pune'),(
#        'Chhattisgarh International Cricket Stadium, Raipur','Chhattisgarh International Cricket Stadium, Raipur'),(
#        'Saurashtra Cricket Association Stadium, Rajkot','Saurashtra Cricket Association Stadium, Rajkot'),(
#        'Maharashtra Cricket Association Stadium, Pune','Maharashtra Cricket Association Stadium, Pune'),(
#        'Green Park Stadium, Kanpur','Green Park Stadium, Kanpur'),(
#        'Shaheed Veer Narayan Singh International Stadium, Raipur','Shaheed Veer Narayan Singh International Stadium, Raipur'),(
#        'Sheikh Zayed Cricket Stadium, Abu Dhabi','Sheikh Zayed Cricket Stadium, Abu Dhabi'),(
#        'Dubai International Cricket Stadium, Dubai','Dubai International Cricket Stadium, Dubai'),(
#        'Sharjah Cricket Stadium, Sharjah','Sharjah Cricket Stadium, Sharjah'),(
#        'Narendra Modi Stadium, Ahmedabad','Narendra Modi Stadium, Ahmedabad'),( 'Arun Jaitley Stadium, Delhi','Arun Jaitley Stadium, Delhi'),(
#        'MCA International Stadium, Pune','MCA International Stadium, Pune'))
class RunForm(forms.Form):
    team1=forms.CharField(widget=forms.Select(choices=teamName))
    team2=forms.CharField(widget=forms.Select(choices=teamName))
    n3=forms.IntegerField()
    # n4=forms.EmailField()
teamNamewin =(('CSK','CSK'),( 'DD','DD'),( 'GL','GL'),( 'KBKP','KBKP'),( 'KTK','KTK'),( 'KKR','KKR'),( 'MI','MI'),( 'PW','PW'),( 'RR','RR'),( 'RCB','RCB'),( 'SRH','SRH')) 
teamNamewintos=((1,'field'),(0,'bat'))
teamNamewintoswin=((0,'team1'),(1,'team2'))
class WinForm(forms.Form):
    team1=forms.CharField(widget=forms.Select(choices=teamNamewin))
    team2=forms.CharField(widget=forms.Select(choices=teamNamewin))
    teamtoswin=forms.CharField(widget=forms.Select(choices=teamNamewintoswin))
    teamtos=forms.CharField(widget=forms.Select(choices=teamNamewintos))
    stdem=forms.IntegerField(widget=forms.NumberInput())
# 'CSK':0, 'DD':1, 'GL':2, 'KBKP':3, 'KTK':4, 'KKR':5, 'MI':6, 'PW':7, 'RR':8, 'RCB':9,
    #    'SRH':10,'field':1, 'bat':0
class tosWinForm(forms.Form):
    team1=forms.CharField(widget=forms.Select(choices=teamNamewin))
    team2=forms.CharField(widget=forms.Select(choices=teamNamewin))
    # teamtoswin=forms.CharField(widget=forms.Select(choices=teamNamewintoswin))
    # teamtos=forms.CharField(widget=forms.Select(choices=teamNamewintos))
    stdem=forms.IntegerField(widget=forms.NumberInput())
class tosdicForm(forms.Form):
    team1=forms.CharField(widget=forms.Select(choices=teamNamewin))
    team2=forms.CharField(widget=forms.Select(choices=teamNamewin))
    # teamtoswin=forms.CharField(widget=forms.Select(choices=teamNamewintoswin))
    # teamtos=forms.CharField(widget=forms.Select(choices=teamNamewintos))
    stdem=forms.IntegerField(widget=forms.NumberInput())