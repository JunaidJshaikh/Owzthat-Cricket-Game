import random

def Owzthat_game():
    total_balls=1
    wickets=0
    total_runs_scored=0
    batting_dice=(1,2,3,4,'out',6)
    umpire_dice=('bowled','stumped','caught','not out','no ball','lbw')
    #extra variable for easy typing
    i=total_balls
    w=wickets
    t=total_runs_scored
    #NEW VARIABLES
    F=0
    S=0
    EXTRAS=0
    DOT_BALL=0
    print('Cricket Match ''\U0001F3CF' ' Simulation \n'
          'Starting the game with 10 balls ' '\U0001F94E' ' and 2 wickets,\n')
    while(i<11 and w<2):
        c=random.choice(batting_dice)
        print('\U0001F94E:',i)

        if(c==1 or c==2 or c==3 or c==4 or c==6):
            t=t+c
            i=i+1
            if(c==4):
                print('And the ball goes tapping in to the boundary \n Thats a Four ! \n4 Runs added to the Score')
                F=F+1
            elif(c==6):
                print('And the ball goes flying in to the boundary, \n Thats a SIX ! \n 6 Runs added to the Score')
                S=S+1
            else:
                print('Runs Scored:',c)
                print(c,'Runs added to the Score')
            print('Total Runs Scored:',t,'\n')
            
        else:
            print('The Bowler Appeals ''\U0001F64B' ':',c)
            d=random.choice(umpire_dice)
            if(d=='not out'):
                
                print('Umpire Decision:',d)
                print('Not Out \n')
                DOT_BALL=DOT_BALL+1
                i=i+1
                
            elif(d=='no ball'):  
                print('Umpire Decision:',d)
                print('No Ball , ball not counted')
                print('1 Extra run given')
                t=t+1
                EXTRAS=EXTRAS+1
                print('Total Runs Scored:',t,'\n')
                print('Its a FREE HIT the bowler has to bowl that again \n')
  #FREE HIT CODE
  #USING RANDOM VARIABLES(FROM MY NAME) FOR THIS PART
                j=random.choice(batting_dice)
                if(j==1 or j==2 or j==3 or j==4 or j==6):
                    t=t+j
                    i=i+1
                    if(j==4):
                        print('And the ball goes tapping in to the boundary, That was a great use of the FREE HIT \n Thats a Four ! \n4 Runs added to the Score')
                        F=F+1
                    elif(j==6):
                        print('And the ball goes flying in to the boundary, That was a great use of the FREE HIT \n Thats a SIX ! \n 6 Runs added to the Score')
                        S=S+1
                    else:
                        print('Runs Scored:',j)
                        print(j,'Runs added to the Score')
                    print('Total Runs Scored:',t,'\n')
                    
                else:
                    print('The Bowler Appeals ''\U0001F64B' ':',j)
                    u=random.choice(umpire_dice)
                    if(u=='not out'):                      
                        print('Umpire Decision:',u)
                        print('Not Out \n')
                        DOT_BALL=DOT_BALL+1
                        i=i+1
                        
                    elif(u=='no ball'):
                        print('Umpire Decision:',u)
                        print('No Ball , ball not counted')
                        print('1 Extra run given')
                        t=t+1
                        EXTRAS=EXTRAS+1
                        print('Total Runs Scored:',t,'\n')
                        print('Its a FREE HIT AGAIN')
                        n=random.choice(batting_dice)
                        print(n)
                        if(n==1 or n==2 or n==3 or n==4 or n==6):
                            t=t+n
                            i=i+1
                            if(n==4):
                                print('And the ball goes tapping in to the boundary, That was a great use of the FREE HIT \n Thats a Four ! \n4 Runs added to the Score')
                                F=F+1
                            elif(n==6):
                                print('And the ball goes flying in to the boundary, That was a great use of the FREE HIT\n Thats a SIX ! \n 6 Runs added to the Score')
                                S=S+1
                            else:
                                print('Runs Scored:',n)
                                print(n,'Runs added to the Score')
                            print('Total Runs Scored:',t,'\n')
                            
                        else:
                            print('The Bowler Appeals ''\U0001F64B' ':',n)
                            a=random.choice(umpire_dice)
                            if(a=='not out'):
                                print('Umpire Decision:',a)
                                print('Not Out \n')
                                DOT_BALL=DOT_BALL+1
                                i=i+1
            
                            else:
                                i=i+1
                                if(a=='caught' or a=='bowled' or a=='lbw'):
                                    print('Umpire Decision:',a)
                                    print('Great work by the Bowler')
                                    print('As this was a FREE HIT, The player is NOT OUT\n')

                                elif(a=='stumped'):
                                    w=w+1
                                    print('Umpire Decision:',a)
                                    print('Straight into the Hands of the Fielder')
                                    print('The Player has to go back to the Stands\n')
                        
                    else:
                        i=i+1
                        if(u=='caught' or u=='bowled' or u=='lbw'):
                            print('Umpire Decision:',u)
                            print('Great work by the Bowler')
                            print('As this was a FREE HIT, The player is NOT OUT\n')

                        elif(u=='stumped'):
                            w=w+1
                            print('Umpire Decision:',u)
                            print('AND THATS A RUN OUT')
                            print('The Player has to go back to the Stands\n')
                
            else:
                i=i+1
                w=w+1
                if(d=='stumped' or d=='bowled' or d=='lbw'):
                    print('Umpire Decision:',d)
                    print('Great work by the Bowler')
                    print('The Player has to go back to the Stands\n')

                elif(d=='caught'):
                    print('Umpire Decision:',d)
                    print('Straight into the Hands of the Fielder')
                    print('The Player has to go back to the Stands\n')
                 
    result = '-------------Game Over-------------'
    print('Number of wickets Fallen:',w)
    print('FOURS:',F)
    print('SIXES:',S)
    print('EXTRAS:',EXTRAS)
    print('Dot Balls:',DOT_BALL)
    print('Total Runs:',t)

    return(result)   
print(Owzthat_game())


 