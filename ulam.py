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
            offset_y = offset_y;

        ini_x = offset_x
        ini_y = offset_y

        print("wh: %d" % wh)

        # We create a blank image
        img = Image.new('1', (wh,wh))
        pix = img.load()

        # We create a list of booleans that'll represent if this index+2 is prime or not
        primes = [True] * (max_number-1)

        # We delete from the list the non-prime numbers (Eratosthenes Sieve)
        for i in range(2, 1+int(math.ceil(math.sqrt(max_number)))):
            if primes[i-2] == True:
                j = int(math.pow(i,2))
                while j <= max_number:
                    primes[j-2] = False
                    j += i

        # We create the ulam image based on the primes list

        
        
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if((i+j)%2 == 0):
                    pix[i,j] = 1

        img.save("ulam.png")
        img.show()
    

if __name__ == "__main__":
    main()
