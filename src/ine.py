import redis
import json


class INE(Object):

    """
    Class used for emulate Electoral National Institute
    in Mexico.

    Its main objective is to give the context of the election
    providing an API for update the election general state (the
    form that I choose to call the votes number per candidate).

    """

    _ALLOWED_VOTES_PER_CITIZEN = 1

    def __init__(self):

        """
        args:
            votes_system (obj):
                Variable that emulates the election system.
                Use redis cloient for this

            curr_votes_per_candidate (dict):
                Updated copy of actual election state

        """

        self.votes_system = redis.StrictRedis(host='localhost')
        self.curr_votes_per_candidate = None
        self._initiate_election_state()

    def _initiate_election_state(self):

        """
        Initiate votes system with initial state

        """
        self.votes_system.hmset('votes_per_candidate', {'AMLO': 0, 'MID': 0, 'ANAYA': 0})

    def get_election_state(self):

        """
        Get total votes per candidate

        return:
            votes_per_candidate (dict):
                A dict that contains the election actual state

        """
        votes_per_candidate = self.votes_system.hgetall('votes_per_candidate')
        return {candidate.decode('utf-8'): int(votes) for candidate, votes in votes_per_candidate.items()}

    def update_election_state(self, vote):

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
        votes_per_candidate = self.get_election_state()
        for candidate in votes_per_candidate:
            votes_per_candidate[candidate] += vote['citizen_vote'][candidate]

        votes_update_state = self.votes_system.hmset('votes_per_candidate', votes_per_candidate)

        return citizen_saved and votes_update_state
