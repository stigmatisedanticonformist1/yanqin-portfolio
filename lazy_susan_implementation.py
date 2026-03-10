
from lazy_susan import *



def solve_trivial_2(table):
    if get_table_state(table)==(1,0) or get_table_state(table)==(0,1):
        flip_coins(table, (1,0))
    

# test:
#t2_1 = create_table(2)
#solve_trivial_2(t2_1)
#run ( t2_1 , solve_trivial_2 )

#print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################







def solve_trivial_4(table):
    flip_coins(table, get_table_state(table))

# test:
#t4_2 = create_table(4)
#solve_trivial_4(t4_2)
#print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t4_2_run = create_table(4)
#run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################






def solve_2(table):
    if check_solved(table) == True:
        return table
    else:
        flip_coins(table,(1,0))

# test:
#t2_3 = create_table(2)
#solve_2(t2_3)
#print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t2_3_run = create_table(2)
#run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





def solve_4(table):
    A=(1,0,1,0)
    B=(1,1,0,0)
    C=(1,0,0,0)
    to_flip=(None, A, B, A, C, A, B, A)
    for element in to_flip:
        if element is not None:
            flip_coins(table, element)
        if check_solved(table):
            return table
    
# test:
#t4_4 = create_table(4)
#solve_4(t4_4)
#print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

#t4_4_run = create_table(4)
#run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

#t4_4_susan = create_table(4)
#Susan(t4_4_susan)

########################################################






def solve(table):
    size = get_table_size(table)
    if size == 1:
        return table
    if check_solved(table):
        return table
    if size <= 0 or (size & (size - 1)) != 0:
        return None
    if size == 2:
        flip_coins(table, (1,0))
        return table
    A=(1,0,1,0)
    B=(1,1,0,0)
    C=(1,0,0,0)
    moves = {1: A, 2: B, 3: C}
    current_size=4
    while current_size<size:
        half=current_size
        Full = (1,)*half
        Blank = (0,)*half
        new_moves={}
        for d in range(1,half):
            old=moves[d]
            new_moves[d]=2*old
        new_moves[half]=Full + Blank
        for d in range(1, half):
            new_moves[half + d] = moves[d] + Blank
        moves = new_moves
        current_size*=2
    num_disks=size-1
    total_moves=2**num_disks - 1
    for k in range(1, total_moves + 1):
        x = k
        disk = 1
        while x % 2 == 0:
            x //= 2
            disk += 1
        flip_coins(table, moves[disk])
        if check_solved(table):
            return table
    

# test:
t4_5 = create_table(2)
solve(t4_5)
#print(check_solved(t4_5))



t8_5 = create_table(8)
solve(t8_5)
#run(t8_5, solve)
#print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
#print(check_solved(t16_5))



    

