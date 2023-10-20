from db.models import Team, Person
from db.session import Base_method
from schemas.pySchemas import TeamDataSchema, TeamInfoSchema, TeamNameSchema, TeamUpdateDataSchema


class Team_method(Base_method):
    def create_team(self, team_name: TeamDataSchema) -> bool:
        """
        create new team
        :param team_name:TeamDataSchema
        :return: bool
        """
        team = self.session.query(Team).filter_by(name=team_name.name).first()
        if team is None:
            self.session.add(Team(name=team_name.name))
            self.session.commit()
            return True
        else:
            return False

    def read_team(self, team_name: TeamNameSchema) -> TeamInfoSchema or bool:
        """
        select info to team
        :param team_name:TeamNameSchema
        :return:TeamInfoSchema or bool
        """
        team = self.session.query(Team).filter_by(name=team_name.team_name).first()
        if team is not None:
            user_list = self.session.query(Person).filter_by(team_id=team.id).all()
            data = {
                'team_name': team.name,
                'members': user_list
            }
            return data
        else:
            return False

    def update_team(self, name: TeamUpdateDataSchema) -> bool:
        """
        change name
        :param name:TeamUpdateDataSchema
        :return:bool
        """
        user = self.session.query(Team).filter_by(name=name.team_name).first()
        if user is not None:
            user.name = name.new_team_name
            self.session.commit()
            return True
        else:
            return False

    def delete_team(self, team_name: TeamNameSchema) -> bool:
        """
        delete data person
        :param team_name:TeamNameSchema
        :return:bool
        """
        team = self.session.query(Team).filter_by(name=team_name.team_name).first()
        if team is not None:
            self.session.delete(team)
            self.session.commit()
            return True
        else:
            return False
