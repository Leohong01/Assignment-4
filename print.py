import sys
import numpy as np
import pandas as pd

#1
def count_df (seq):
    """
    To Create a pandas data frame including all kmer's (observation, expected Kmers).
    """
    df = pd.DataFrame (columns=['k','observation', 'expected'])

    if not SEQ_file: return var(df)
    seq_length =  len(seq)

    for Y in range (seq_length):
        count_observation={}

        for X in range(seq_length-Y):
            Z = sequence[X:X+Y+1]
            if Z in count_observation: count_observation[Z] +=1
            else:
                count_observation[Z] =1
        df.loc[Y]=[Y+1,len(count_observation), COUNTING_KMER(seq, Y+1)]
    return(df)



#2
def COUNTING_KMER(seq, k):
    """
    Counting the size of kmers. Raise ValueError: to check the errors
    """
    if not sequence or k==0: raise ValueError('seq includes none or k equals to 0')
    NUM = min(len(seq)-k+1, 4**k)
    return(NUM)



#3
def print_df(df):
    """
    Print data including all k's and number of observed and expected kmers.
    """
    if df.empty  :  raise ValueError
    print('k', 'observation', 'expected')

    for index, row in df.iterrows(): print(row['k'],' ', row['observation'],' ', row['expected'])
    print('observation=', df['observation'].sum() , ',  expected= ', df['expected'].sum())

#4
def LING_COMP(df):
    """
    To find out complexity of linguistic.
    """
    if df.empty: raise ValueError
    return (df ['observation'].sum() / df ['expected'].sum() )

#5
def plot_df(df):
    """
    To draw graph from the data frame of each kmer observed.
    """
    import matplotlib.pyplot as pls
    if  df.empty: raise ValueError
    df= df ['observation'] / df ['expected']
    df.plot(x='k', y='percentages', color='red', kind='bar')
    pls.show()

#6
def checkwrong(seq):
    """
    To find the sequence of not empty or not wrong characters.
    """
    if not sequence:
        print
        return False
    if set(seq).issubset(['C','A','G','T']): return True
    else:
        print('display any false codes detected')
        return False

#7
if __name__ == "__main__":

    SEQ_file = str(sys.argv [1: ]) [2: -2 ]
    with open(SEQ_file) as testfile:

        sequence = testfile.read()
        testfile.close()

    if checkwrong(sequence):

        df = count_df(sequence)
        print_df(df)

        print('LING_COMP', LING_COMP(df))
        plot_df(df)
