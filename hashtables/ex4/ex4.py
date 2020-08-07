def has_negatives(a):
    
    storage = {}    
    result = []
   
    for num in a:        
        if storage.get(
                abs(num)):             
            if (storage.get(abs(num)) + num) == 0:                
                result.append(abs(num))
        else:            
            storage[abs(num)] = num
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
