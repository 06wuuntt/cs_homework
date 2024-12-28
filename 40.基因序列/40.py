def search(startgene, dna:str, endgene):
    splitdna = dna.split(startgene)
    del splitdna[0]
    # print(splitdna)
    if len(splitdna) == 0:
        return False
    if any(j in i for i in splitdna for j in endgene) == False:
        return False
    for i in splitdna:
        searchdna.append(i[:-3])
    
def main():
    startgene = input()
    endgene = input().split()
    dna = input()
    if search(startgene, dna, endgene) == False:
        print('No gene')
    result = sorted(searchdna, key = lambda x: (len(x), x))
    for i in result:
        print(i)

searchdna = list()
main()