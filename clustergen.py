import random
points = int( input ("Numero de punts: ") )
clusters = int( input ("Numero de clusters: ") )
point_list = []
point_dist = []
cluster_list = []

# genera punts aleatoris
for i in range (0, points):
	a = random.randint(0,1000)
	point_list.append(a)

print ("\nLlista de punts")
for i in point_list:
	print(i)

# ordena la llista
point_list_sort = point_list.copy()
point_list_sort.sort()

print ("\nLlista de punts ordenada")
for i in point_list_sort:
	print(i)

# calcula les distancies
last=0
for i in point_list_sort:
	if last != 0:
		point_dist.append(i-last)
	last = i

print ("\nDistancies")
for i in point_dist:
	print(i)

# ordena distancies en ordre invers i troba la maxima distancia
point_dist_sort = point_dist.copy()
point_dist_sort.sort(reverse=True)

dist = point_dist_sort[clusters-1]
print ("\nMaxima distancia")
print (dist)
icluster = 1
print("\nPunts ordenats en clusters")
for i in range (0, points):
	if i == 0:
		print ("Cl",icluster)
		print (point_list_sort[i])
	else:
		if point_dist[i-1] > dist:
			icluster = icluster + 1
			print ("Cl",icluster)
		print (point_list_sort[i])

# genera matriu de distancies
print ("\nMatriu de distancies")
print (points,clusters)
for p1 in point_list:
	for p2 in point_list:
		dist = abs(p2-p1)
		print (dist,end=" ")
	print()
