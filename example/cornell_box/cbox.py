import bpy
import mathutils
import string
import math
import os
import math

os.chdir('/Users/anubhav/Downloads/RSOLP_Annotator_Source/example/cornell_box')

#Set resolution
render = bpy.context.scene.render
render.filepath = '//'
render.resolution_x = 512
render.resolution_y = 512
render.resolution_percentage = 100

#Create scene root node
scene = bpy.context.scene
root = bpy.data.objects.new('scene', None)
root.location = (0, 0, 0)
root.rotation_euler = (3.14159/2, 0, 0)
root.scale = (1, 1, 1)
scene.objects.link(root)

#Create camera
camdata = bpy.data.cameras.new('cameraData')
camdata.lens_unit = 'FOV'
cam = bpy.data.objects.new('camera', camdata)
cam.matrix_local = ([0.999948, -0.008667, 0.005357, 0], [0.008667, 0.999962, 0.000046, 0], [0.005358, -0.000000, 0.999986, 0], [0, 0, 0, 1])
f = 368.061914
ppx = 256.422458
ppy = 304.741150
maxdim = max(render.resolution_x,render.resolution_y)
camdata.angle = 2*math.atan(0.5*maxdim/f)
camdata.shift_x = -(render.resolution_x/2-ppx)/maxdim
camdata.shift_y = -(render.resolution_y/2-ppy)/maxdim
camdata.dof_distance = 0.0
camdata.clip_start = 5.996369
camdata.clip_end = 1000.0
camdata.luxrender_camera.use_clipping = True
camdata.luxrender_camera.luxrender_film.write_png = True
camdata.luxrender_camera.luxrender_film.write_flm = False
camdata.luxrender_camera.luxrender_film.luxrender_tonemapping.type = 'linear'
bpy.context.scene.luxrender_sampler.haltspp = 500
scene.objects.link(cam)
cam.parent = root
bpy.data.scenes[0].camera = bpy.data.objects['camera']

def setUV(me, vals):
    for i in range(len(vals)):
        me.uv_layers[0].data[i].uv = vals[i]
    return
########## Scene boundaries ##########

#Box verts
verts = ((-6.364086, -5.000000, -14.099105),
         (-6.259342, 7.114094, -14.099105),
         (6.151884, 7.181517, -14.099105),
         (5.988890, -5.000000, -13.966741),
         (-6.364086, -5.000000, -5.899105),
         (-6.259342, 7.114094, -5.899105),
         (6.151884, 7.181517, -5.899105),
         (5.988890, -5.000000, -5.766741))

#mid wall
name = 'mid'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(0.000000,1.000000,2.000000,3.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])

#left wall
name = 'left'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(5.000000,4.000000,0.000000,1.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])

#top wall
name = 'top'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(1.000000,5.000000,6.000000,2.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])

#right wall
name = 'right'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(3.000000,2.000000,6.000000,7.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])

#bot wall
name = 'bot'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(4.000000,0.000000,3.000000,7.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])

#back wall
name = 'back'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
me.from_pydata(verts, [], [(7.000000,6.000000,5.000000,4.000000)])
me.update(calc_edges=True)
mat = bpy.data.materials.new(name+'Mat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new(name+'Tex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/'+name+'.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
texslottrans = mat.texture_slots.add()
texslottrans.texture_coords = 'UV'
texslottrans.texture = bpy.data.textures.new(name+'TexTransp', 'IMAGE')
texslottrans.texture.image = bpy.data.images.load('//textures/'+name+'Transp.png')
texslottrans.use = False
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name
mat.luxrender_transparency.transparent = True
mat.luxrender_transparency.alpha_source = 'texture'
mat.luxrender_transparency.alpha_usefloattexture = True
mat.luxrender_transparency.alpha_floattexturename = texslottrans.texture.name
mat.luxrender_transparency.inverse = True
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0,0), (0,1), (1,1), (1,0)])


########## Lights ##########
name = 'light1'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
lv = (
      (-1.321653,7.140917,-11.988000),
      (1.515488,7.156330,-12.015613),
      (1.548963,7.156512,-10.834269),
      (-1.325990,7.140894,-10.757661),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 17.273769
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)

name = 'light2'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
lv = (
      (6.055412,-0.028386,-11.728670),
      (6.054619,-0.087685,-10.468461),
      (6.084779,2.166329,-10.536115),
      (6.084799,2.167872,-11.748818),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 1.000000
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)

name = 'light3'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
lv = (
      (-6.320443,0.047518,-11.020096),
      (-6.321030,-0.020404,-12.310546),
      (-6.300044,2.406776,-12.376614),
      (-6.300520,2.351746,-11.126348),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 1.000000
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)



########## Supporting surfaces ##########
#Image as material for extruded objects
mat = bpy.data.materials.new('sceneMat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new('sceneTex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/cbox-reflectance.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name

name = 'surf1'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
sv = (
      (-3.419289,-1.427966,-9.520411),
      (0.364390,-1.427966,-10.235898),
      (-0.923996,-1.427966,-12.217383),
      (-4.768794,-1.427966,-11.927562),
      (-3.255029,-5.000000,-9.043637),
      (0.528650,-5.000000,-9.759123),
      (-0.759735,-5.000000,-11.740609),
      (-4.604533,-5.000000,-11.450788),
     )
me.from_pydata(sv, [], [(0,1,2), (0,2,3), (4,5,6), (4,6,7), (0,4,5), (0,5,1), (1,5,6), (1,6,2), (2,6,7), (2,7,3), (3,7,4), (3,4,0)])
me.update(calc_edges=True)
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0.240234, 0.294922),(0.523438, 0.304688),(0.443359, 0.320312),(0.240234, 0.294922),(0.443359, 0.320312),(0.210938, 0.316406),(0.242187, 0.005859),(0.539117, 0.036701),(0.453127, 0.098332),(0.242187, 0.005859),(0.453127, 0.098332),(0.211260, 0.089055),(0.240234, 0.294922),(0.242187, 0.005859),(0.539117, 0.036701),(0.240234, 0.294922),(0.539117, 0.036701),(0.523438, 0.304688),(0.523438, 0.304688),(0.539117, 0.036701),(0.453127, 0.098332),(0.523438, 0.304688),(0.453127, 0.098332),(0.443359, 0.320312),(0.443359, 0.320312),(0.453127, 0.098332),(0.211260, 0.089055),(0.443359, 0.320312),(0.211260, 0.089055),(0.210938, 0.316406),(0.210938, 0.316406),(0.211260, 0.089055),(0.242187, 0.005859),(0.210938, 0.316406),(0.242187, 0.005859),(0.240234, 0.294922),])
name = 'surf2'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
sv = (
      (-0.194576,2.108791,-10.513401),
      (2.987664,2.108791,-9.991826),
      (4.212259,2.108791,-12.029950),
      (0.778438,2.108791,-12.410998),
      (-0.349893,-5.000000,-11.936416),
      (2.832347,-5.000000,-11.414841),
      (4.056942,-5.000000,-13.452965),
      (0.623121,-5.000000,-13.834014),
     )
me.from_pydata(sv, [], [(0,1,2), (0,2,3), (4,5,6), (4,6,7), (0,4,5), (0,5,1), (1,5,6), (1,6,2), (2,6,7), (2,7,3), (3,7,4), (3,4,0)])
me.update(calc_edges=True)
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0.482422, 0.548828),(0.710938, 0.558594),(0.748047, 0.533203),(0.482422, 0.548828),(0.748047, 0.533203),(0.541016, 0.527344),(0.478516, 0.103516),(0.678304, 0.091021),(0.716416, 0.139045),(0.478516, 0.103516),(0.716416, 0.139045),(0.531612, 0.145173),(0.482422, 0.548828),(0.478516, 0.103516),(0.678304, 0.091021),(0.482422, 0.548828),(0.678304, 0.091021),(0.710938, 0.558594),(0.710938, 0.558594),(0.678304, 0.091021),(0.716416, 0.139045),(0.710938, 0.558594),(0.716416, 0.139045),(0.748047, 0.533203),(0.748047, 0.533203),(0.716416, 0.139045),(0.531612, 0.145173),(0.748047, 0.533203),(0.531612, 0.145173),(0.541016, 0.527344),(0.541016, 0.527344),(0.531612, 0.145173),(0.478516, 0.103516),(0.541016, 0.527344),(0.478516, 0.103516),(0.482422, 0.548828),])
bpy.context.scene.update()
bpy.ops.wm.save_mainfile(filepath="cbox.blend")

