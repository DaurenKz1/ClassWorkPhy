def show_multiply_table(num,i=1):
    print("%d x %d  = %d " % (num,i,num*i) )
    if i < 10:
        show_multiply_table(num, i+1)
    return 
show_multiply_table(6)