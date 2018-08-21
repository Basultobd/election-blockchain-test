from datetime import datetime

class Vote(object):

	_ALLOWED_VOTES_PER_CITIZEN = 1

	def __init__(self, **kwargs):
		self.user_name = kwargs['user_name']
		self.user_state = kwargs['user_state']
		self.user_city = kwargs['user_city']
		self.vote_body = kwargs['vote_body']
		self.creation_date = str(datetime.now())
		self.source_ip = '127.0.0.1'

	def is_valid(self):
		
		""" Verify if vote_body 
		has a valid format

		"""

		validation_state = False

		vote_body = self.__dict__['vote_body']
		if isinstance(vote_body, dict):
			# Validate that only one candidate have 1 vote
			votes_number_list = list(vote_body.values())
			if (all(number >= 0 for number in votes_number_list) 
				and sum(votes_number_list) == Vote._ALLOWED_VOTES_PER_CITIZEN):
				validation_state = True

		return validation_state

	def to_dict(self):
		
		"""
		Return objetc properties in dict form

		"""
		return self.__dict__

		
		