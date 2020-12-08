My attempts at the 2020 Advent of Code challenge

Challenge one approach - need to find two numbers in a list that added together = 2020. First split the list into numbers > 1010 and numbers < 1010: then test each number in one list against the other (since we know that numbers in the same list can't = 2020). Part 2 - need to find three numbers in a list that added together = 2020. We stort the list, then start with the biggest number and smallest number. We then try adding those two, together with the middle number (from smallest to biggest). When the sum of all three > 2020, we break out, pick the next smallest number, and go round again. When we find the three that == 2020 we exit.

Challenge two approach - string parsing using simple regex to make sure each password has the correct number of occurances of key letter. Second part is trickier, need to be very careful with list lengths and indexing. Also note that the passwords can be shorter than the first required letter position, or the second required position.

Challenge three approach - split 'map' of hillside in to list, step through each 'level' of the hillside, looping when you get to an edge. Remembering that computers count from 0, and lists have line return characters. The hardest part is indexing lists.

Challenge four approach - key value pairs screams dictionary in python. The data is a complete jumble though, we'll have to add null values for missing data, and can't rely on any of it for a UID. Also need to be careful about sorting and comparing key lists, and eof.