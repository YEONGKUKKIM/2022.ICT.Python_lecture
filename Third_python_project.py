import numpy as np
from random import *
import random
import pandas as pd

class Hanwoo:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        print ('한우 키우기 게임을 시작하겠습니다!')
        
    def Genration(self,onwer):
        self.owner = onwer
        My_animal_number_init = self.number
        name = self.name
        sex_list = ["수컷","암컷"]*int(My_animal_number_init/2)
        random.shuffle(sex_list)
        pheno = list(map(lambda x : round(x,1),list(np.random.normal(340,2,My_animal_number_init))))
        data_set = pd.DataFrame(zip(sex_list,pheno),columns=['Sex','Pheno'],index=My_animal_name_list)
        print (f'{onwer}님의 한우 농장이 생성 되었습니다. 아래와 같은 한우를 획득하셨습니다.')
        print (data_set)
        return data_set
        
    def Mating_system(self,male,female,new,data):
        self.male = male
        self.female = female
        self.new = new
        self.data_set = data
        if data_set.loc[male,'Sex'] == data_set.loc[female,'Sex']:
            print ("*** Warnings : You input animals have same sex.")
            print ("*** Warnings : Please put data set has male and female animals.")
            pass
        else:
            new_pheno = int((int(data_set.loc[male,'Pheno']) + int(data_set.loc[female,'Pheno']))/2 + round(uniform(-3,3),1))
            new_sex = ["수컷","암컷"]
            random.shuffle(new_sex)
            data_mat = pd.DataFrame(zip([new_sex[0]],[new_pheno]),columns=['Sex','Pheno'],index=[new])
            data_set.loc[new] = [new_sex[0],new_pheno]
        return data_set


def Run(name1,name2,name3,Player):
    for i in range(3):
        if i == 0:
            data.Mating_system(name1,name2,name3,data_set)
            print (data_set)
        else:
            data.Mating_system(input("Input Male name! : "),input("Input Female name! : "),input("Input New name! : "),data_set)
            print (data_set)
        if i == 2 :
            print (data_set)
            print (f"{Player}님의 농장에서 한우 육종하기 게임은 끝이 났습니다. Game finish!")
            print ("Please check the best animal you have!")



My_animal_name_list = ['우롱','초롱','커피','우유','딸기','수박']
data = Hanwoo(My_animal_name_list,6)

data_set = data.Genration('김영국1')
Run('우롱','초롱','바나나','김영국1')

data_set = data.Genration('김영국2')
Run('우롱','초롱','바나나','김영국2')



