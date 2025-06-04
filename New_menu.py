
# The restaurant revisted
# Add setters and getters to all subclasses for menu item
# Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
# Add the class Payment() following the class example.

class MenuItem:
    def __init__(self,name: str, price: float, description: str = "", x: float = 0) :
        self.__name = name
        self.__price = price 
        self.__discount = x
        self.__description = description
        
    def get_name(self):
        return self.__name
        
    def get_price(self):
        return self.__price
    
    def get_discount(self):
        return self.__discount
    
    def set_discount(self, x):
        self.__discount = x
        pass
    
    def get_description(self):
        return self.__description
    

    def calculate_total_price(self)-> float:
        a = self.get_price() * (1 - self.get_discount()/100)
        self.set_discount(0) 
        return a
    
    def new_discount(self, tacaño)->float:
        if tacaño == 0:
            self.set_discount(0) 
        else:
            self.set_discount(self.get_discount() + tacaño)


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, gluten: bool, description: str, x: float = 0):
        self.__gluten = gluten
        super().__init__(name, price, description, x)

    def get_gluten(self):
        return self.__gluten
    
    def __str__(self):
        return f"{self.get_name()} (gluten: {self.get_gluten()}): {self.get_price()}, {self.get_description()}"

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.__type = type
    
    def get_type(self):
        return self.__type
    
    def __str__(self):
        return f"{self.get_name()} ({self.get_type()}): {self.get_price()}, {self.get_description()}"  

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, brand: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def __str__(self):
        return f"{self.get_name()} - {self.get_brand()}: {self.get_price()}, {self.get_description()}"


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, cantidad: float, description: str, x: float = 0):
        self.__cantidad = cantidad
        super().__init__(name, price, description, x)   

    def get_cantidad(self):
        return self.__cantidad
    
    def __str__(self):
        return f"{self.get_name()} (cantidad: {self.get_cantidad()} gr): {self.get_price()}, {self.get_description()}"

class Order:
    def __init__(self, menu: list, tip: float = 0):
        self.menu = menu
        self.tip = tip
        self.order = []
        self.limit = 0
    
    def see_menu(self):
        n = len(self.menu)
        for i in range(n):
            print(str(i + 1) + ".", self.menu[i])
        return f"{n}. {self.menu[n - 1]}"

    def see_order(self):
        print("")
        n = len(self.order)
        print("lo que has pedido:")
        print("")
        for i in range(n):
            print(f"[{self.order[i].get_name()} - con un descuento de {self.order[i].get_discount()}%]")
        return ""

    
    def add_item(self, food :"MenuItem")-> list:
        self.limit = 0
        for i in self.order:
            i.new_discount(0)
        self.order.append(food)
        return f"se añidio {food.get_name()} (se reiniciaron todos los descuentos)"

    def calculate_bill_amount(self):
        print("")
        amount = 0
        for i in self.order:
            amount += i.calculate_total_price()
        return amount

#! ya no se va a tomar  los descuentos en el programa principal
        
    def discounts(self):
        print("")
        desserts = [i for i in self.order if isinstance(i, Dessert)]
        main_coursess = [i for i in self.order if isinstance(i, MainCourse)]
        bevereages = [i for i in self.order if isinstance(i, Beverage)]
        appetizers = [i for i in self.order if isinstance(i, Appetizer)]
        if self.calculate_bill_amount() >= 80000:
            for i in self.order:
                i.new_discount(15)
            print("Tu cuenta es mas de 80000, 15% en la cuenta total")
       
        elif len(desserts) + len(main_coursess) + len(bevereages) + len(appetizers) >= 4:
            for i in self.order:
                i.new_discount(20)
            return "por comprar un postre, plato fuerte, aperitivos y postre ahora tiene un 20% de descuento!"
        elif (len(main_coursess) + len(bevereages)) % 2 == 0 :
            for i in self.order:
                if i in main_coursess or i in bevereages:
                    i.new_discount(10)
                else:
                    pass
            return "por comprar cantidades pares de bebidas y de platos fuertes son un 10% mas baratos!"
        elif self.limit >= 0: 
            return "no puedes aplicarle descuento al descuento, bobo hpta"
        else:
            return "no hay descuentos disponibles, pobre"
        

class Payment:
    def __init__(self):
        pass

    def pay(self, check):
        raise NotImplementedError("No se ha definido tontin)")

class CardPayment(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, check):
        print(f"Paying ${check} with card {self.number[-4:]}")

class CashPayment(Payment):
    def __init__(self, get_money: float):
        super().__init__()
        self.money = get_money

    def pay(self, check):
        if self.money > check:
            print(f"It was paid the bill of ${check}, your change is ${self.money - check}")
        elif self.money == check:
            print(f"It was paid exact check, no change")
        else:
            print(f"You don't have enough money to pay the check, We accept other payment methods")
        

         
milhoja = Dessert("milhoja", 7500, True, "Postre con mil hojas")
pollo_asado = MainCourse("pollito asado", 40000, "pollo","Un pollo asado de dudosa procedencia")
bistec = MainCourse("bistec", 25000, "carne", "Hecho de las vacas de genetica en la nacional")
natilla = Dessert("natilla", 5000, True, "Delicioso postre colombiano con leche de bufalo")
changua = Appetizer("changua", 9500, 500,"leche con huevo (¿Quien creyo que era buena idea esto?)")
cerveza_1 = Beverage("cerveza", 3500, "poker", "Cerveza que toma el rolo promedio")
aguardiente = Beverage("aguardiente 1/2", 16000, "nectar", "Agua que pica pero rico")
chunchullo = Appetizer("chunchullo", 12000, 200, "No preguntes de donde viene, solo disfrutalo")
mojarra = MainCourse("mojarra", 40000, "pescado","OJO CON LAS ESPINAS")
limonada = Beverage("limonada de coco", 3500, "frutiño", "Limonada hecha con agua de la llave")

menu = [milhoja, pollo_asado, bistec, natilla, changua, cerveza_1, aguardiente, chunchullo, mojarra, limonada]
cliente = Order(menu, tip = 0)

card = CardPayment("15478935456215789", 666)
cash = CashPayment(130000)

cliente.see_menu()
cliente.add_item(pollo_asado)
cliente.add_item(bistec)
print(cliente.see_order())
print(cliente.calculate_bill_amount())

print(cliente.calculate_bill_amount())
cliente.see_order()
print("")
print(cliente.add_item(mojarra))
print(cliente.add_item(milhoja))
print(cliente.add_item(changua))

cliente.see_order()
cliente.calculate_bill_amount()
cliente.see_order()

print("                                  |CUENTA|")
a = float(input(f"cuanto porcentaje de la cuenta quieres agregar: "))
total = cliente.calculate_bill_amount() 
cliente.tip = a
if a == 0:
    print("tacaño resulto el señor!")

total_plustip = total * (a / 100 + 1)
print(f"Total a pagar: {total_plustip}, cuenta de {total} con propina de: {cliente.tip}%" )
print("")
print("$Pay the bill with cash$")
print("")
cash.pay(total_plustip)
print("")
print("$Pay the bill with card$")
print("")
card.pay(total_plustip)
