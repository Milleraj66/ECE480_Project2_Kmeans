'''
File Name: Kmeans_Manhattan2.py
Author:    Arthur J. Miller
Date:      02-17-2016
Update:     02-22-2016 AJM
update:     02-23-2016 AJM
update:     02-24-2016 AJM
Purpose:   K-Means Clustering using manhattan distance scheme
Details:    Using Example given on blackboard
            -3 clusters
            -8 Points: (2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(4,9)
            -distance using manhattan : d(a,b) = |x2-x1|+|y2-y1|
TODO: not getting floating point answers
'''

class Points(object):
    # Constructors
    def __init__(self):
        self.x = 0
        self.y = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Makes objects iterable
    def __iter__(self):
         return self
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
#########################################END Points CLASS###################################################3

def main():
    #******************Define Variables
    # Define data points "data"
    data = []
    data.append(Points(2,10))
    data.append(Points(2,5))
    data.append(Points(8,4))
    data.append(Points(5,8))
    data.append(Points(7,5))
    data.append(Points(6,4))
    data.append(Points(1,2))
    data.append(Points(4,9))
    # Define # of clusters "k"
    k = 3
    # Define # of data points "d"
    d = len(data)
    # Define each clusters temp center "centroidList"
    centroidList = []
    # Define 2d Cluster Matrix "cluster"
    cluster = []
    for i in range(k):
        cluster.append([])

    #******************ALGORITHM K-Means
    ##### 1. Initialize center values (these are discrete so we can use same starting points as given examples)
    centroidList.append(data[0])
    centroidList.append(data[3])
    centroidList.append(data[6])

    ##### 7. repeat loop until algorithm converges
    iterations = 0
    while(1):
        ##### House Keeping Tasks
        # Empty clusters for next iteration
        del cluster[:]
        # Redifne 2d cluster array
        for i in range(k):
            cluster.append([])
        ##### 2. Calulate Distance values using manhattan distance
        ##### 3. Assign points to clusters by calculating which cluster has min distance
        for i in range(d):
            comp = []   # list holding distances to be compared
            for j in range(k):
               comp.append(dist_man(centroidList[j],data[i]))
            minVal = min(comp)
            minIndex = comp.index(minVal)
            cluster[minIndex].append(data[i])
        ##### 4. Re-Calculate center values by taking average of cluster values
        centroidList_Old = list(centroidList)
        for i in range(k):
            centroidList[i] = calc_center(cluster[i])
        ##### 5. Check for convergance
        counter = 0
        for i in range(k):
            if (centroidList[i].x != centroidList_Old[i].x):
                break
            elif(centroidList[i].y != centroidList_Old[i].y):
                break
            else:
                counter += 1
        ##### 6. Stop algorithm if converges
        if(counter == k):
            break
        # HouseKeeping: Print each iterations cluster values
        print("After iteration:",iterations )
        print("Intermediate Cluster Values:")
        for xl in range(k):
            for obj in cluster[xl]:
                print("Cluster #:",xl,"Pt: (",obj.x,",",obj.y,")")
        iterations += 1
        ##################################### END WHILE(1)
    print("Total number of iterations to converge:",iterations )
    print("Final Cluster Values:")
    for xl in range(k):
        for obj in cluster[xl]:
            print("Cluster #:",xl,"Pt: (",obj.x,",",obj.y,")")
#########################################END MAIN###################################################3

#### FUNCTIONS
# pass in cluster (list of Point obj's) and return new center pt
def calc_center(cluster):
    xsum = 0.0
    ysum = 0.0
    for obj in cluster:
        xsum += obj.x
        ysum += obj.y
    xmean = xsum/len(cluster)
    ymean = ysum/len(cluster)
    mean = Points(xmean,ymean)
    return mean

# pass in data Point obj, return manhattan distance from current center Point obj
def dist_man(center, point):
    return abs(center.x-point.x)+abs(center.y-point.y)
#########################################END FUNCTIONS###################################################3

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()