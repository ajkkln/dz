import random
from collections import defaultdict
from typing import List

def learn(dataset: List[str]):
    model = defaultdict(list)
    start_words = []
    
    for text in dataset:
        words = text.split()
        if words: 
            start_words.append(words[0])
            for i in range(len(words) - 1):
               
                model[words[i]].append(words[i + 1])

    model["_start_"] = start_words
    return model

def generate(state, length=50) -> str:
   
    current_word = random.choice(state["_start_"])
    output_words = [current_word]
    
    for _ in range(length - 1):
        next_words = state.get(current_word)
        if not next_words:
            break 
        
        current_word = random.choice(next_words)
        output_words.append(current_word)
    
    return ' '.join(output_words)


dataset = [
   "the dog ran quickly through the park chasing after a ball",
   "a ball rolled across the park as the kids quickly chased after it",
   "they quickly ran after the ball which flew across the park",
   "in the park the dog quickly grabbed the ball and ran off"
]

model = learn(dataset)
generated_text = generate(model, length=10)
print(generated_text)

