import bpy

filename = 'newPositions.txt'

def parseFile(filename):
    lines = open(filename).read().split('\n')
    lines = lines[:-1]
    objName = lines[0].split()[0]
    locations = []
    for l in lines[1:]:
        args = l.split()
        frameNo = args[0]
        locations.append((float(args[1]), float(args[2]), 0.0) if args[1] != 'None' else None)
    return objName, locations

# Load file and parse
objName, locations = parseFile(filename)

objName = 'Cube'

obj = bpy.data.objects[objName]
c = 50 # frequency of frame

#locations = [(1, 2, 3), (4, 5, 6)]

for i in range(len(locations)):
    (x, y, z) = locations[i] if locations[i] != None
    obj.location.x = x
    obj.location.y = y
    #obj.location.z = z
    obj.keyframe_insert(data_path="location", frame=i*c)
