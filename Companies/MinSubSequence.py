def lengthEachScene(inputList):
    # WRITE YOUR CODE HERE
    length = len(inputList)
    hm_all = {}
    # form the hashmap all the shot labels
    for i in range(length):
        shot_label = inputList[i]
        if shot_label in hm_all:
            hm_all[shot_label] = hm_all[shot_label] + 1
        else:
            hm_all[shot_label] = 1
    # use two pointers
    i = 0 
    j = 0 
    result_min_sub_seq = []
    while i<=j and i < length and j < length:
        shot_label = inputList[i]
        if hm_all[shot_label] > 1:
            no_of_occurences = hm_all[shot_label]
            # extend the sub sequence until all this shot_label are found
            while no_of_occurences != 1:
                j += 1 
                if inputList[j] == shot_label:
                    no_of_occurences -= 1 
            # see if you can extend more by checking the neighbouring characters
            # hashmap of this sequence till now
            hm_this = {}
            for k in range(i,j+1):
                shot_label = inputList[k]
                if shot_label in hm_this:
                  hm_this[shot_label] = hm_this[shot_label] + 1
                else:
                    hm_this[shot_label] = 1
            while True:
                if j+1 == length:
                    break   
                next_shot_label = inputList[j+1]
                if next_shot_label in hm_this:
                    j += 1 
                    hm_this[next_shot_label] += 1 
                else:
                    break
        this_sub_seq_len = j - i + 1
        result_min_sub_seq.append(this_sub_seq_len)
        i = j + 1 
        j = i
    return result_min_sub_seq

result = lengthEachScene(['a','b','c','d','a','e','f','g','h','i','j','e'])