import match
import visual
import math
import copy

def aparear(n):
    P = match.create_random_points(n)
    aparear=[0]*len(P)
    P.sort(key=lambda Point: Point.x)
    """for i in range(len(P)):
        if(P[i].color==-1):
            grpR[i]=P.deepcopy(i)
        else:
            grpA[i]=P.deepcopy(i)
    """
    lCopy=copy.deepcopy(P)
    algorithm(lCopy, lCopy, aparear)

def heuristic(P):
    showlistPoint(P)
def restriccion(A, B, ListO, p):
    for i in range(p, len(ListO)):
        if(A.x<ListO[i].x and A.y<ListO[i].x and B.x>ListO[i].x and B.y<ListO[i].y):
            return False
    return True

def algorithm(lPuntos, lRestriccion, aparear):
    dim=0
    auxj=0
    r=0
    rectangulos=[]
    for i in range(len(lPuntos)):
        for j in range(i+1, len(lPuntos)):
            while(lRestriccion[r].x!=lPuntos[i].x):
                r+=1
            if(dim<math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2)) and restriccion(lPuntos[i], lPuntos[j], lRestriccion, r) and lPuntos[i].color==lPuntos[j].color):
                dim=math.sqrt(((lPuntos[j].x-lPuntos[i].x)**2)+((lPuntos[j].y-lPuntos[i].y)**2))
                auxj=j
        if(auxj!=0):
            rectangulos.append(match.Rectangle(min(lPuntos[i].x,lPuntos[auxj].x), max(lPuntos[i].x,lPuntos[auxj].x), min(lPuntos[i].y,lPuntos[auxj].y), max(lPuntos[i].y,lPuntos[auxj].y)))
            aparear[i]=1
            aparear[auxj]=1
            auxj=0
    visual.Window(points=lPuntos,rectangles=rectangulos) 




# def dijkstra(D):      Estoy repensando esto del Dijkstra, quizas con solo ordenar sea suficiente
#   Para ello pienso que se puede crear una nueva lista de pares ordenados de pares ordenados Rec(P1,P2)
#   esto es porque me di cuenta de que cada punto no puede tener otro en el mismo eje x o y POR DEFINICION DEL PROBLEMA

"""def mergeList(A): #Avance 02/05, falta mota jaja
    if len(A) >1:
        md=len(A)//2
        l=A[:md]
        r=A[md:]
        mergeList(l)
        mergeList(r)
        i=j=k=0
        c=[]
        while i<len(l) and j<len(r):
            if(l[i].x<=r[j].x):
                c.append(A[i])
                i+=1
            else:
                c.append(A[j])
                j+=1
        while i<len(A):
            c.append(A[i])
            i+=1
        while j<len(A):
            c.append(A[i])
            j+=1
        return c"""
def showlistPoint(P):
    for i in range(P):
        print("("+str(i.x)+", "+str(i.y)+", "+str(i.color)+")")

aparear(10)
