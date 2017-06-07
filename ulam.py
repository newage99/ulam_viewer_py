#! /usr/bin/python3
import sys, math
from PIL import Image

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

        # We create a list of booleans that'll represent if this index is prime or not
        primes = [True] * (max_number+1)
        primes[0] = False
        primes[1] = False

        # We delete from the list the non-prime numbers (Eratosthenes Sieve)
        for i in range(2, 1+int(math.ceil(math.sqrt(max_number)))):
            if primes[i] == True:
                j = int(math.pow(i,2))
                while j <= max_number:
                    primes[j] = False
                    j += i

        cont = 0
        times = 1
        cont_2_veces = 0
        dirr = 0

        # We create the ulam image based on the primes list
        for i in range(1,max_number+1):
            
            pix[offset_x,offset_y] = int(primes[i])

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

        # We save the image
        img.save("ulam.png")
        img.show()
    

if __name__ == "__main__":
    main()
