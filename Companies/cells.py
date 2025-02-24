def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    if days == 0:
        return states
    else:
        #store present states
        present_states = states.copy()
        next_day_states = present_states.copy()
        #now change states day by day
        for i in range(1, days + 1):
            next_day_states = present_states.copy()
            # now go cell by cell
            for j in range(0,7):
                if(j == 0):
                    next_day_states[j] = 0 ^ present_states[j+1]
                elif(j == 7):
                    next_day_states[j] = 0 ^ present_states[j-1]
                else:
                    next_day_states = present_states[j-1] ^ present_states[j+1]
            present_states = next_day_states.copy()
        return present_states

if __name__ == "__main__":
    result = cellCompete([1,0,0,0,0,1,0,0],1)
    pass