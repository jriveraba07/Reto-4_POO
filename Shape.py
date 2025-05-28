
#* reto 4

from math import acos 
from math import degrees

class Point:
    definition: str = "Entidad geometrica abstracta que representa un punto en el espacio"
    #* atributos que tiene la clase ^
    #* la funcion inicializadora
    def __init__(self, x : float = 0, y : float = 0):
        self.x = x 
        self.y = y
    
    # metodos
    def move(self, new_x : float, new_y : float):
        self.x = new_x
        self.y = new_y
        
    def reset(self):
        self.x = 0 
        self.y = 0   

    def prod_punto(self, point: "Point"):
        return self.x * point.x + self.y * point.y
    
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5 
        return distance
    
    def __sub__(self, point2: "Point")-> "Point":
        vec_x = self.x - point2.x
        vec_y = self.y - point2.y
        return Point(vec_x, vec_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"


    
class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self)-> float:
        return self.start.compute_distance(self.end)

    def compute_slope(self)-> float:
        if self.end.x != self.start.x:     
            delta_y = self.end.y - self.start.y
            delta_x = self.end.x - self.start.x
            return delta_y / delta_x
        else:
            return None
    
    def __str__(self):
        return f"star: {self.start} , end: {self.end}"
    
    def __repr__(self):
        return f"[{self.start} , {self.end}]"
    

class Shape:
    def __init__(self, is_regular: bool):
        self.regular = is_regular
    
    def vertices(self):
        pass
    
    def edges(self):
        pass
    
    def inner_angles(self):
        pass
    
    def compute_area(self):
        pass
   
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass

class Triangle(Shape):
    def __init__(self, is_regular: bool, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(is_regular)
        self.__Point_1 = point_1
        self.__Point_2 = point_2
        self.__Point_3 = point_3
    
    def get_Point_1(self):
        return self.__Point_1
    
    def get_Point_2(self):
        return self.__Point_2
    
    def get_Point_3(self):
        return self.__Point_3
    
    def vertices(self):
        v = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        for i in range(len(v)):
            print(f"vertice {chr(97 + i)} =  {v[i]}")
        return ""

    def edges(self):
        line_1 = Line(self.get_Point_1(), self.get_Point_2())
        line_2 = Line(self.get_Point_2(), self.get_Point_3())
        line_3 = Line(self.get_Point_3(), self.get_Point_1())
        d = [line_1, line_2, line_3]
        return d
    
    def compute_inner_angles(self):
        d = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        angle = []
        for i in range(3):
            vec1 = d[i] - d[(i + 1) % 3]
            vec2 = d[i] - d[(i + 2) % 3]
            a = vec1.prod_punto(vec2)
            b = vec1.compute_distance(Point(0, 0)) * vec2.compute_distance(Point(0, 0))
            angle.append(round(degrees(acos(a / b)), 2))
        return angle

    def inner_angles(self):
        vertices = [self.get_Point_1(), self.get_Point_2(), self.get_Point_3()]
        angles = self.compute_inner_angles()
        for i in range(len(vertices)):
            print(f"{chr(97 + i)}: {vertices[i]} = {angles[i]}")  
        return ""
    
    def compute_perimeter(self):
        s = 0
        for i in self.edges():
            s += i.compute_length()
        return round(s, 3)
    
    def compute_area(self):
        # lo que voy a poner es una formula general de cualquier triangulo
        edges = self.edges()
        a: float = edges[0].compute_length()
        b: float = edges[1].compute_length()
        c: float = edges[2].compute_length()
        #* s es el semiperimetro, osea que es la mitad del perimetro
        s: float = self.compute_perimeter() / 2
        return round((s * (s - a) * (s- b) * (s - c)) ** 0.5, 2)

class Equilateral(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(True, point_1, point_2, point_3 )
    

class Scalene(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(False, point_1, point_2, point_3 )


class Isosceles(Triangle):
    def __init__(self, point_1: "Point" , point_2: "Point" , point_3: "Point"):
        super().__init__(True, point_1, point_2, point_3 )



class Rectangle(Shape):
    def __init__(self, is_regular: bool, point_bt_sid: "Point", point_up_sid: "Point"):
        super().__init__(is_regular)
        self.__ver1 = point_bt_sid
        self.__ver2 = Point(point_up_sid.x, point_bt_sid.y)
        self.__ver3 = point_up_sid
        self.__ver4 = Point(point_bt_sid.x, point_up_sid.y)

    def get_ver1(self):
        return self.__ver1
    
    def get_ver2(self):
        return self.__ver2
    
    def get_ver3(self):
        return self.__ver3
    
    def get_ver4(self):
        return self.__ver4
    
    def vertices(self):
        v = [self.get_ver1(), self.get_ver2(), self.get_ver3(), self.get_ver4()]
        return v
    
    def edges(self):
        line_1 = Line(self.get_ver1(), self.get_ver2())
        line_2 = Line(self.get_ver2(), self.get_ver3())
        line_3 = Line(self.get_ver3(), self.get_ver4())
        line_4 = Line(self.get_ver4(), self.get_ver1())
        d = [line_1, line_2, line_3, line_4]
        return d
    
    def compute_inner_angles(self):
        angle = [90, 90, 90, 90]
        return angle

    def inner_angles(self):
        d = self.vertices()
        angles = self.compute_inner_angles()
        for i in range(len(d)):
            print(f"{chr(97 + i)}: {d[i]} = {angles[i]}")  
        return ""
    
    def compute_perimeter(self):
        s = 0
        for i in self.edges():
            s += i.compute_length()
        return round(s, 3)
    
    def compute_area(self):
        base: float = abs(self.get_ver1().x - self.get_ver3().x)
        altura: float = abs(self.get_ver1().y - self.get_ver3().y)
        return base * altura
    

class Square(Rectangle):
    def __init__(self, point_bt_sid: "Point", point_up_sid: "Point"):
        super().__init__(True, point_bt_sid, point_up_sid)
        
# Triángulo escaleno (todos los lados diferentes)
ver = Point(0, 1)
ver2= Point(2, 2)
ver3 = Point(2, 4)

rectangulo = Rectangle(False, ver, ver2)
cuadrado = Square(ver3, Point(4 , 6))

print("                           |rectangulo|")
print("")
print("estos son los vertices del rectangulo:")
print(rectangulo.vertices()) 
print("estos son los lados del rectangulo:" ,rectangulo.edges()) 
print("estos son los angulos del rectangulo:")
print(rectangulo.inner_angles())

print("este es el perimetro del rectangulo:" ,rectangulo.compute_perimeter())
print("este es el area del rectangulo:" ,rectangulo.compute_area())   

print("")

print("                           |cuadrado|")
print("")
print("estos son los vertices del cuadrado:")
print(cuadrado.vertices()) 
print("estos son los lados del cuadrado:" ,cuadrado.edges()) 
print("estos son los angulos del cuadrado:")
print(cuadrado.inner_angles())

print("este es el perimetro del cuadrado:" ,cuadrado.compute_perimeter())
print("este es el area del cuadrado:" ,cuadrado.compute_area())   

print("")



print(                              "|Triangulos - prueba|")

# Triángulo equilátero 
A = Point(0, 0)
B = Point(1, 0)
C = Point(0.5, 0.866)  

triangulo_equilatero = Equilateral(point_1=A, point_2=B, point_3=C)

# Triángulo isósceles (dos lados iguales)
D = Point(0, 0)
E = Point(2, 0)
F = Point(1, 2)

triangulo_isosceles = Isosceles(point_1=D, point_2=E, point_3=F)

# Triángulo escaleno (todos los lados diferentes)
G = Point(0, 1)
H = Point(2, 1)
I = Point(2, 4)

triangulo_escaleno = Scalene(point_1=G, point_2=H, point_3=I)

print("                           |triángulo escaleno|")
print("")
print("estos son los vertices del triángulo:")
print(triangulo_escaleno.vertices()) 
print("estos son los lados del triángulo:" ,triangulo_escaleno.edges()) 
print("estos son los angulos del triángulo:")
print(triangulo_escaleno.inner_angles())

print("este es el perimetro del triángulo:" ,triangulo_escaleno.compute_perimeter())
print("este es el area del triángulo:" ,triangulo_escaleno.compute_area())   

print("")

print("                           |triángulo isoceles|")

print("")
print("estos son los vertices del triángulo:")
print(triangulo_isosceles.vertices()) 
print("estos son los lados del triángulo:" ,triangulo_isosceles.edges()) 
print("estos son los angulos del triángulo:")
print(triangulo_isosceles.inner_angles())
print("este es el perimetro del triángulo:" ,triangulo_isosceles.compute_perimeter())
print("este es el area del triángulo:", triangulo_isosceles.compute_area())
      
print("")

print("                           |triángulo equilatero|")

print("")

print("estos son los vertices del triángulo:")
print(triangulo_equilatero.vertices()) 
print("estos son los lados del triángulo:" ,triangulo_equilatero.edges()) 
print("estos son los angulos del triángulo:")
print(triangulo_equilatero.inner_angles())
print("este es el perimetro del triángulo:" ,triangulo_equilatero.compute_perimeter())
print("este es el area del triángulo:", triangulo_equilatero.compute_area() )

