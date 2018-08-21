from datetime import datetime

class Vote(object):

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

		validation_state = True

		vote_body = self.__dict__['vote_body']
		if not isinstance(vote_body, dict):
			validation_state = False
		
		# Validate that only one candidate have 1 vote
		if list(vote_body.values()).count(1) is not 1:
			validation_state = False

		return validation_state

	def to_dict(self):
		return self.__dict__

		
		