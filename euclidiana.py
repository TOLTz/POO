import math



class Pontos:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    def math_euclidiana(self):
        p1 = self.p1
        p2 = self.p2
        if len(p1) != len(p2):
            raise ValueError("Os pontos devem ter a mesma dimensão")
        
        return round(math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2))), 2)
    
        
    def distancia_euclidiana(self):
        p1 = self.p1
        p2 = self.p2
        if len(p1) != len(p2):
            raise ValueError("Os pontos devem ter a mesma dimensão")

        soma_quadrados = sum((a - b) ** 2 for a, b in zip(p1, p2))
        
        x = soma_quadrados
        if x == 0:
            return 0
        estimativa = x / 2
        for _ in range(10):
            estimativa = (estimativa + x / estimativa) / 2
        
        return round(estimativa, 2)

point = Pontos((10, 5), (15,-2))
print(point.distancia_euclidiana())
print(point.math_euclidiana())
 
 
 
