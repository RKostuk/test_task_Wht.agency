from db.models import Person, Team
from db.session import Base_method
from schemas.pySchemas import TeamAddPersonSchema


class Method(Base_method):
    def add_person(self, data: TeamAddPersonSchema) -> bool:
        user = self.session.query(Person).filter_by(email=data.email).first()
        team = self.session.query(Team).filter_by(name=data.name_team).first()
        if user is not None and team is not None:
            team.members.append(user)
            self.session.commit()
            return True
        else:
            return False
