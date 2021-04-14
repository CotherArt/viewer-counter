import serial_com as ard
import scraping as sc

def main():
    bufer = 0
    sc.start()
    while True:
        viewers = sc.viewers()
        if viewers != bufer:
            ard.write_read(viewers)
            bufer = viewers
        print(viewers)

    sc.top()
        

if __name__ == '__main__':
    main()

