from django.forms import forms, fields


class Form(forms.Form):
    input_int = fields.IntegerField(label="int field", required=True ,min_value=0)
