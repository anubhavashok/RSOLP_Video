import bpy
import mathutils
import string
import math
import os
import math

os.chdir('/Users/anubhav/Desktop/16823/Project/RSOLP_Video/example/moving_ball')

#Set resolution
render = bpy.context.scene.render
render.filepath = '//'
render.resolution_x = 686
render.resolution_y = 1219
render.resolution_percentage = 100

#Create scene root node
scene = bpy.context.scene
root = bpy.data.objects.new('scene', None)
root.location = (0, 0, 0)
root.rotation_euler = (3.14159/2, 0, 0)
root.scale = (-1, 1, 1)
scene.objects.link(root)

#Create camera
camdata = bpy.data.cameras.new('cameraData')
camdata.lens_unit = 'FOV'
cam = bpy.data.objects.new('camera', camdata)
cam.matrix_local = ([0.999727, 0.021272, 0.009664, 0], [-0.021271, 0.999774, -0.000206, 0], [-0.009666, -0.000000, -0.999953, 0], [0, 0, 0, 1])
f = 1303.776217
ppx = 469.015703
ppy = 624.261970
maxdim = max(render.resolution_x,render.resolution_y)
camdata.angle = 2*math.atan(0.5*maxdim/f)
camdata.shift_x = -(render.resolution_x/2-ppx)/maxdim
camdata.shift_y = -(render.resolution_y/2-ppy)/maxdim
camdata.dof_distance = 0.0
camdata.clip_start = 11.860978
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
verts = ((-8.499925, -5.000000, 26.402054),
         (-8.742469, 6.364279, 26.402054),
         (8.239133, 6.285653, 26.402054),
         (8.583225, -5.000000, 26.732281),
         (-8.499925, -5.000000, 11.402054),
         (-8.742469, 6.364279, 11.402054),
         (8.239133, 6.285653, 11.402054),
         (8.583225, -5.000000, 11.732281))

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
      (-3.738263,6.341109,15.504488),
      (-3.753279,6.341179,20.397617),
      (-4.495077,6.344613,20.366841),
      (-4.483026,6.344558,15.501028),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 25.000000
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)

name = 'light2'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
lv = (
      (2.952435,6.310131,15.422047),
      (3.690302,6.306715,15.426315),
      (3.677046,6.306776,20.207905),
      (2.940836,6.310185,20.277002),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 25.000000
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
texslot.texture.image = bpy.data.images.load('//textures/no_ball_cropped-reflectance.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name

name = 'surf1'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
sv = (
      (3.732351,-3.304255,26.871281),
      (-3.828760,-3.304255,26.980163),
      (-3.639924,-3.304255,10.075920),
      (3.498656,-3.304255,9.887397),
      (3.699656,-5.000000,26.667303),
      (-3.861455,-5.000000,26.776185),
      (-3.672619,-5.000000,9.871942),
      (3.465961,-5.000000,9.683419),
     )
me.from_pydata(sv, [], [(0,1,2), (0,2,3), (4,5,6), (4,6,7), (0,4,5), (0,5,1), (1,5,6), (1,6,2), (2,6,7), (2,7,3), (3,7,4), (3,4,0)])
me.update(calc_edges=True)
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0.960641, 0.353197),(0.427114, 0.359760),(0.000000, 0.144009),(0.960641, 0.353197),(0.000000, 0.144009),(1.358601, 0.123500),(0.957726, 0.284288),(0.420126, 0.290993),(-0.027866, -0.047403),(0.957726, 0.284288),(-0.027866, -0.047403),(1.358956, -0.070698),(0.960641, 0.353197),(0.957726, 0.284288),(0.420126, 0.290993),(0.960641, 0.353197),(0.420126, 0.290993),(0.427114, 0.359760),(0.427114, 0.359760),(0.420126, 0.290993),(-0.027866, -0.047403),(0.427114, 0.359760),(-0.027866, -0.047403),(0.000000, 0.144009),(0.000000, 0.144009),(-0.027866, -0.047403),(1.358956, -0.070698),(0.000000, 0.144009),(1.358956, -0.070698),(1.358601, 0.123500),(1.358601, 0.123500),(1.358956, -0.070698),(0.957726, 0.284288),(1.358601, 0.123500),(0.957726, 0.284288),(0.960641, 0.353197),])
########## Sphere ##########
#Image as material for extruded objects
mat = bpy.data.materials.new('sceneMat')
mat.use_shadeless = True
mat.diffuse_intensity = 1
mat.specular_intensity = 0
texslot = mat.texture_slots.add()
texslot.texture_coords = 'UV'
texslot.texture = bpy.data.textures.new('sceneTex', 'IMAGE')
texslot.texture.image = bpy.data.images.load('//textures/no_ball_cropped-reflectance.png')
texslot.texture.luxrender_texture.type_label = 'Use Blender Texture'
mat.luxrender_material.luxrender_mat_matte.Kd_usecolortexture = True
mat.luxrender_material.luxrender_mat_matte.Kd_colortexturename = texslot.texture.name

name = 'sphere1'
ob = bpy.ops.mesh.primitive_uv_sphere_add(segments=100, ring_count=100, size=0.5, location=(471.000000, 920.203125, 0.000000))bpy.context.scene.objects.link(ob)
ob.parent = root
bpy.context.scene.update()
bpy.ops.wm.save_mainfile(filepath="no_ball_cropped.blend")

