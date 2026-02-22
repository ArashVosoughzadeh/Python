scores = {"Alice": 85, "Bob": 92, "charlie": 78}
          
max_key = max(scores, key=scores.get)
print(max_key)