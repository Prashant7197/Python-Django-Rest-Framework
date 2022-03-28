from pyexpat import model
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname','emailid','description','mobile','date_created','position')
        labels = {
            'fullname': 'Full Name',
            'emailid' : 'Email ID',
            'description' : 'Description',
            'mobile' : 'Mobile',
            'date_created' : 'Hiring Date',
            'position' : 'Position',
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        