'''
    Math

    https://leetcode.com/discuss/interview-question/815119/grab-codility-online-test-question

    When John gambles at the casino, he always uses a special system of tactics that he devised himself. Its based on always betting in one of two ways in each game: 
    • betting exactly one chip (to test his luck); 
    • betting all-in (he bets everything he has). 

    Wins in the casino are paid equal to the wager, so if he bets C chips and wins, he gets 2C chips back. If he loses, he doesn't get any chips back. It was a very lucky day yesterday and John won every game he played, starting with one chip and leaving the casino with N chips. We also know that John played all-in no more than K times. Your task is to calculate the smallest possible number of rounds he could have played. Note: betting just one chip is never considered playing all-in. 

    Write a function: public func solution(_ N Int, _ K : Int) -› Int 
'''


import math

def gamble(N, K):
    count = 0
    if N % 2 == 1:
        N -= 1
        count += 1
    if N >= 2**K:
        N /= 2**K
        count += K
        return count + N - 1
    else:
        return count + math.log(N, 2)