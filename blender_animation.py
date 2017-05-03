import bpy

filename = '/Users/anubhav/Desktop/16823/Project/RSOLP_Video/newPositions.txt'

objName = 'Ball'
obj = bpy.data.objects[objName]
(x, y, z) = obj.location
startX = None
startY = None
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

# Load file and parse
objName, locations = parseFile(filename)


c = 1 # frequency of frame

#locations = [(1, 2, 3), (4, 5, 6)]

for i in range(len(locations)):
    (x, y, z) = locations[i] if locations[i] is not None else (x, y, z)
    obj.location.x = x
    obj.location.y = y
    #obj.location.z = z
    obj.keyframe_insert(data_path="location", frame=i*c)
