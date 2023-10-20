from pydantic import EmailStr

from db.models import Person
from db.session import Base_method
from schemas.pySchemas import PersonDataSchema, PersonInfoTeamSchema, EmailDataSchema, PersonUpdateDataSchema


class Person_method(Base_method):
    def create_person(self, person: PersonDataSchema) -> bool:
        """
        create new user add in db
        :param person:PersonCreate
        :return: bool
        """
        user = self.session.query(Person).filter_by(email=person.email).first()
        if user is None:
            self.session.add(Person(
                name=person.name,
                surname=person.surname,
                email=person.email
            ))
            self.session.commit()
            return True
        else:
            return False

    def read_person(self, email_data: EmailDataSchema) -> PersonInfoTeamSchema or bool:
        """
        selec data person
        :param email_data: EmailDataSchema
        :return: PersonInfoTeamSchema or bool
        """
        user = self.session.query(Person).filter_by(email=email_data.email).first()
        if user:
            data = {
                'name': user.name,
                'surname': user.surname,
                'email': user.email,
                'team': user.team,
            }
            return data
        else:
            return False

    def update_person(self, email_data: PersonUpdateDataSchema) -> bool:
        """
        change email address
        :param email_data: PersonUpdateDataSchema
        :return: bool
        """
        user = self.session.query(Person).filter_by(email=email_data.email).first()
        if user is not None:
            user.email = email_data.new_email
            self.session.commit()
            return True
        else:
            return False

    def delete_person(self, email_data: EmailDataSchema) -> bool:
        """
        delete data person
        :param email_data:EmailDataSchema
        :return:bool
        """
        user = self.session.query(Person).filter_by(email=email_data.email).first()
        if user is not None:
            self.session.delete(user)
            self.session.commit()
            return True
        else:
            return False
