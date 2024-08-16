""" User will tell how many times to toss the coin based on that use random function to do those many tosses, outcome is 0 or 1.
count number of 1's and 0's and plot the graph for each. """
import random
import matplotlib.pyplot as plt
def coin(n):
    heads=0
    tails=0
    for i in range(n):
        x= random.randint(0,1)
        if x==1:
            heads+=1
        else:
            tails+=1
    # for plotting the results
    labels = ['Heads', 'Tails']
    counts = [heads,tails]
    plt.bar(labels,counts,color=['blue','green'])
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.title(f'Results of {n} Coin Tosses')

    #for adding counts on top of the bars
    for i,count in enumerate(counts):
        plt.text(i,count+0.05,str(count),ha='center',va='bottom')
    plt.show()
        
n=int(input("enter the number of tosses you want me to do: "))
coin(n)