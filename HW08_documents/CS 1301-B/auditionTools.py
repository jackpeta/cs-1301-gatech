def calculateScore(scoreList):
    threeMultipliers = [5, 2, 4]
    totalScore = 0
    for i in range(len(scoreList)):
         totalScore += (scoreList[i] * threeMultipliers[i % 3])
    return totalScore
