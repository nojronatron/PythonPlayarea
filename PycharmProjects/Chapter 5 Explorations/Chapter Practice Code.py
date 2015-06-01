__author__ = 'Blue'

nested = ["first", ("second", "third"), ["fourth", "fifth", "sixth"]]
print("Nested has only", len(nested), "elements.")
print(nested)

print("\n")
scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
print("Scores has", len(scores), "elements.")
print(scores)

print("\nHere are the scores, by player:")
print(scores[0])
print(scores[1])
print(scores[2])

moe_Score = scores[0]
larry_Score = scores[1]
curly_Score = scores[2]

print("\nScores as assigned, by indexed variable:")
print(moe_Score[0], ": ", moe_Score[1], sep="")
print(larry_Score[0], ": ", larry_Score[1], sep="")
print(curly_Score[0], ": ", curly_Score[1], sep="")

print("\nNow direct-access to tuple contents:")
print(scores[0][0], ": ", scores[0][1], sep="")
print(scores[1][0], ": ", scores[1][1], sep="")
print(scores[2][0], ": ", scores[2][1], sep="")

input("\nPress the Enter key to exit.")
