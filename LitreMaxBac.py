def PoissonMax(nom):
  x = float(input("Entrer taille max d'un " + nom + " en cm : "))
  y = int(input("Entrer le nombre d'individu : "))
  x = (x**3 / 25) * y
  return x


nbrspec = int(input("Nombre d'espéce(s) dans votre aquarium (crevettes + poissons) : "))
valfinal = 0

for i in range(nbrspec):
  print("\n")
  nom = (input("Entrer le nom de l'espéce : "))
  valpoiss = PoissonMax(nom)
  print("Litrage(s) minimum de l'aquarium : ", round(valpoiss,2), " litres pour vos ", nom)
  valfinal += valpoiss
  
print("\n Il vous faut donc un bac de ", round(valfinal,2), " litres minimum pour bien maintenir vos poissons")