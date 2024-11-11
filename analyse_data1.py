# +
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('lv-college.csv', sep = ';')
df["autre langue que l'anglais en LV1 en 6ème"]=df["6èmes LV1 espagnol"]+df['6èmes LV1 allemand']+df['6èmes LV1 autres langues']
df["autre langue que l'anglais en LV1 en 5ème"]=df["5èmes LV1 espagnol"]+df['5èmes LV1 allemand']+df['5èmes LV1 autres langues']
df["autre langue que l'anglais en LV1 en 4ème"]=df["4èmes LV1 espagnol"]+df['4èmes LV1 allemand']+df['4èmes LV1 autres langues']
df["autre langue que l'anglais en LV1 en 3ème"]=df["3èmes LV1 espagnol"]+df['3èmes LV1 allemand']+df['3èmes LV1 autres langues']

display(df["6èmes LV1 anglais"].sum())
display(df["5èmes LV1 anglais"].sum())
display(df["4èmes LV1 anglais"].sum())
display(df["3èmes LV1 anglais"].sum())
        
A=["6ème","5ème","4ème","3ème"]
Y=[ 200833,173936,168905,159220]
plt.plot(X,A, label="LV1 autre que l'anglais")
plt.legend()

B=[ 28031,26262,23798,21937]
plt.plot(X,B, label="LV1 espagnol")
plt.legend()


C=[155831,132578,130781,123799]
plt.plot(X,C, label="LV1 allemand")
plt.legend()

D=[3951790,3961318,3944966,3976424]
plt.plot(X,D, label="LV1 anglais")
plt.legend()
plt.show()


# +
X=["6ème","5ème","4ème","3ème"]
Y=[ 878, 771, 737,695]
Z=[16093, 14325,13589, 12789]

plt.plot(X,Y, label="privé")
plt.plot(X,Z,label="public")
plt.title("nombre de personnes faisant une LV1 autre qu'anglais,espagnol et italien")
plt.legend()
plt.show()
# -



# on voit que le nombre de personnes faisant allemand LV1 diminue dans le public mais presque peu dans le privé


