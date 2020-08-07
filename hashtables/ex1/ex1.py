def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}  
    if length <=1:
        print("Error! Too short")
        return None


    for i in range(length):
        c = weights[i]
        if c in dict:
            prev = dict[c]
            return(i,prev)    
        dict[limit - weights[i]] = i
    return None


weights = [2, 3, 5, 10, 15]
print(get_indices_of_item_weights(weights, 5, 21))
