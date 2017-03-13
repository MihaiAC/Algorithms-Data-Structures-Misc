from matplotlib import pyplot
from functools import partial
import timeit
import random

class Plotter:
    #generator = generates a list of appropiate arguments for the function, based on the previous list of arguments
    #func = function of which the runtime will be measured
    #n = number of plot points (executions of function func)
    def plotter(func,generator,n):
        x = range(1,n)
        y = []
        argss = []
        for i in x:
            argss = generator(argss)
            #By increasing "number", the plot gets smoother, but takes longer to generate.
            #"number" = number of times the timing is repeated.
            y.append(timeit.timeit(partial(func,argss), number = 20))
    
        #Plot the graph:
        pyplot.plot(x,y)
        pyplot.show()

def gen(lst):
    lst.append(random.randint(1,1000))
    return lst

#Selection sort:
def func(lst):
    for i in range(0,len(lst) - 1):
        minim = i
        for j in range(i+1,len(lst) - 1):
            if(lst[j] < lst[minim]):
                minim = j
        if(minim != i):
            aux = lst[i]
            lst[i] = lst[minim]
            lst[minim] = aux
    




def main():
    Plotter.plotter(func,gen,100)

if __name__ == '__main__':
    main()