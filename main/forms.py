from django import forms
from .models import Todo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout ,Row,Div,Field


class AddTodoForm(forms.ModelForm):

    class Meta:
        model=Todo
        fields=['todo_desc','due_date','priority']

    def __init__(self, *args, **kwargs):
         super(AddTodoForm, self).__init__(*args, **kwargs)
         self.helper=FormHelper(self)
         self.fields['todo_desc'].label=False
         self.fields['due_date'].label=False
         self.fields['priority'].label=False
         
         self.helper.layout=Layout(

             Div(
             Div(Field( 'todo_desc', placeholder="Enter Your current Profession" ),css_class='hunwidth'),
             Div(Field('due_date',placeholder='Enter the Due Date'),css_class='hunwidth'),
             Div(Field('priority'),css_class='hunwidth'),
             
             css_class='col-xl-12',
             ),
             
         )