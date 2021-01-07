import numpy as np
import random

import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation

import sys
import math

global anim

class Cluster:
    def __init__(self,numOfData=120,numOfCluster=3):
        self._num_of_data=numOfData
        self._num_of_cluster=numOfCluster
        self._datas = []
        for i in range(0, self._num_of_cluster):
            cr=[np.random.uniform(-15, 15),np.random.uniform(-15, 15)]
            for j in range(0 ,math.floor(self._num_of_data/self._num_of_cluster)):
                self._datas.append([np.random.uniform(cr[0]-1, cr[0]+1),np.random.uniform(cr[1]-1, cr[1]+1)])

    def getDim(self):
        return len(self._datas)
    def getInf(self):
        return 1
    def getSup(self):
        return self._num_of_cluster
    def getDatas(self):
        return self._datas

    def fitness(self, X):
        return self.fitnessG(X)

    def fitnessG(self, X):
        cluster_array=[round(x) for x in X]
        for i in range(0,len(cluster_array)):
            if cluster_array[i]<1:
                cluster_array[i]=1
            if cluster_array[i]>self._num_of_cluster:
                cluster_array[i]=self._num_of_cluster

        cluster_count=[ 0 for i in range(0,self._num_of_cluster+1)]
        for i in range(0,len(cluster_array)):
            cluster_count[int(cluster_array[i])] +=1
        s_i=self.__s_i(cluster_array,cluster_count)
        return sum(s_i) / len(s_i)

    def __s_i(self,cluster_array,cluster_count):
        a_i=self.__a_i(cluster_array,cluster_count)
        b_i=self.__b_i(cluster_array,cluster_count)
        s_i=[]

        for i in range(0,len(self._datas)):
            if cluster_count[int(cluster_array[i])]==1:
                s_i.append(0)
            elif cluster_count[int(cluster_array[i])] > 1:
                s_i.append((b_i[i]-a_i[i])/max(a_i[i],b_i[i]))

        return s_i

    def __a_i(self,cluster_array,cluster_count):
        a_i=[]
        for i in range(0,len(self._datas)):
            cn=cluster_array[i]
            sigma=0
            for j in range(0,len(self._datas)):
                if j==i:
                    continue
                if cn==cluster_array[j]:
                    sigma += self._distance(self._datas[i],self._datas[j])
            if cluster_count[int(cn)]==1:
                a_i.append(0)
            else:
                a_i.append((1/(cluster_count[int(cn)]-1))*sigma)
        return a_i

    def __b_i(self,cluster_array,cluster_count):
        b_i=[]

        for i in range(0,len(self._datas)):
            cn=cluster_array[i]
            b=[]
            for k in range(1,self._num_of_cluster+1):
                if k != cn and cluster_count[k] > 0:
                    sigma=0
                    for j in range(0 ,len(self._datas)):
                        if cn != cluster_array[j]:
                            sigma += self._distance(self._datas[i],self._datas[j])
                    b.append((1/cluster_count[k])*sigma)
            b_i.append(min(b))
        return b_i


    def _distance(self, p,q):
        return math.sqrt(np.sum([math.pow(p[i]- q[i],2) for i in range(0,len(p))]))


    def plot2(self):

        minX=min([data[0] for data in self._datas])
        maxX=max([data[0] for data in self._datas])

        minY=min([data[1] for data in self._datas])
        maxY=max([data[1] for data in self._datas])

        self.__fig = plt.figure()
        self.__ax =  self.__fig.add_subplot(111, xlim=(minX,maxX), ylim=(minY,maxY))

        scat = self.__ax.scatter([], [], c=[],s=25, cmap="hsv", vmin=0, vmax=1)
        scat.set_offsets(self._datas)
        scat.set_array(np.array([1 for i in range(0,len(self._datas))]))

        plt.show()

    def animatePlot2(self,maxtime,update):
        global anim

        minX=min([data[0] for data in self._datas])
        maxX=max([data[0] for data in self._datas])

        minY=min([data[1] for data in self._datas])
        maxY=max([data[1] for data in self._datas])

        self.__fig = plt.figure()
        self.__ax =  self.__fig.add_subplot(111, xlim=(minX,maxX), ylim=(minY,maxY))

        scat = self.__ax.scatter([], [], c=[],s=25, cmap="hsv", vmin=0, vmax=1)

        anim=matplotlib.animation.FuncAnimation(self.__fig, update, frames=maxtime,repeat=False,fargs=(scat,))

        plt.show()

    def animate(self,maxtime,update):
        self.animatePlot2(maxtime,update)
