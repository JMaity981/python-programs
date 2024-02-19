def game():
    score=int(input("Enter Your score= "))
    return score

score=game()
with open("Highscore.txt")as f:
    highscore=int(f.read())

if highscore<score:
    with open("Highscore.txt","w")as f:
        f.write(str(score))