from flask_wtf import FlaskForm 
from wtforms import SelectField, BooleanField

class OrderEditForm(FlaskForm):
    status = SelectField('Status', choices=[
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ])
    is_paid = BooleanField('Is Paid')