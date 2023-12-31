from pydantic import BaseModel, EmailStr
from typing import List


class EmailDataSchema(BaseModel):
    email: EmailStr

class PersonDataSchema(EmailDataSchema):
    name: str
    surname: str

class PersonInfoTeamSchema(PersonDataSchema):
    team: str

class TeamDataSchema(BaseModel):
    name: str

class TeamNameSchema(BaseModel):
    team_name: str

class TeamAddPersonSchema(BaseModel):
    email: EmailStr
    name_team: str

class PersonUpdateDataSchema(BaseModel):
    email: EmailStr
    new_email: EmailStr

class TeamUpdateDataSchema(BaseModel):
    team_name: str
    new_team_name: str

class TeamInfoSchema(BaseModel):
    team_name: str
    members: List[str]

class ResponseSchema(BaseModel):
    result: bool
    info: str = None
    data: dict = None
