#! /usr/bin/python3
import sys, math, time
from PIL import Image
from primes import getPrimes

NUMBERS_LIMIT = 90000000

def main():

    max_number = 0

    if len(sys.argv) > 1:
        max_number = int(sys.argv[1])

    if max_number > 1:

        # We calculate the image dimensions depending on the number specified in the first argument
        salir = False
        comp = 1
        summ = 1
        wh = 0
        offset_x = 0
        offset_y = 0

        while salir == False:
            if(max_number >= comp and max_number < (comp+summ)):
                wh+=1
                salir = True
            else:
                wh+=1
                comp += summ
                summ += 2

        if wh % 2 == 0:
            offset_x = (wh/2)-1;
            offset_y = (wh/2);
        else:
            offset_x = (wh-1)/2;
            offset_y = offset_x;

        ini_x = offset_x
        ini_y = offset_y

        print("wh: %d" % wh)
        print("offset_x: %d" % offset_x)
        print("offset_y: %d" % offset_y)

        # We create a blank image
        img = Image.new('1', (wh,wh))
        pix = img.load()
        
        cont = 0
        times = 1
        cont_2_veces = 0
        dirr = 0
        lo_que_lleva = 0
        lo_que_resta = max_number
        delta = math.ceil(max_number/NUMBERS_LIMIT)
        num_of_primes = 0
        sqrt_all = math.floor(math.sqrt(max_number))
        primes = [0] * sqrt_all
        start = time.time()

        for i in range(delta):

            limit = NUMBERS_LIMIT            

            if lo_que_resta < NUMBERS_LIMIT:
                limit = lo_que_resta

            lo_que_lleva_end = lo_que_lleva + limit

            print("lo_que_lleva: "+str(lo_que_lleva))
            print("lo_que_lleva_end: "+str(lo_que_lleva_end))
            
            primeList = getPrimes(lo_que_lleva,lo_que_lleva_end,primes[:num_of_primes])

            limit_range = limit
            if lo_que_lleva == 0:
                limit_range -= 1

            for j in range(limit_range):

                if primeList[j] == True:
                    pix[offset_x,offset_y] = 1
                    if primes[num_of_primes-1] < sqrt_all:
                        primes[num_of_primes] = j+1+lo_que_lleva
                        num_of_primes += 1
                else:
                    pix[offset_x,offset_y] = 0
                
                if cont == times:
                    if cont_2_veces == 0:
                        cont_2_veces += 1
                    elif cont_2_veces == 1:
                        times += 1
                        cont_2_veces = 0
                    dirr += 1
                    cont = 0
                    
                cont += 1
                dirr = dirr % 4

                if dirr == 0:
                    offset_x += 1
                elif dirr == 1:
                    offset_y -= 1
                elif dirr == 2:
                    offset_x -= 1
                elif dirr == 3:
                    offset_y += 1

            lo_que_lleva = lo_que_lleva_end
            lo_que_resta -= limit
            primeList = []

        done = time.time()

        print("time: "+str(done-start))

        img.save("ulam.png")
        img.show()
    

if __name__ == "__main__":
    main()
