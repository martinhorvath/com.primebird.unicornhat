import unicornhat as uh
import time

uh.set_layout(uh.PHAT)
uh.brightness(0.2)
uh.clear()
uh.show()

ar_martin = [[1,1,1,1],[0,1,0,0],[0,0,1,0],[0,1,0,0],[1,1,1,1],[0,0,0,0],[1,1,1,1],[1,0,1,0],[1,1,1,1],[0,0,0,0]]
i = 0
endOfText = False

matrix = [[0,0,0,0,0,0,0,0],[0,0,0,0]]

while True:
    while endOfText == False:
        for c in range(len(matrix[0])):
            for r in range(len(matrix[1])):
                if i+c < len(ar_martin):
                    if ar_martin[i+c][r] == 1:
                        uh.set_pixel(c,r,0,0,255)
                    else:
                        uh.set_pixel(c,r,0,0,0)
                else:
                    #end of text reached
                    endOfText = True
                    uh.set_pixel(c,r,0,0,0)
        uh.show()
        time.sleep(0.5)
        uh.clear()
        uh.show()
        i+=1
    i = 0
    endOfText = False
