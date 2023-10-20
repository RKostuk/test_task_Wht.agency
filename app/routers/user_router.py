from fastapi import APIRouter

from db.Person import Person_method
from db.Team import Team_method
from db.person_team_method import Method
from schemas.pySchemas import (
    PersonDataSchema,
    TeamAddPersonSchema,
    EmailDataSchema,
    PersonUpdateDataSchema, ResponseSchema
)

from utils.utils import return_result

Method = Method()
PM = Person_method()
TM = Team_method()
user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.post('/create/', status_code=200, response_model=ResponseSchema)
async def add_user(data: PersonDataSchema):
    if PM.create_person(person=data):
        return return_result(result=True, info='successfully add user')
    else:
        return return_result(result=False, info='the user with this email is registered')


@user_router.get('/info/', status_code=200, response_model=ResponseSchema)
async def info_user(data: EmailDataSchema):
    data_info = PM.read_person(email_data=data)
    if data_info is not False:
        print(data_info)
        return return_result(result=True, data=data_info)
    else:
        return return_result(result=False, info='user with this email was not found')


@user_router.put('/update_email/', status_code=200, response_model=ResponseSchema)
async def update_user(data: PersonUpdateDataSchema):
    if PM.update_person(email_data=data):
        return return_result(result=True, info='successfully change')
    else:
        return return_result(result=False, info='user with email not found')


@user_router.delete('/delete/', status_code=200, response_model=ResponseSchema)
async def delete_user(data: EmailDataSchema):
    if PM.delete_person(email_data=data):
        return return_result(result=True, info='successfully delete')
    else:
        return return_result(result=False, info='user with email not found')


@user_router.post('/add_to_team/', status_code=200, response_model=ResponseSchema)
async def add_user_to_team(data: TeamAddPersonSchema):
    if Method.add_person(data=data):
        return return_result(result=True, info='successfully add')
    else:
        return return_result(result=False, info='Eror add person')
