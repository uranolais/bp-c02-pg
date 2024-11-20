from cliente import Cliente
from item import Item

cliente = Cliente("lais", "alura")
print(f"Cliente: {cliente.nome}, Endereço: {cliente.endereco}")

item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
print(f"Item: {item_um.nome}, Preço: {item_um.preco}")
print(f"Item: {item_dois.nome}, Preço: {item_dois.preco}")
