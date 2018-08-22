from .ine import INE
from datetime import datetime


class Vote(object):

    """
    Class for vote model

    """

    def __init__(self, citizen_name, citizen_state, citizen_vote):

        """
        args:
            citizen_name (str):
                Name of the citizen

            citizen_state (str):
                Residence state of the citizen

            citizen_vote (dict):
                Citizen vote format defined for INE

        """
        self.citizen_name = citizen_name
        self.citizen_state = citizen_state
        self.citizen_vote = citizen_vote
        self.emission_date = str(datetime.now())

    def is_valid(self):

        """
        Verify if citizen_vote has a valid format

        """
        validation_state = False

        citizen_vote = self.__dict__['citizen_vote']
        if isinstance(citizen_vote, dict):
            # Validate that only one candidate have 1 vote
            votes_number_list = list(citizen_vote.values())
            if (all(number >= 0 for number in votes_number_list)
                    and sum(votes_number_list) == INE._ALLOWED_VOTES_PER_CITIZEN):
                validation_state = True

        return validation_state

    def to_dict(self):

        """
        Return objetc properties in dict form

        """
        return self.__dict__
