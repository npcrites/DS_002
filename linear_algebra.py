from typing import List
import math

Vector = List[float]


def add(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w), "vectors must be same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]
assert add([1,2,3],[4,5,6]) == [5,7,9]



def subtract(v:Vector, w:Vector) -> Vector:
    assert len(v)== len(w),"vectors must be same length"
    return[v_i - w_i for v_i, w_i in zip (v,w)]
assert subtract([5,7,9],[4,5,6]) == [1,2,3]



def vector_sum(vectors: List[Vector]) -> Vector:
    #sums all corresponding elements
    #check that vectors is not empty
    assert vectors, "no vectors provided!"
    
    #check that vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    
    #the ith element of the result is the sum of every vector[i]
    return[sum(vector[i] for vector in vectors) 
               for i in range(num_elements)]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]



def scalar_multiply(c: float, v:Vector) -> Vector:
    return [c* v_i for v_i in v]

assert scalar_multiply(2,[1,2,3]) == [2,4,6]



def vector_mean(vectors:List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]



def dot(v: Vector, w: Vector) -> float:
    assert len(v)  == len(w)
    return sum(v_i * v_w for v_i, v_w in zip(v,w))
assert dot ([1,2,3], [4,5,6]) == 32



def sum_of_squares (v: Vector)-> float:
    return dot(v,v)



def magnitude(v: Vector) -> float:
    return matht.sqrt(sum_of_squares(v))



def squared_distance (v:Vector, w:Vector) -> float:
    return sum_of_squares(subtract(v,w))



def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v,w))



def distance(v: Vector, w: Vector) -> float: 
    return magnitude(subtract(v,w))

