# EXERCICIO 1

class Publicacao: #classe base 
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
    
    def descrever(self): #método descrever 
        print(f"Título:{self.titulo}, Ano:{self.ano_publicacao}")

class Livro(Publicacao): #classe filha 
    def __init__(self, autor, titulo, ano_publicacao):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor #atributo adicional 

    def descrever(self): 
        super().descrever() #sobrescrevendo método 
        print(f"Autor:{self.autor}") #informação específica 

class Revista(Publicacao): #classe filha
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao #atributo adicional 

    def descrever(self):
        super().descrever() #sobrescrevendo método
        print(f"Edicao: {self.edicao}") #informação específica 
