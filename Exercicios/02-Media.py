
def Media(num1, num2):
    media = (num1 + num2)/2 
    return media


def main():
    nota1 = float(input())
    nota2 = float(input()) 

    print(Media(nota1, nota2))


if __name__ == "__main__":
    print(__name__)
    main()