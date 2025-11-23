import sys

def somme_arguments(args):
    somme = 0
    for arg  in args:
        somme += flost(arg)
    return somme

if __name__ == "__main__"
    if len(sys.argv)>1:
        result = somme_arguments(sys.argv[1:])
        print("somme est ", result)
    else:
         print('veuillez passer des nombres arguments')