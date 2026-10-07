import random

lottozahlen = []
stats = {}

def lotto_setup(array):
    for z in range(1, 46, 1):
        array.append(z)


def play_lotto():
    
    gezogene_zahlen = []
    for i in range(1,7,1):
        ran_num = random.randint(0,len(lottozahlen)-i)
        gezogene_zahlen.append(lottozahlen[ran_num])
        lottozahlen[ran_num] = lottozahlen[len(lottozahlen)-i]
        lottozahlen[len(lottozahlen)-i] = gezogene_zahlen[i-1]
    # print(gezogene_zahlen)
    return gezogene_zahlen


def lotto_stats():
    for i in range(1,46,1):
        stats[i] = 0

    num_trys = int(input("Wie viele Ziehungen sollen simuliert werden?"))

    for t in range(num_trys):
        data = play_lotto()
        for n in data:
            stats[n] += 1

    for key, value in stats.items():
        print(key, ": ", value)
        

     





if __name__ == "__main__":
    lotto_setup(lottozahlen)
    lotto_stats()