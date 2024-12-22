from typing import Tuple
def pull(n: int) -> Tuple[int, int]:
    min_4_star = 0
    min_5_star = 0
    
   
    min_5_star = n // 90
    
    
    min_4_star = n // 10
    min_4_star = min_4_star - min_5_star 
    return min_4_star, min_5_star


print(pull(24))  

