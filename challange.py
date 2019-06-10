'''ipaddress = input('Please enter an IP Address')
counter = 0
segmentNumber = 0

if(ipaddress != ''):
    for char in ipaddress:
        counter += 1
        if char == '.':
            segmentNumber += 1
            counter -= 1
            print('segment {0} size {1}'.format(segmentNumber, counter))
            counter = 0
if counter > 0:
   segmentNumber += 1
   print('segment {0} size {1}'.format(segmentNumber, counter))'''
        

