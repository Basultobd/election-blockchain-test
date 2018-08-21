from votes_container import VotesContainer
from vote import Vote
from ine import INE

def main():
    votes_container = VotesContainer(id=1, previous_hash=0)

    ine = INE()

    vote = Vote(
        user_name='Daniel',
        user_state='Yucatan',
        user_city='Merida',
        vote_body={'AMLO':1, 'MID':0, 'ANAYA':0}
    )

    if vote.is_valid():
        ine.update_votes_per_candidate(vote.to_dict())

    vote2 = Vote(
        user_name='Diego',
        user_state='Yucatan',
        user_city='Merida',
        vote_body={'AMLO':0, 'MID':1, 'ANAYA':0}
    )

    if vote2.is_valid():
        ine.update_votes_per_candidate(vote2.to_dict())

    vote3 = Vote(
        user_name='Daniel',
        user_state='Yucatan',
        user_city='Merida',
        vote_body={'AMLO':0, 'MID':0, 'ANAYA':1}
    )

    if vote3.is_valid():
        ine.update_votes_per_candidate(vote3.to_dict())

    # if vote.is_valid():
    #     INE.update_election_state(vote)
    #     vote_id = blockchain.current_votes_container.add_vote(vote.to_dict())
    #     if blockchain.current_votes_container.is_full():
    #         notifier.notify_nodes(event='mine_container')
    #     response = {'message': f'vote added to container {vote_id}'}
    # else:
    #     response = {'message': f'vote format is not valid'}

    # return  jsonify(response, 200)


if __name__ == '__main__':
    main()