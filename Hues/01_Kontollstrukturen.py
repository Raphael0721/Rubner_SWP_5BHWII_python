import random


def check_random_number():
    num1 = random.randint(1, 100)
    res = odd_or_even(num1)

    if(res == "even"):    
        print("The number is even")
    elif(res == "odd"):
        print("The number is odd")
    else:
        print("Error")

    

def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def random_Car():
    cars = ["BMW", "Mercedes", "Audi", "Volkswagen", "Porsche"]
    return cars[random.randint(0, len(cars) - 1)]

def car_rating():
    car = random_Car()
    match car:
        case "BMW":
            print("BMW ist ein teures Auto.")
        case "Mercedes":
            print("Mercedes ist ein luxuriöses Auto.")
        case "Audi":
            print("Audi ist ein luxuriöses Auto.")
        case "Volkswagen":
            print("Volkswagen ist ein zuverlässiges Auto.")
        case "Porsche":
            print("Porsche ist ein Sportwagen.")
        case _:
            print("Unbekanntes Auto.")

def while_loop_example():
    number = 7
    ran_num = None
    counter = 0
    while ran_num != number:
        counter += 1
        ran_num = random.randint(1, 10)
    print(f"Nummer {number} wurde nach {counter} Versuchen gefunden.")
        
def for_loop_example():
    array = [2,5,4,1,3]
    for i in array:
       print (i)

    for i in range(5):
        if i == 3:
            break
        print(i)

    for i in range(5):
            if i == 3:
                continue
            print(i)

def empty_loop_example():
    for i in range(5):
        pass  


    

if __name__ == "__main__":
    # if Struktur
    check_random_number()
    # match-case Struktur
    car_rating()
    # for Schleife & continue & break
    for_loop_example()
    # pass example
    empty_loop_example()
    # while Schleife
    while_loop_example()
    # exception handling
    try:
        lz = int(input("Geben Sie Ihre Lieblingszahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
    else:
        print(f"Ihre lieblingszahl ist: {lz}")
    finally:
        print("Programm beendet.")