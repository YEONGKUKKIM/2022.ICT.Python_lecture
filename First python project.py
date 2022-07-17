def revSeq(seq):
    data1=seq[::-1]
    compDic={'A':'T','C':'G','G':'C','T':'A'}
    result=""
    for i in data1:
        result += compDic[i]
    return result

def DNAtoRNA(data):
    Seq_RNA=data.replace("T","U")
    return Seq_RNA

Codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
        'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W',
    }

def RNAtoProtein(data):
    protein =""
    if len(data)%3 == 0:
        for i in range(0, len(data), 3):
            codon = data[i:i + 3]
            protein+= Codon_table[codon]
    return protein

def main():
    #seq="ACTTACGGCATTAGACATTAG"
    seq=input("Enter Sequence data : ")
    revComp_result=revSeq(seq)
    #Step 1. Complementary Sequence code
    print ("Sequence : ", seq)
    print ("Complementary Sequence : ", revComp_result)
    
    #Step 2. DNA to RNA Seuqence code
    RNA_result=DNAtoRNA(seq)
    print ("RNA Sequnce : ",RNA_result)

    #Step 3. RNA to Protein Translation code 
    Protein_result=RNAtoProtein(RNA_result)
    print ("Protein Sequence : ", Protein_result)

    #Save all results
    File_name = input("Enter file name : ")
    File_name2 = str(File_name)+".txt"
    file_result=open(File_name2,"w")
    file_result.write("Sequence : "+ seq + "\n")
    file_result.write("Complementary Sequence : "+ revComp_result + "\n")
    file_result.write("RNA Sequnce : " +RNA_result + "\n")
    file_result.write("Protein Sequence : " + Protein_result + "\n")
    file_result.close()
    print ("Results saved on file to ", File_name)

main()


