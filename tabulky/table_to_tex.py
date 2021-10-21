with open('params.csv', 'r') as vstup:
    with open('tabulka.tex','w') as vystup:
        line=vstup.readline()
        line=line.split(';')
        n=len(line)
        vystup.write('\begin{tabular}{')
        for i in range(n):
            vystup.write('|c')
        vystup.write('|}'+'\n')
        vystup.write('\hline'+'\n')
        for i in range(n-1):
            vystup.write(str(line[i])+'&')
        vystup.write(str(line[n-1])+'\\'+'\\'+'\n')
        for line in vstup:
            line=line.split(';')
            vystup.write('\hline'+'\n')
            for i in range(n-1):
                vystup.write(str(line[i])+'&')
            vystup.write(str(line[n-1])+'\\'+'\\'+'\n')
        vystup.write('\hline'+'\n')
        vystup.write('\end{tabular}')

            
