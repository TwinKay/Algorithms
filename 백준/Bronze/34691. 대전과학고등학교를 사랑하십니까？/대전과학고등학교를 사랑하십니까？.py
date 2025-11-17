dic = {
    'animal': 'Panthera tigris',
    'tree': 'Pinus densiflora',
    'flower': 'Forsythia koreana'
}
while True:
    s = input().strip()
    
    if s == 'end':
        break
    else:
        print(dic[s])