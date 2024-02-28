class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')

    # Здесь переопределён метод __str__ .
    def __str__(self):
        return f'У мобильного телефона {self.dial_type} тип набора номера'


phone = Phone('дисковый')
# Создать объект mobile_phone класса MobilePhone
mobile_phone = MobilePhone('сенсорный', 'LTE')

print(phone)
# Распечатать объект mobile_phone.
print(mobile_phone)  # Переопределённый метод __str__ в классе.
