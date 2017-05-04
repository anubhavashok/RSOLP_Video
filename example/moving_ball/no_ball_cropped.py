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
cam.matrix_local = ([0.999723, 0.023422, 0.002419, 0], [-0.023422, 0.999726, -0.000057, 0], [-0.002419, 0.000000, -0.999997, 0], [0, 0, 0, 1])
f = 2329.395824
ppx = 344.170107
ppy = 559.556445
maxdim = max(render.resolution_x,render.resolution_y)
camdata.angle = 2*math.atan(0.5*maxdim/f)
camdata.shift_x = -(render.resolution_x/2-ppx)/maxdim
camdata.shift_y = -(render.resolution_y/2-ppy)/maxdim
camdata.dof_distance = 0.0
camdata.clip_start = 3.297715
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
verts = ((-4.865485, -5.000000, 34.569484),
         (-5.080799, 4.187043, 34.569484),
         (5.028508, 4.181123, 34.569484),
         (5.250789, -5.000000, 34.618433),
         (-4.865485, -5.000000, 3.169484),
         (-5.080799, 4.187043, 3.169484),
         (5.028508, 4.181123, 3.169484),
         (5.250789, -5.000000, 3.218433))

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
      (-2.579775,4.185578,19.347575),
      (-2.618059,4.185601,25.880745),
      (-3.152627,4.185914,25.892529),
      (-3.087731,4.185876,19.910474),
      (-3.010437,4.185831,19.395726),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3), (0,3,4)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 40.438564
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)

name = 'light2'
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)  
bpy.context.scene.objects.link(ob)
ob.parent = root
lv = (
      (2.119184,4.182826,19.391302),
      (2.627394,4.182529,19.450426),
      (2.700395,4.182486,25.833385),
      (2.168693,4.182797,25.845133),
     )
me.from_pydata(lv, [], [(0,1,2), (0,2,3)])
me.update(calc_edges=True)
emit_mat = bpy.data.materials.new(name+'Mat')
emit_mat.luxrender_emission.use_emission = True
emit_mat.luxrender_emission.gain = 1.000000
emit_mat.luxrender_emission.L_color = [0.500000, 0.500000, 0.500000]
me.materials.append(emit_mat)


########## Sun ##########
sun = bpy.data.lamps.new('sunLamp', type='HEMI')
sun.luxrender_lamp.luxrender_lamp_hemi.type = 'distant'
sun.energy = 14.357659
ob = bpy.data.objects.new('sun', sun)
bpy.context.scene.objects.link(ob)
ob.parent = root
ob.matrix_local = mathutils.Matrix(([-0.001897, -0.001023, 0.999998, 0], [-0.474736, 0.880128, 0.000000, 0], [0.880126, 0.474735, 0.002156, 0], [0, 0, 0, 1]))
ob.location = [0.083253, -0.407959, 18.881722]

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
      (-2.687091,-3.918324,18.720353),
      (-0.665236,-3.918324,16.354854),
      (0.796291,-3.918324,16.705227),
      (2.674273,-3.918324,18.543774),
      (2.807832,-3.918324,18.975846),
      (3.968535,-3.918324,27.085317),
      (3.782273,-3.918324,44.475023),
      (2.472087,-3.918324,48.534062),
      (1.066954,-3.918324,50.242700),
      (-0.076357,-3.918324,50.178716),
      (-1.707779,-3.918324,49.421095),
      (-2.731499,-3.918324,48.066136),
      (-3.683743,-3.918324,44.458307),
      (-3.885061,-3.918324,26.713498),
      (-2.621605,-5.000000,18.503349),
      (-0.599751,-5.000000,16.137850),
      (0.861776,-5.000000,16.488223),
      (2.739759,-5.000000,18.326770),
      (2.873318,-5.000000,18.758843),
      (4.034020,-5.000000,26.868313),
      (3.847758,-5.000000,44.258019),
      (2.537573,-5.000000,48.317058),
      (1.132440,-5.000000,50.025696),
      (-0.010872,-5.000000,49.961712),
      (-1.642294,-5.000000,49.204091),
      (-2.666013,-5.000000,47.849132),
      (-3.618257,-5.000000,44.241303),
      (-3.819575,-5.000000,26.496494),
     )
me.from_pydata(sv, [], [(0,1,2), (0,2,3), (0,3,4), (0,4,5), (0,5,6), (0,6,7), (0,7,8), (0,8,9), (0,9,10), (0,10,11), (0,11,12), (0,12,13), (14,15,16), (14,16,17), (14,17,18), (14,18,19), (14,19,20), (14,20,21), (14,21,22), (14,22,23), (14,23,24), (14,24,25), (14,25,26), (14,26,27), (0,14,15), (0,15,1), (1,15,16), (1,16,2), (2,16,17), (2,17,3), (3,17,18), (3,18,4), (4,18,19), (4,19,5), (5,19,20), (5,20,6), (6,20,21), (6,21,7), (7,21,22), (7,22,8), (8,22,23), (8,23,9), (9,23,24), (9,24,10), (10,24,25), (10,25,11), (11,25,26), (11,26,12), (12,26,27), (12,27,13), (13,27,14), (13,14,0)])
me.update(calc_edges=True)
me.materials.append(mat)
uvTex = me.uv_textures.new(name+'UVTex')
setUV(me, [(0.005831, 0.147290),(0.352770, 0.084944),(0.653061, 0.090687),(0.005831, 0.147290),(0.653061, 0.090687),(0.982507, 0.130883),(0.005831, 0.147290),(0.982507, 0.130883),(0.995627, 0.139907),(0.005831, 0.147290),(0.995627, 0.139907),(0.995627, 0.258037),(0.005831, 0.147290),(0.995627, 0.258037),(0.791545, 0.368783),(0.005831, 0.147290),(0.791545, 0.368783),(0.676385, 0.384370),(0.005831, 0.147290),(0.676385, 0.384370),(0.575802, 0.390933),(0.005831, 0.147290),(0.575802, 0.390933),(0.498542, 0.391753),(0.005831, 0.147290),(0.498542, 0.391753),(0.386297, 0.390933),(0.005831, 0.147290),(0.386297, 0.390933),(0.310496, 0.387651),(0.005831, 0.147290),(0.310496, 0.387651),(0.221574, 0.376166),(0.005831, 0.147290),(0.221574, 0.376166),(0.004373, 0.267061),(0.007289, 0.030801),(0.359103, -0.049424),(0.663207, -0.040722),(0.007289, 0.030801),(0.663207, -0.040722),(0.995530, 0.013161),(0.007289, 0.030801),(0.995530, 0.013161),(1.008501, 0.025001),(0.007289, 0.030801),(1.008501, 0.025001),(1.004615, 0.178765),(0.007289, 0.030801),(1.004615, 0.178765),(0.796003, 0.321194),(0.007289, 0.030801),(0.796003, 0.321194),(0.679952, 0.340844),(0.007289, 0.030801),(0.679952, 0.340844),(0.578811, 0.348919),(0.007289, 0.030801),(0.578811, 0.348919),(0.501220, 0.349687),(0.007289, 0.030801),(0.501220, 0.349687),(0.388522, 0.348212),(0.007289, 0.030801),(0.388522, 0.348212),(0.312440, 0.343704),(0.007289, 0.030801),(0.312440, 0.343704),(0.223242, 0.328576),(0.007289, 0.030801),(0.223242, 0.328576),(0.005379, 0.186693),(0.005831, 0.147290),(0.007289, 0.030801),(0.359103, -0.049424),(0.005831, 0.147290),(0.359103, -0.049424),(0.352770, 0.084944),(0.352770, 0.084944),(0.359103, -0.049424),(0.663207, -0.040722),(0.352770, 0.084944),(0.663207, -0.040722),(0.653061, 0.090687),(0.653061, 0.090687),(0.663207, -0.040722),(0.995530, 0.013161),(0.653061, 0.090687),(0.995530, 0.013161),(0.982507, 0.130883),(0.982507, 0.130883),(0.995530, 0.013161),(1.008501, 0.025001),(0.982507, 0.130883),(1.008501, 0.025001),(0.995627, 0.139907),(0.995627, 0.139907),(1.008501, 0.025001),(1.004615, 0.178765),(0.995627, 0.139907),(1.004615, 0.178765),(0.995627, 0.258037),(0.995627, 0.258037),(1.004615, 0.178765),(0.796003, 0.321194),(0.995627, 0.258037),(0.796003, 0.321194),(0.791545, 0.368783),(0.791545, 0.368783),(0.796003, 0.321194),(0.679952, 0.340844),(0.791545, 0.368783),(0.679952, 0.340844),(0.676385, 0.384370),(0.676385, 0.384370),(0.679952, 0.340844),(0.578811, 0.348919),(0.676385, 0.384370),(0.578811, 0.348919),(0.575802, 0.390933),(0.575802, 0.390933),(0.578811, 0.348919),(0.501220, 0.349687),(0.575802, 0.390933),(0.501220, 0.349687),(0.498542, 0.391753),(0.498542, 0.391753),(0.501220, 0.349687),(0.388522, 0.348212),(0.498542, 0.391753),(0.388522, 0.348212),(0.386297, 0.390933),(0.386297, 0.390933),(0.388522, 0.348212),(0.312440, 0.343704),(0.386297, 0.390933),(0.312440, 0.343704),(0.310496, 0.387651),(0.310496, 0.387651),(0.312440, 0.343704),(0.223242, 0.328576),(0.310496, 0.387651),(0.223242, 0.328576),(0.221574, 0.376166),(0.221574, 0.376166),(0.223242, 0.328576),(0.005379, 0.186693),(0.221574, 0.376166),(0.005379, 0.186693),(0.004373, 0.267061),(0.004373, 0.267061),(0.005379, 0.186693),(0.007289, 0.030801),(0.004373, 0.267061),(0.007289, 0.030801),(0.005831, 0.147290),])
bpy.context.scene.update()
bpy.ops.wm.save_mainfile(filepath="no_ball_cropped.blend")

