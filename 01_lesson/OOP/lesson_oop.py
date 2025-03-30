from user import User
from card import Card

tom = User("Tom")
tom.sayName()
tom.setAge(33)
tom.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Tom F")
tom.addCard(card)
tom.getCard().pay(1000)
