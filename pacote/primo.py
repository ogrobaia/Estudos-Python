def primo(numero):
    if numero < 1:
        for x in range(2, numero):
            if(numero % x) == 0:
                return "Esse não é primo"
            else:
                return "Esse eh primo"
        else:
            return "Esse numero não eh primo: numero menor ou igual a 1"
        
if __name__ == '__name__'
print("Ola Mundo!!")