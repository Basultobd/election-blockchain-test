
import hashlib
from datetime import datetime
import json

class VotesContainer(object):

	_MAX_VOTES_PER_CONTAINER = 5
	
	def __init__(self, **args):
		self.id = args['id']
		self.container = []
		self.previous_hash = args['previous_hash']
		self.proof = 0 
		self.creation_timestamp = str(datetime.now())

	def add_vote(self, vote):
		self.container.append(vote)

	def is_full(self):
		return len(self.container) == Block._MAX_VOTES_PER_CONTAINER

	def is_valid(self):
		return 0

	def hash(self):
		
		"""
		Creates a SHA-256 hash of a Block

		We must make sure that the Dictionary is
		Ordered, or we'll have inconsistent hashes
		"""

		block_string = json.dumps(self.__dict__, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	def is_valid_hash(self):
		return 0