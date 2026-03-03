letra = input("Digite uma letra: ")
letra = letra.trim()

match letra.lower():
    case 'a':
        print("É uma vogal")