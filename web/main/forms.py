from django.forms import forms, fields


class Form(forms.Form):
    input_d_int = fields.IntegerField(label="kiek darbuoju dirba imoneja ?", required=True ,min_value=0)
    input_rd_int = fields.IntegerField(label="kiek riboto darbingumo darbuoju dirba imoneja ?", required=True ,min_value=0)

