## vlcp (Void Linux Control Panel)
## (c) NazionLinux 2024
## Contact me: nazionlinux (at) gmail dot com
## https://www.nazionlinux.com
## License: GPL3
## python vlcp.py
green = '\033[32m'
red = '\033[31m'
resetc = '\33[m'
print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
print(green + '*                                                                   ' + red + '*' , resetc)
print(green + '*' + resetc + '                     VOID LINUX CONTROL PANEL                      ' + red + '*' , resetc)
print(green + '*                                                                   ' + red + '*' , resetc)
import os
while True:
    try:
        print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
        print(green + '*  [' + resetc + '0' + green + '] » ' + resetc + 'Esci                                                       ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '1' + green + '] » ' + resetc + 'Aggiorna database/sistema (dist-upgrade) Debian            ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '2' + green + '] » ' + resetc + 'Aggiorna database/sistema (verbose mode)                   ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '3' + green + '] » ' + resetc + 'Aggiorna database/sistema (senza conferma)                 ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '4' + green + '] » ' + resetc + 'Cancella cache pacchetti scaricati                         ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '5' + green + '] » ' + resetc + 'Rimuove pacchetti orfani                                   ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '7' + green + '] » ' + resetc + 'Installa pacchetti                                         ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '6' + green + '] » ' + resetc + 'Cerca pacchetto                                            ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '8' + green + '] » ' + resetc + 'Rimuove pacchetto e dipendenze                             ' + red + '*' , resetc)
        print(green + '*  [' + resetc + '9' + green + '] » ' + resetc + 'Lista pacchetti installati                                 ' + red + '*' , resetc)
        print(green + '* [' + resetc + '10' + green + '] » ' + resetc + 'Lista pacchetti installati (colonne)                       ' + red + '*' , resetc)
        print(green + '* [' + resetc + '11' + green + '] » ' + resetc + 'Lista kernels                                              ' + red + '*' , resetc)
        print(green + '* [' + resetc + '12' + green + '] » ' + resetc + 'Rimuove kernels manualmente                                ' + red + '*' , resetc)
        print(green + '* [' + resetc + '13' + green + '] » ' + resetc + 'Rimuove tutti i vecchi kernels                             ' + red + '*' , resetc)
        print(green + '* [' + resetc + '14' + green + '] » ' + resetc + 'Rimuove pacchetti orfani e cancella la cache               ' + red + '*' , resetc)
        print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
        print("Digitare un numero da 1-14:")
        options = int(input())
        if options == 0:
            print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
            break
        elif options == 1:
            os.system("sudo xbps-install -Su")
            print("\n")
        elif options == 2:
            os.system("sudo xbps-install -Suv")
            print("\n")
        elif options == 3:
            os.system("sudo xbps-install -Syu")
            print("\n")
        elif options == 4:
            os.system("sudo xbps-remove -Ov")
            print("\n")
        elif options == 5:
            os.system("sudo xbps-remove -ov")
            print("\n")
        elif options == 6:
            package = input('Pacchetto da cercare: ')
            os.system('xbps-query -Rs ' + package)
            print("\n")
        elif options == 7:
            install = input('Pacchetto da installare: ')
            os.system('sudo xbps-install -S ' + install)
            print('\n')
        elif options == 8:
            remove = input('Pacchetto da rimuovere: ')
            os.system('sudo xbps-remove -R ' + remove)
            print("\n")
        elif options == 9:
            os.system("xbps-query -l")
            print("\n")
        elif options == 10:
            os.system("xbps-query -m | column")
            print("\n")
        elif options == 11:
            print("LISTA KERNELS:")
            os.system("vkpurge list")
            print("\n")
        elif options == 12:
            os.system("vkpurge list")
            vkpurge = input("Versione kernel da rimuovere:")
            os.system("sudo vkpurge rm " + vkpurge)
            print("\n")
        elif options == 13:
            os.system("sudo vkpurge rm all")
            print("\n")
        elif options == 14:
            os.system("sudo xbps-remove -Oo")
            print("\n")
        else:
            print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
            print(green + '*                                                                   ' + red + '*' , resetc)
            print(green + '*' + red + '                    ERRORE: NUMERO INESISTENTE                     ' + red + '*' , resetc)
            print(green + '*                                                                   ' + red + '*' , resetc)
    except:
            print(green + '********************' + resetc + '*****************************' + red + '********************' , resetc)
            print(green + '*                                                                   ' + red + '*' , resetc)
            print(green + '*' + red + '                    ERRORE: DIGITARE UN NUMERO                     ' + red + '*' , resetc)
            print(green + '*                                                                   ' + red + '*' , resetc)

