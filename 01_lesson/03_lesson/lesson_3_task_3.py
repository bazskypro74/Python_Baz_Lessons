from adres import Address
from mail import Mailing
from_date = Address("305010", "Kursk", "Dimitrova", "3", "5")
to_date = Address("303002", "Moscow", "Lenina", "87", "158")
mail1 = Mailing(from_address=from_date, to_address=to_date,
                track="355555444", cost=350)
print(f"Отправление {mail1.track
                     } из {mail1.from_address} в {mail1.to_address
                                                  }. Стоимость {mail1.cost
                                                                } рублей")
