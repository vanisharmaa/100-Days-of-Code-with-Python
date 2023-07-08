def turn_right() :
    turn_left()
    turn_left()
    turn_left()

while front_is_clear() : # for cases when there is an empty square and the right is always clear and reeborg gets stuck in a loop.
    move()
turn_left() #now there is a wall in front, make that wall in right but turning reeborg to left.
# turning left or not doesn't matter much, turning left will make reeborg reach there faster.
while not at_goal() :
    if right_is_clear() :
        turn_right()
        move()
    elif front_is_clear() :
        move()
    else : 
        turn_left()
        
