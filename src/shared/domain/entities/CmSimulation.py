

class CmSimulation:
    #geometria
    Xcg: float #Posição do Centro de Gravidade (CG) / Positivo ou negativo (0,25 = 25% da corda)
    Xac_w: float #Posição do Centro Aerodinâmico (AC) / Valor positivo e fixo
    Sw: float #Área da Asa (m²) / Deve ser um valor positivo.
    St: float #Área da Empenagem Horizontal (Tail Area) / Deve ser um valor positivo
    cw: float #Corda Média Aerodinâmica da Asa (Wing Mean Aerodynamic Chord) / Deve ser um valor positivo. Medido em metros.
    ct: float #Corda Média Aerodinâmica da Empenagem Horizontal (Tail Mean Aerodynamic Chord) / Deve ser um valor positivo. Medido em metros.
    iw: float #Ângulo de Incidência da Asa (Wing Incidence Angle) / Pode ser positivo ou negativo ou zero. Medido em graus. No código, ele é fornecido em graus e convertido para radianos.
    it: float #Ângulo de Incidência da Empenagem Horizontal (Tail Incidence Angle) / Pode ser positivo ou negativo ou zero. Medido em graus.
    lt: float #Braço de Cauda (Tail Arm) / Deve ser um valor positivo. Quanto maior o braço de cauda, mais "autoridade" (capacidade de gerar momento) a empenagem tem.
    #aero
    Cm_ac: float #Coeficiente de Momento no Centro Aerodinâmico / Geralmente um valor pequeno, negativo ou zero.
    Cl_0: float #Coeficiente de Sustentação com Ângulo de Ataque Zero / Positivo ou zero.
    Cl_alpha: float #Inclinação da Curva de Sustentação (Lift Curve Slope) / É sempre positivo antes do estol(stall). Teoricamente, para um aerofólio 2D, é 2\pi por radiano. Para uma asa 3D finita, é sempre menor que 2\pi.
    
    def __init__(self, 
                 xcg: float, 
                 xac_w: float, 
                 sw: float, 
                 st: float, 
                 cw: float, 
                 ct: float, 
                 iw: float, 
                 it: float, 
                 lt: float, 
                 cm_ac: float, 
                 cl_0: float, 
                 cl_alpha: float):
      pass

    @staticmethod
    def validate_xcg(xcg: float) -> bool:
        if xcg is None:
            return False
        elif type(xcg) != float:
            return False
        elif xcg < -1 or xcg > 1:
            return False
        return True