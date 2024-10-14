from fastapi import FastAPI
from pydantic import BaseModel
from sqladmin import Admin, ModelView

from admin.auth import authentication_backend
from db.base import engine
from db.crud.payments import create_payment_db
from db.models import modelviews

app = FastAPI()
admin_app = Admin(app, engine, authentication_backend=authentication_backend)


class NewPaymentData(BaseModel):
    user_id: int
    payment_id: str
    amount: int


@app.get('/ping')
def ping():
    return {'ping': 'pong'}


@app.post('/payment')
def create_payment_api(payment: NewPaymentData):
    res = create_payment_db(
        payment.payment_id,
        payment.user_id,
        payment.amount
    )
    return res.model_dump()


for model in modelviews:
    class UserAdmin(ModelView, model=model['model']):
        column_list = model['column_list']
        column_searchable_list = model['column_list']
        column_sortable_list = model['column_list']
        icon = model['icon']
        name = model['name']
        name_plural = model['name_plural']
        form_overrides = model.get('form_overrides')
        column_formatters = model.get('column_formatters', {})
    admin_app.add_view(UserAdmin)
