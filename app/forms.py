from pyexpat import model
from attr import fields
from django import forms
from .models import Resume


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICES=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Beed','Beed')
]


class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    job_city=forms.MultipleChoiceField(label='Prefreed Job Location',choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields='__all__'
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No','email':'Email ID','profile_image':'Profile Image',
        'my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'profile_image':forms.FileInput(attrs={'class':'form-control'}),
            'my_file':forms.FileInput(attrs={'class':'form-control'}),
            # 'job_city':forms.TextInput(attrs={'class':'form-control'}),   

        }
