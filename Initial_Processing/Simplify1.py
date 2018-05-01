def main():
    infile=open("sourcefile.fa","r")
    outfile=open("outfile.txt","w")
    dic={}
    flag1=False
    flag2=False
    for line in infile:
        line=line.strip()
        if line[0]==">":
            count=0
            while count<=len(line) and line[count]!="/":
                count+=1
            name=line[:count+1]
            flag1=True
            outfile.write(name)
            outfile.write("\n")

        elif line!="":
            key=line
            flag2=True
            outfile.write(key)
            outfile.write("\n")

        elif line=="":
            outfile.write("\n")

        if flag1==True and flag2==True:
            dic[name]=key



            




main()