import matplotlib


#--------------------------How to use-------------------------------------
#Remplir les variables suivantes suivant vos compétences:
skills2=['python','C++','Julia','Javascript'] # exemple: skills2=['julia','python','javascript']
note=[8,9,6,10] # exemple: note=[7,8,5] ne doit pas dépasser 10
skills1=['Curiosité','Ingénieux','Force de proposition','Prise de recul','réactivité']
pourcentage1=[60,70,80,40,100] # ne doit pas dépasser 100
skills0=['Backend', 'Frontend', 'Algorithme', 'Web scrapping']
pourcentage0=[40,30,15,15]
#cliquer sur F5 ou run 
#Faire marcher un digramme en particulier:
a=[] #la compétence exemple: a=['python','java']
b=[] # pourcentage
#Pour le diagramme en baton:
#run_baton(a,b)
#kiviat
#run_kiviat(a,b)
#circulaire
#run_circulaire(a,b)




#-----------------------Advenced Use---------------------------------
#Set possible:
coloree=list(matplotlib.colors.cnames.keys())
hatchee=['','/', '|', '-', '+', 'x', 'o', 'O', '.', '*']
linestylee=['solid', 'dashed', 'dashdot', 'dotted']
barwidthee=[i for i in range(10)]



#Diagramme en kiviat
#diagramme_kiviat(skills,prcntg,colorxaxis,coloryaxis,linestyle,edgecolor)
#Set default:
coloryaxis='blue'
colorxaxis='blue'
linestyle='solid'
edgecolor='blue'

#Diagramme en baton
#diagramme_baton(skills2,note,hatch1,hatch2,colorlinewidth,colorbarfilled,colorline,colorlinenonefilled,linestyle,barwidth)
#Set default:
colorlinewidth='blue'
colorbarfilled='green'
colorline='black'
colorlinenonefilled='white'
hatch1=''
hatch2='-'
linestyle='solid'
barwidth=1





#--------------------------------Code----------------------------------
from math import pi
import matplotlib.pyplot as plt
def diagramme_circulaire(skills,prcntg):  
    explode=(0,)*(len(skills)+1)
    skills=skills+['autre']
    prcntg=prcntg+[100-sum(prcntg)]
    plt.pie(prcntg, explode=explode, labels=skills, autopct='%1.00f%%', startangle=100, shadow=True)
    plt.axis('equal')
    return plt.show()

def diagramme_kiviat(skills,prcntg,colorxaxis,coloryaxis,linestyle,edgecolor):
    N = len(skills)
    
    x_as = [n / float(N) * 2 * pi for n in range(N)]
    prcntg += prcntg[:1]
    x_as += x_as[:1]
    plt.rc('axes', linewidth=0.5, edgecolor=edgecolor)
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
    ax.xaxis.grid(True, color=colorxaxis, linestyle=linestyle, linewidth=0.5)
    ax.yaxis.grid(True, color=coloryaxis, linestyle=linestyle, linewidth=0.5)
    plt.xticks(x_as[:-1], [])
    plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])
    ax.plot(x_as, prcntg, linewidth=0, linestyle=linestyle, zorder=3)
    ax.fill(x_as, prcntg, 'b', alpha=0.3)
    plt.ylim(0, 100)
    for i in range(N):
           angle_rad = i / float(N) * 2 * pi
    
           if angle_rad == 0:
               ha, distance_ax = "center", 10
           elif 0 < angle_rad < pi:
               ha, distance_ax = "left", 1
           elif angle_rad == pi:
               ha, distance_ax = "center", 1
           else:
               ha, distance_ax = "right", 1
    
           ax.text(angle_rad, 100 + distance_ax, skills[i], size=10, horizontalalignment=ha, verticalalignment="center")
    plt.show()

def  diagramme_baton(skills2,note,hatch1,hatch2,colorlinewidth,colorbarfilled,colorline,colorlinenonefilled,linestyle,barwidth):
    bar_Width = barwidth
    y1 = note
    y2 = [10-i for i in y1]
    r = range(len(y1))
    plt.barh(r, y1, height = bar_Width, color = [colorbarfilled for i in y1],
           edgecolor = [colorlinewidth for i in y1], linestyle = linestyle, hatch =hatch1,
           linewidth = 3)
    plt.barh(r, y2, height = bar_Width, left = y1, color = [colorlinenonefilled for i in y1],
           edgecolor = [colorline for i in y1], linestyle = linestyle , hatch = hatch2,
           linewidth = 3)
    plt.yticks(range(len(y1)), skills2)
    plt.show()
def run():
    diagramme_baton(skills2,note,hatch1,hatch2,colorlinewidth,colorbarfilled,colorline,colorlinenonefilled,linestyle,barwidth)
    diagramme_kiviat(skills1,pourcentage1,colorxaxis,coloryaxis,linestyle,edgecolor)
    diagramme_circulaire(skills0,pourcentage0)
def run_baton(a,b):
    diagramme_baton(a,b,hatch1,hatch2,colorlinewidth,colorbarfilled,colorline,colorlinenonefilled,linestyle,barwidth)
def run_circulaire(a,b):
    diagramme_circulaire(a,v)
def run_kiviat(a,b):
    diagramme_kiviat(a,b,colorxaxis,coloryaxis,linestyle,edgecolor)
    
run()
