import redis


class INE():

	"""
	Class used for emulate Electoral National Institute
	in Mexico.

	Its main objective is to give the context of the election
	providing an API for update the election general state (the 
	form that I choose to call the votes number per candidate).

	"""
	
	def __init__(self):
		self._votes_system = redis.StrictRedis(host='localhost')
		self.initiate_votes_counter()

	def initiate_votes_counter(self):
		self._votes_system.hmset('votes_per_candidate', {'AMLO':0, 'MID': 0, 'ANAYA': 0})

	def get_votes_per_candidate(self):
		votes_state = self._votes_system.hgetall('votes_per_candidate')
		return {candidate.decode('utf-8'): int(votes) for candidate, votes in votes_state.items()}

	def update_votes_per_candidate(self, vote):

		"""
		Update election state with the information
		of a new vote.

		args:
			vote (obj):
				Object that contains all related stuff
				with user and his favourite candidate

		"""
		votes_per_candidate = self.get_votes_per_candidate()
		for candidate in votes_per_candidate:
			votes_per_candidate[candidate] += vote['vote_body'][candidate]

		# Update votes per candidate in system
		self._votes_system.hmset('votes_per_candidate', votes_per_candidate)
		

		