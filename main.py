from cluster import Cluster

from foa import FOA

foa=FOA(fun=Cluster(30,3),numSedds=15, maxTime=1000, lifeTime=2, areaLimit=15, localMotion=.5, localSeeding=5,transferRate=10, globalSeeding=3)
foa.run()