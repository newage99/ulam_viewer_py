#! /usr/bin/python3
import math

def getPrimes(start,stop,prev_primes):

    if start < 2:
        start = 2

    if start == 2:

        values = [True] * (stop)
        values[1] = False

        for i in range(2,math.ceil(math.sqrt(stop))):

            if values[i] == True:

                for j in range(i*i,stop,i):

                    values[j] = False

        del values[0]

    else:

        #for i in prev_primes:
            #print(i)

        values = [True] * (stop-start)
        sqrt = math.ceil(math.sqrt(stop))

        for i in prev_primes:

            if i > sqrt:
                break

            startt = start
            while(startt%i):
                startt += 1
                
            for j in range(startt,stop,i):

                    values[j-start] = False
        

    return values
