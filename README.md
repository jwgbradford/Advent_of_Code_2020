My attempts at the 2020 Advent of Code challenge

Challenge one approach - need to find two numbers in a list that added together = 2020. First split the list into numbers > 1010 and numbers < 1010: then test each number in one list against the other (since we know that numbers in the same list can't = 2020)

Challenge two approach - need to find three numbers in a list that added together = 2020. We stort the list, then start with the biggest number and smallest number. We then try adding those two, together with the middle number (from smallest to biggest). When the sum of all three > 2020, we break out, pick the next smallest number, and go round again. When we find the three that == 2020 we exit.