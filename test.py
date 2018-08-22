from src.votes_container import VotesContainer
from src.vote import Vote
from src.ine import INE


def test():

    votes_container = VotesContainer(id=1, previous_hash=0)
    ine = INE()

    vote = Vote(
        citizen_name='Daniel',
        citizen_state='Yucatan',
        citizen_vote={'AMLO': 1, 'MID': 0, 'ANAYA': 0}
    )

    if vote.is_valid():
        ine.update_state_of_election(vote)

    vote2 = Vote(
        citizen_name='Diego',
        citizen_state='Yucatan',
        citizen_vote={'AMLO': 0, 'MID': 1, 'ANAYA': 0}
    )

    if vote2.is_valid():
        ine.update_state_of_election(vote2)

    vote3 = Vote(
        citizen_name='Daniel',
        citizen_state='Yucatan',
        citizen_vote={'AMLO': 0, 'MID': 0, 'ANAYA': 1}
    )

    if vote3.is_valid():
        ine.update_state_of_election(vote3)

    print(INE.curr_state_of_election)

    # if vote.is_valid():
    #     INE.update_state_of_election(vote)
    #     vote_id = blockchain.current_votes_container.add_vote(vote.to_dict())
    #     if blockchain.current_votes_container.is_full():
    #         notifier.notify_nodes(event='mine_container')
    #     response = {'message': f'vote added to container {vote_id}'}
    # else:
    #     response = {'message': f'vote format is not valid'}

    # return  jsonify(response, 200)


if __name__ == '__main__':
    test()
