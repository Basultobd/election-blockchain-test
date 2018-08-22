import redis
import json


class INE(object):

    """
    Class used for emulate Electoral National Institute
    in Mexico.

    Its main objective is to give the context of the election
    providing an API for update the election general state (the
    form that I choose to call the votes number per candidate).

    """

    _ALLOWED_VOTES_PER_CITIZEN = 1
    curr_state_of_election = None

    def __init__(self):

        """
        args:
            votes_system (obj):
                Variable that emulates the election system.
                Use redis client for this
        """

        self.votes_system = redis.StrictRedis(host='localhost')
        self._initiate_state_of_election()

    def _initiate_state_of_election(self):

        """
        Initiate votes system with initial state

        """
        self.votes_system.hmset('state_of_election', {'AMLO': 0, 'MID': 0, 'ANAYA': 0})

    def _get_state_of_election_from_system(self):

        """
        Get total votes per candidate

        return:
            state_of_election (dict):
                A dict that contains the election actual state

        """
        state_of_election = self.votes_system.hgetall('state_of_election')
        return {candidate.decode('utf-8'): int(votes) for candidate, votes in state_of_election.items()}

    def update_state_of_election(self, vote):

        """
        Update election state with the information
        of a new vote.

        args:
            vote (obj):
                Object that contains all related stuff
                with user and his favourite candidate

        """
        vote = vote.to_dict()
        # TODO: Save citizen name, state and time in DB
        # Temporary
        citizen_saved = True

        # Update votes per candidate in system
        state_of_election = self._get_state_of_election_from_system()
        for candidate in state_of_election:
            state_of_election[candidate] += vote['citizen_vote'][candidate]

        votes_update_state = self.votes_system.hmset('state_of_election', state_of_election)

        update_state = False
        if citizen_saved and votes_update_state:
            # Success
            update_state = True
            # Update copy
            INE.curr_state_of_election = state_of_election

        return update_state
