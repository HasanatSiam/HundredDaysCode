def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = sum(combined_names.count(letter) for letter in 'true')
    # print(type(true_count))
    love_count = sum(combined_names.count(letter) for letter in 'love')
    love_score = int(f'{true_count}{love_count}')
    print(love_score)
    

name1 = input("Enter the name of first person: ") 
name2 = input("Enter the name of second person: ") 
calculate_love_score(name1, name2)