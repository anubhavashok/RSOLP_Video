import bpy

filename = '/Users/anubhav/Desktop/16823/Project/RSOLP_Video/newPositions.txt'

objName = 'Ball'
obj = bpy.data.objects[objName]
obj.animation_data_clear()
(x, y, z) = obj.location
startX = None
startY = None

bot = bpy.data.objects['bot']
right = bpy.data.objects['right']
img = bpy.data.images.load(filepath='/Users/anubhav/Desktop/16823/Project/RSOLP_Video/example/moving_ball/no_ball_cropped.jpg')

def parseFile(filename):
    startX = None
    startY = None
    lines = open(filename).read().split('\n')
    lines = lines[:-1]
    objName = lines[0].split()[0]
    locations = []
    for l in lines[1:]:
        args = l.split()
        frameNo = args[0]
        curX = float(args[1]) if args[1] != 'None' else None
        curY = float(args[2]) if args[1] != 'None' else None
        startX = startX if startX else curX
        startY = startY if startY else curY
        if curX:
            locations.append(((curX - startX)/400.0 + x, (curY - startY)/400.0 + y, 0.0))
        else:
            locations.append(None)
    return objName, locations

import collections
def parseFile2(filename):
    lines = open(filename).read().split('\n')
    lines = lines[:-1]
    objName = lines[0].split()[0]
    locations = collections.OrderedDict()
    for l in lines[1:]:
        args = l.split()
        if args[1] != 'None':
            frameNo = int(args[0])
            curX = float(args[1])
            curY = float(args[2])
            locations[frameNo] = (curX, curY)
    return objName, locations

def normalizeLocations(locations):
    for frameNo in locations:
        (x, y) = locations[frameNo]
        x = x/float(img.size[0]) * bot.dimensions[0]/2.0
        y = y/float(img.size[1]) * right.dimensions[1]/2.0
        locations[frameNo] = (x, y)
    prevX = list(locations.values())[0][0]
    prevY = list(locations.values())[0][1]
    for frameNo in locations:
        (x, y) = locations[frameNo]
        tempX = x
        tempY = y
        x -= prevX
        y -= prevY
        prevX = tempX
        prevY = tempY
        locations[frameNo] = (x, y)
    return locations

# Load file and parse
objName, locations = parseFile2(filename)
locations = normalizeLocations(locations)

c = 1 # frequency of frame

#locations = [(1, 2, 3), (4, 5, 6)]
'''
for i in range(len(locations)):
    (x, y, z) = locations[i] if locations[i] is not None else (x, y, z)
    obj.location.x = x
    obj.location.y = y
    #obj.location.z = z
    obj.keyframe_insert(data_path="location", frame=i*c)
'''
obj.location.x = -2.51091
obj.location.y = -22.20513
obj.location.z = -3.13994

obj.keyframe_insert(data_path='location', frame=1)

for frameNo in locations:
    obj.location.x -= locations[frameNo][0]
    obj.location.y -= locations[frameNo][1]
    print(obj.location.x, obj.location.y)
    obj.keyframe_insert(data_path="location", frame=frameNo)

