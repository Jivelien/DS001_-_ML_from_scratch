
class Truc:
    attribut : str

t1 = Truc()
t1.attribut = 'konbawa' # FIXME : variable de class ou instance ?

Truc.attribut = 'hello'

t2 = Truc()

Truc.attribut = 'coucou'

print(Truc.attribut)
print(t1.attribut)

# https://dzone.com/articles/python-class-attributes-vs-instance-attributes