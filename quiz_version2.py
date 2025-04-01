questions = (
    "best footballer in the world ?",
    "short from of central processing unit is ?",
    "2+2= ?",
    "what is national animal of india ?",
    "what is name of your course?")

answers = (
    "ronaldo","cpu","4","tiger","python"
)

marks = (5,4,3,2,1)  

score = 0

for i in range(len(questions)): 
    print(questions[i])         
    ans = input() 
    if ans == answers[i]: 
     score += marks[i]
        
# Display final score
print(f"your total score is: {score}")