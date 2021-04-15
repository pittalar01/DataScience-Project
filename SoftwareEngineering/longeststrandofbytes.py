# -*- coding: utf-8 -*-
"""longeststrandofbytes.ipynb
    Code file
"""

import pandas as pd
#For finding the longest strand
def findLength(A, B):
    memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                memo[i][j] = memo[i+1][j+1]+1
    return max(max(row) for row in memo)

#Method for choosing 2 files at once to find if it contains the longest strand
def files(l):
    df = pd.DataFrame(columns=['Filename1','Filename2','Length'])
    list2={}
    q=len(l)
    print(l)
    for i in range(q):
        with open(l[i], mode='rb') as file:
            fileContent = file.read()
            file.close()
        for j in range(i+1,q):
            with open(l[j], mode='rb') as file:
                fileContent2 = file.read()
                file.close()
            t=findLength(fileContent,fileContent2)
            s=l[i]
            a=l[j]
            df=df.append({'Filename1':l[i],'Filename2':l[j],'Length':t},ignore_index=True)
    print(df[df['Length']==df['Length'].max()])

if __name__ == "__main__":
  #send input  binary files for finding the longest strands through the files() function: As sample I have considered 4 files
  files([r'/content/sample.1',r'/content/sample.2',r'/content/sample.3',r'/content/sample.4'])
