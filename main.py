from cluster import Cluster

from foa import FOA

foa=FOA(fun=Cluster(20,3),numSedds=15, maxTime=1000, lifeTime=2, areaLimit=15, localMotion=.3, localSeeding=5,transferRate=10, globalSeeding=5)
foa.run()