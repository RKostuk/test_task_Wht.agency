from fastapi import APIRouter

from db.Person import Person_method
from db.Team import Team_method
from db.person_team_method import Method
from schemas.pySchemas import PersonDataSchema, TeamDataSchema, TeamAddPersonSchema, TeamNameSchema, \
    TeamUpdateDataSchema, EmailDataSchema, PersonUpdateDataSchema

from utils.utils import return_result

Method = Method()
PM = Person_method()
TM = Team_method()
router = APIRouter()


@router.get("/", status_code=200)
async def root():
    return {
        "result": "working"
    }


@router.post('/user_add/', status_code=200)
async def add_user(data: PersonDataSchema):
    if PM.create_person(person=data):
        return return_result(result=True, info='successfully add user')
    else:
        return return_result(result=False, info='the user with this email is registered')


@router.get('/user_info/', status_code=200)
async def info_user(data: EmailDataSchema):
    data_info = PM.read_person(email_data=data)
    if data_info is not False:
        return return_result(result=True, data=data_info)
    else:
        return return_result(result=False, info='user with this email was not found')


@router.put('/user_update_email/', status_code=200)
async def update_user(data: PersonUpdateDataSchema):
    if PM.update_person(email_data=data):
        return return_result(result=True, info='successfully change')
    else:
        return return_result(result=False, info='user with email not found')


@router.delete('/user_delete/', status_code=200)
async def delete_user(data: EmailDataSchema):
    if PM.delete_person(email_data=data):
        return return_result(result=True, info='successfully delete')
    else:
        return return_result(result=False, info='user with email not found')

@router.post('/team_create/', status_code=200)
async def create_group(data: TeamDataSchema):
    if TM.create_team(team_name=data):
        return return_result(result=True, info='successfully create')
    else:
        return return_result(result=False, info='a team by that name has already been created')

@router.get('/team_info/', status_code=200)
async def team_info(data: TeamNameSchema):
    data_info = TM.read_team(team_name=data)
    if data_info:
        return return_result(result=True, data=data_info, info='successfully take info')
    else:
        return return_result(result=False, info='not found team')

@router.put('/team_update/', status_code=200)
async def update_user(data: TeamUpdateDataSchema):
    if TM.update_team(name=data):
        return return_result(result=True, info='successfully change')
    else:
        return return_result(result=False, info='team with name not found')

@router.delete('/team_delete/', status_code=200)
async def delete_team(data: TeamNameSchema):
    if TM.delete_team(team_name=data):
        return return_result(result=True, info='successfully delete')
    else:
        return return_result(result=False, info='team with name not found')

@router.post('/add_user_to_team/', status_code=200)
async def add_user_to_team(data: TeamAddPersonSchema):
    if Method.add_person(data=data):
        return return_result(result=True, info='successfully add')
    else:
        return return_result(result=False, info='Eror add person')

