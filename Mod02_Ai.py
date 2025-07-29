class BookStoreInventory:
    def __init__(self):
        self.inventory = {}

    def addBook(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def checkQuantity(self, title):
        if title in self.inventory:
            return self.inventory.get(title, 0)
        else:      
            return 0   

    def removeBook(self, title, quantity):
        if title in self.inventory and self.inventory[title]:
            self.inventory[title] -= quantity
            if self.inventory[title] == 0:
                del self.inventory[title]
            return True
        return False
    
    def recommendBooks(self, description):
        keywords = description.lower().split()
        recommendations = {
            'análise': 'Os elementos da aprendizagem estatística',
            'aventura': 'O Hobbit de J.R.R. Tolkien',
            'mistério': 'As Aventuras de Sherlock Holmes de MI LUCU', 
            'romance': 'Orgulho e Preconceito de Jane Austen',
            'ficção': 'Duna de Frank Herbert',
            'fantasia': 'Harry Potter e a Pedra Filosofal de J.K. Rowling',
            'história': 'Sapiens: Uma Breve História da Humanidade por Yuval Noah Harari'
        }
        for keyword in keywords:
            if keyword in recommendations:
                return recommendations[keyword]
        return "Sem recomendações para você no momento."


if __name__ == "__main__":
    bookStore = BookStoreInventory()
    bookStore.addBook("Sapiens:Uma Breve História da Humanidade", 2)
    bookStore.addBook("Duna", 3)  
    bookStore.addBook("O Hobbit", 1)   
    bookStore.addBook("O Senhor dos Anéis", 2)   
    bookStore.addBook("Harry Potter e a Pedra Filosofal", 4)   
    bookStore.addBook("As Aventuras de Sherlock Holmes", 3) 

    recommendation = bookStore.recommendBooks("este livro é uma aventura sobre hobbit que encontra anel mágico ")
    print("Recomendação: " + recommendation)  

    hobbitQuantity = bookStore.checkQuantity("O Hobbit")
    print("Quantidade de O Hobbit: " + str(hobbitQuantity))   

    bookStore.removeBook("O Hobbit", 1)

    print("Quantidade após remover:", bookStore.checkQuantity("O Hobbit"))
