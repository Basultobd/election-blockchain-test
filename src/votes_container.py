
import hashlib
from datetime import datetime
import json

class VotesContainer(object):

	_MAX_VOTES_PER_CONTAINER = 5
	
	def __init__(self, **args):

		"""

		args:
			id (str):
				The id for the container
			previous_container_hash:
				A SHA-256 hash corresponding 
				to previous container 

		"""

		self.id = args['id']
		self.container = []
		self.previous_container_hash = args['previous_hash']
		self.proof = 0 
		self.creation_timestamp = str(datetime.now())

	def add_vote(self, vote):
		
		"""
		Add a vote to the container

		args:
			vote (obj):
				A single vote object
		"""
		self.container.append(vote)

	def is_full(self):

		"""
		Verificate if the contianer id full of votes

		return:
			is_full (bool):
				Boolean that indicates if
				the state of the container

		"""
		is_full = len(self.container) == Block._MAX_VOTES_PER_CONTAINER
		return is_full

	def is_valid(self):

		"""
		Validate if votes inside container
		have a valid format

		"""

		return NotImplementedError

	def hash(self):
		
		"""
		Creates a SHA-256 hash of a container (block)

		We must make sure that the Dictionary is
		Ordered, or we'll have inconsistent hashes
		"""

		container_str = json.dumps(self.__dict__, sort_keys=True).encode()
		return hashlib.sha256(container_str).hexdigest()

	def is_valid_hash(self):

		"""
		Validate if container hash is valid
		
		"""
		return NotImplementedError
		