#define a function for downward half pyramid pattern
def downward_half_pyramid(n):
    #for loop range
    for i in range(n, 0, -1):
        for j in range(i):
            #print a star for each column
            print("*", end=" ")

#print a newline
#check if working add number in function