from time import sleep

twoPoints = ":"
zero = "0"
onlyPoint = twoPoints.replace('', '')
twoPointsAndZero = twoPoints.replace('', '') + zero.replace('', '')
onlyZero = zero.replace('', '')

for hora in range(25):
    for minuto in range(60):
        for segundo in range(60):

            if hora < 10 and segundo < 10 and minuto < 10:
                print(onlyZero, hora, twoPointsAndZero,
                      minuto, twoPointsAndZero, segundo)
            else:
                if hora < 10 and segundo < 10:
                    print(onlyZero, hora, onlyPoint,
                          minuto, twoPointsAndZero, segundo)
                else:
                    if hora < 10 and minuto < 10:
                        print(onlyZero, hora, twoPointsAndZero,
                              minuto, onlyPoint, segundo)
                    else:
                        if segundo < 10 and minuto < 10:
                            print(hora, twoPointsAndZero, minuto,
                                  twoPointsAndZero, segundo)
                        else:
                            if segundo < 10:
                                print(hora, onlyPoint, minuto,
                                      twoPointsAndZero, segundo)
                            else:
                                if minuto < 10:
                                    print(hora, twoPointsAndZero,
                                          minuto, onlyPoint, segundo)
                                else:
                                    if hora < 10:
                                        print(onlyZero, hora, onlyPoint,
                                              minuto, onlyPoint, segundo)

                sleep(1)

    if hora == 24:
        hora = 0
