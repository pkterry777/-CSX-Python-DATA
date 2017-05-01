num = {'1':'壹','2':'貳','3':'參',
       '4':'肆','5':'伍','6':'陸',
       '7':'柒','8':'捌','9':'玖'}
 
locate = {'1':'元','2':'拾','3':'佰','4':'仟','5':'萬'}
 
n = input()
 
location = len(n)
for i in range(len(n)):
    print(num[n[i]]+locate[str(location)],end='')
    location -= 1
print('整')
