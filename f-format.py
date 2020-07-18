candidate_vote = int(input('How many votes did the candidate get?'))
total_vote = int(input('What is the total amount of votes?'))

message_to_candidate = (
    f"You received {candidate_vote} number of votes \n"
    f"The total number of votes in the election was {total_vote} \n"
    f"You received {candidate_vote/total_vote*100:.2f}% of the votes"
)

print(message_to_candidate)
