questions = [
    ["Who is the long-time host of the TV show 'Kaun Banega Crorepati'?", #Questions
     "A. Shah Rukh Khan",
     "B. Amitabh Bachchan",
     "C. Salman Khan",
     "D. Aamir Khan",
     "B"],

    ["In which year did 'Kaun Banega Crorepati' first air in India?",
     "A. 1995",
     "B. 1998",
     "C. 2000",
     "D. 2005",
     "C"],

    ["What is the capital city of India?",
     "A. Mumbai",
     "B. New Delhi",
     "C. Kolkata",
     "D. Chennai",
     "B"],

    ["Which Indian festival is known as the 'Festival of Lights'?",
     "A. Holi",
     "B. Eid",
     "C. Diwali",
     "D. Pongal",
     "C"],

    ["Who is known as the 'Father of the Indian Constitution'?",
     "A. Mahatma Gandhi",
     "B. Jawaharlal Nehru", 
     "C. B. R. Ambedkar",
     "D. Sardar Patel",
     "C"],

    ["Which sport is the Indian Premier League (IPL) associated with?",
     "A. Football",
     "B. Hockey",
     "C. Cricket",
     "D. Tennis",
     "C"],

    ["What is the national animal of India?",
     "A. Lion",
     "B. Tiger",
     "C. Elephant",
     "D. Peacock",
     "B"],

    ["Which river is considered the holiest in Hinduism?",
     "A. Yamuna",
     "B. Ganga",
     "C. Godavari",
     "D. Narmada",
     "B"],

    ["Who was the first Prime Minister of independent India?",
     "A. B. R. Ambedkar",
     "B. Indira Gandhi",
     "C. Rajendra Prasad",
     "D. Jawaharlal Nehru",
     "D"],

    ["The currency of India is called:",
     "A. Rupee",
     "B. Dollar",
     "C. Taka",
     "D. Ringgit",
     "A"]
]


for question in questions:       #options from questions in a,b,c,d
    print(question[0])
    print(f'{question[1]}')
    print(f'{question[2]}')
    print(f'{question[3]}')
    print(f'{question[4]}')

#input answer and verify if its correct or not

    a=input("Choose the correct option A,B,C,D: ").upper().strip()
    if(a==question[5]):
        print("Congratulations! your answer was correct ")
        
    else:
        print(f"Incorrect answer! the correct answer was {question[5]}")
        print("Best of luck next time!")
        break
    
