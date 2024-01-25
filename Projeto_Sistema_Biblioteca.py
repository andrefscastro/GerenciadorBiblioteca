class Livros:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel




class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    def listarLivros(self):
        print("Livros disnponiveis:")
        for livro in self.livros:
            if livro.disponivel:
                print(f"{livro.titulo} - {livro.autor}")
            else:
                print(f"{livro.titulo} não disponivel.")

    def emprestar(self, livro_desejado):

        livro_encontrado = None
        for livro in self.livros:
            if livro.titulo == livro_desejado and livro.disponivel:
                livro_encontrado = livro
                break

        if livro_encontrado:
            livro_encontrado.disponivel = False
            print(f"Você realizou o empréstimo do livro {livro_desejado}.")

        else:
            print(f"{livro_desejado} não disponível no momento.")


def exibirMenu():
    print("""\nEscolha uma opção:
    1 - Listar livros disponiveis
    2 - Emprestar um livro
    3 - Sair
    """)

def menu_principal():
    flag = True
    while flag:
        exibirMenu()
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                biblioteca.listarLivros()
            elif opcao == 2:
                livro_desejado = input("Digite o livro desejado: ")
                biblioteca.emprestar(livro_desejado)
            elif opcao == 3:
                flag = False
            else:
                print("Digite apenas uma das opções indicadas.")
        except ValueError:
            print("Digite apenas números")




### Abaixo Processo do aluguel dos livros

##Criando livros que estarão disponiveis na biblioteca:

livro_1 = Livros("A Bela e a Fera", "Elizabeth Rudnick", disponivel=True)
livro_2 = Livros("Harry Potter", "J. K. Rowling", disponivel=True)
livro_3 = Livros("O Senhor dos Anéis", "J. R. R. Tolkien", disponivel=True)

##Criando estoque de livros:

biblioteca = Biblioteca([livro_1, livro_2, livro_3])


##chamando a função para Exibir o menu principal
menu_principal()


