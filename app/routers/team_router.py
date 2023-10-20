from fastapi import APIRouter

from db.Team import Team_method
from schemas.pySchemas import TeamDataSchema, TeamNameSchema, TeamUpdateDataSchema

from utils.utils import return_result

TM = Team_method()
team_router = APIRouter(prefix='/team', tags=['team'])


@team_router.post('/create/', status_code=200)
async def create_group(data: TeamDataSchema):
    if TM.create_team(team_name=data):
        return return_result(result=True, info='successfully create')
    else:
        return return_result(result=False, info='a team by that name has already been created')


@team_router.get('/info/', status_code=200)
async def team_info(data: TeamNameSchema):
    data_info = TM.read_team(team_name=data)
    if data_info:
        return return_result(result=True, data=data_info, info='successfully take info')
    else:
        return return_result(result=False, info='not found team')


@team_router.put('/update/', status_code=200)
async def update_user(data: TeamUpdateDataSchema):
    if TM.update_team(name=data):
        return return_result(result=True, info='successfully change')
    else:
        return return_result(result=False, info='team with name not found')


@team_router.delete('/delete/', status_code=200)
async def delete_team(data: TeamNameSchema):
    if TM.delete_team(team_name=data):
        return return_result(result=True, info='successfully delete')
    else:
        return return_result(result=False, info='team with name not found')
