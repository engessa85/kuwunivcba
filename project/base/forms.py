from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Desires_model,Courses_model, DT_model, Days_model ,User



class TeacherForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["first_name", "last_name", "username", "email", "password1","password2"]
        help_texts = {"username":None}




class DesireForm(forms.ModelForm):

    d1 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True))
    d1t1 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d1t2 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d1t3 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    day1 = forms.ModelChoiceField(queryset=Days_model.objects.all())

    d2 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True))
    d2t1 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d2t2 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d2t3 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    day2 = forms.ModelChoiceField(queryset=Days_model.objects.all())

    d3 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True))
    d3t1 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d3t2 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d3t3 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    day3 = forms.ModelChoiceField(queryset=Days_model.objects.all())

    d4 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True))
    d4t1 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d4t2 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d4t3 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    day4 = forms.ModelChoiceField(queryset=Days_model.objects.all())


    d5 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True))
    d5t1 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d5t2 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    d5t3 = forms.ModelChoiceField(queryset=DT_model.objects.all())
    day5 = forms.ModelChoiceField(queryset=Days_model.objects.all())

    class Meta:
        model = Desires_model
        
        fields = ['d1','d1t1','d1t2','d1t3','day1',
                  'd2','d2t1','d2t2','d2t3','day2',
                  'd3','d3t1','d3t2','d3t3','day3',
                  'd4','d4t1','d4t2','d4t3','day4',
                  'd5','d5t1','d5t2','d5t3','day5',]
    
    def __init__(self, *args, **kwargs):
        super(DesireForm,self).__init__(*args, **kwargs)
        self.fields['day1'].empty_label = "Day"
        self.fields['day2'].empty_label = "Day"
        self.fields['day3'].empty_label = "Day"
        self.fields['day4'].empty_label = "Day"
        self.fields['day5'].empty_label = "Day"
        
    
   

class DesireFormUpdate(forms.ModelForm):

    d1 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True),required=False, empty_label=None)
    d1t1 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d1t2 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d1t3 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    day1 = forms.ModelChoiceField(queryset=Days_model.objects.all(),required=False, empty_label=None)

    d2 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True),required=False, empty_label=None)
    d2t1 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d2t2 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d2t3 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    day2 = forms.ModelChoiceField(queryset=Days_model.objects.all(),required=False, empty_label=None)

    d3 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True),required=False, empty_label=None)
    d3t1 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d3t2 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d3t3 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    day3 = forms.ModelChoiceField(queryset=Days_model.objects.all(),required=False, empty_label=None)

    d4 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True),required=False, empty_label=None)
    d4t1 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d4t2 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d4t3 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    day4 = forms.ModelChoiceField(queryset=Days_model.objects.all(),required=False, empty_label=None)

    d5 = forms.ModelChoiceField(queryset=Courses_model.objects.filter(offered = True),required=False, empty_label=None)
    d5t1 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d5t2 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    d5t3 = forms.ModelChoiceField(queryset=DT_model.objects.all(),required=False, empty_label=None)
    day5 = forms.ModelChoiceField(queryset=Days_model.objects.all(),required=False, empty_label=None)
    
    

    class Meta:
        model = Desires_model
        fields = ['d1','d1t1','d1t2','d1t3','day1',
                  'd2','d2t1','d2t2','d2t3','day2',
                  'd3','d3t1','d3t2','d3t3','day3',
                  'd4','d4t1','d4t2','d4t3','day4',
                  'd5','d5t1','d5t2','d5t3','day5',]
        
        
    def __init__(self, *args, **kwargs):
        super(DesireFormUpdate,self).__init__(*args, **kwargs)
        # self.fields['day5'].queryset = Days_model.objects.all()
        
        
        
        

        

        
        
       
class AddingCourseForm(forms.ModelForm):

    class Meta:
        model = Courses_model
        fields = "__all__"
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields['title'].label = 'Course Name'
            self.fields['number'].label = 'Course Number'
            self.fields['offered'].label = 'Course offered'
           

class AddingTomeForm(forms.ModelForm):

    class Meta:
        model = DT_model
        fields = "__all__"

class ModUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"
        fields = ['serialNumber', 'report', 'teaching', 'vip']
    
    


            
        

        
    
    
            










