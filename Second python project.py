############################### Alignment using program
from Bio import Align

aligner = Align.PairwiseAligner(match_score=1.0)

seq2 = "ACTTACGGCA"
seq3 = "TTACG"

alignLocal = aligner.align(seq2,seq3)

for x in alignLocal:
    print (x)


############################# GC contents & alignment program
class DNA_Toolkit:
    def __init__(self):
        print ("##################################")
        print ("##Start DNA Toolkit by Yeongkuk!##")
        print ("##################################")
    def Count_amino_acid(self,seq):
        seq_list=list(seq)
        Amino_acid_Dic={}
        for i in seq_list:
            try:
                Amino_acid_Dic[i] += 1
            except:
                Amino_acid_Dic[i] = 1    
        return Amino_acid_Dic

class Kmer_make:
    def __init__(self,seq2):
        print ("Start program about Alignment!")
        self.seq=seq2 
        

    def setdata(self):
        seq=self.seq 
        Ref_dMer={}
        nn=range(1,len(seq)+1,1)
        for k in nn:
            for i in range(0,len(seq)-k+1,1):
                Ref_Motif = seq[i:i+k]
                if Ref_dMer.get(Ref_Motif):
                    Ref_dMer[Ref_Motif] += 1
                else:
                    Ref_dMer[Ref_Motif] = 1
        return Ref_dMer

class Align_run():
    def __init__(self,Ref_results,Test_results,original_seq):
        print ("")
        print ("################################################")
        print ("##Ready to excute mapping to reference genome!##")
        print ("################################################")
        print ("")
        self.Ref = Ref_results
        self.Test = Test_results
        self.original = original_seq

    def Run_matching(self):
        Ref = self.Ref
        Test = self.Test
        original = self.original
        for j in (list(Test)[::-1]):
            if j in list(Ref):
                if len(j) == 1 :
                    print ("*** Warning message : Test sequence length is 1. So, Please enter the sequence information!")
                    break
            print ("#########################################################################")
            print (f"    The Original Test sequence is : {original}.")
            print (f"    The maximum sequence matched with Reference is : {j}.")
            print (f"    The maximum sequence length matched with Reference is : {len(j)}.")
            print (f"    Percentage of sequence matching to reference sequence is : {round((len(j)/len(list(Ref)[::-1][0]))*100,3)}%.")
            print ("#########################################################################")
            break
        else:
            pass

def main():
    Ref_sequence="ACTTACGGCA"
    sequence="TTACG"
    Data=DNA_Toolkit()
    Count_acid_result=Data.Count_amino_acid(sequence)
    print ("  1. Results (Count about amino acid!)")
    print ("    A = %d , C = %d , T = %d , G = %d" % (Count_acid_result['A'],Count_acid_result['C'],Count_acid_result['T'],Count_acid_result['G']))
    print ("  2. Results (GC contents(%)!)")
    #print ("GC Content (%) = {0}%".format(round(((int(Count_acid_result['G'])+int(Count_acid_result['C']))*100)/(int(Count_acid_result['C'])+int(Count_acid_result['G'])+int(Count_acid_result['A'])+int(Count_acid_result['T'])),3)))
    print (f"    GC Content (%) = {round(((int(Count_acid_result['G'])+int(Count_acid_result['C']))*100)/(int(Count_acid_result['C'])+int(Count_acid_result['G'])+int(Count_acid_result['A'])+int(Count_acid_result['T'])),3)}%")
    data = Kmer_make(Ref_sequence)
    data2 = Kmer_make(sequence)
    Ref=data.setdata()
    Test=data2.setdata()

    Results=Align_run(Ref,Test,sequence)
    Results.Run_matching()

main()


