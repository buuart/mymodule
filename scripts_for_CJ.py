#  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐   ┬┬ ┬┌┐┌┌─┐┬  ┌─┐
#  │  │ │││││  ├┬┘├┤  │ ├┤    ││ │││││ ┬│  ├┤ 
#  └─┘└─┘┘└┘└─┘┴└─└─┘ ┴ └─┘  └┘└─┘┘└┘└─┘┴─┘└─┘
#  by buuart

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

fig, ax = plt.subplots()

# histogram our data with numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 100)

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

# here comes the tricky part -- we have to set up the vertex and path
# codes arrays using moveto, lineto and closepoly

# for each rect: 1 for the MOVETO, 3 for the LINETO, 1 for the
# CLOSEPOLY; the vert for the closepoly is ignored but we still need
# it to keep the codes aligned with the vertices
nverts = nrects*(1 + 3 + 1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(
    barpath, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())


def animate(i):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, bins = np.histogram(data, 100)
    top = bottom + n
    verts[1::5, 1] = top
    verts[2::5, 1] = top
    return [patch, ]

ani = animation.FuncAnimation(fig, animate, 100, repeat=False, blit=True)
plt.show()


def scatter(iteration):
	for i in range(iteration):
		x = np.random.random_integers(200)
		y = np.random.random_integers(200)
		scale=np.random.random_integers(50,100)
		plt.scatter(x,y,c='blue',alpha=0.3, marker='o', s=scale, edgecolor='None')
	plt.grid(False)
	plt.show()




def brus(side,hm):
    x=[]
    for a in range(side):
        for b in range(side):
            e=[a,b]
            x.append(e)
    for i in range(9):
        bpy.ops.mesh.primitive_cube_add(radius=0.5, view_align=False, enter_editmode=False, location=(c[i][0], c[i][1], z[i]/2))
        bpy.ops.transform.resize(value=(0, 0, z[i]), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


import bpy
bpy.ops.object.select_by_layer()
bpy.ops.object.delete(use_global=False)
def voxel(num,size,scale):
    bpy.ops.mesh.primitive_monkey_add(view_align=False, enter_editmode=False, location=(0, 0, 0))
    bpy.ops.transform.resize(value=(size, size, size), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'BLOCKS'
    bpy.context.object.modifiers["Remesh"].octree_depth = num
    bpy.context.object.modifiers["Remesh"].scale = scale


voxel(6,5,0.99)


import bpy
import numpy as np
bpy.ops.object.select_by_layer()
bpy.ops.object.delete(use_global=False)

def brus(side,hm,radiusVal):
    x=[]
    for a in range(side):
        for b in range(side):
            e=[a,b]
            x.append(e)
    c=x
    z=[]
    for i in range(side**2):
        z.append(np.random.random())
    z=np.array(z)
    z=z*hm
    for i in range(side**2):
        h=z[i]/(1/radiusVal)
        bpy.ops.mesh.primitive_cube_add(radius=radiusVal, view_align=False, enter_editmode=False, location=(c[i][0], c[i][1], h))
        bpy.ops.transform.resize(value=(0, 0, z[i]), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


brus(25,12,0.05)

#bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, view_align=False, enter_editmode=False, location=(13.8888, 13.1058, -16.8145), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))


cosR=[]
for i in range(10):
	cosR=np.concatenate((cosR,z))
corR=cosR.reshape(10,10)


from PIL import Image, ImageDraw
image=Image.open('name.bmp')
width = image.size[0] 
height = image.size[1]	
pix = image.load()
def pixelbrus(radiusVal):
	for a in range(width):
		for b in range(height):
			h=(pix[a,b][0])/2
			py.ops.mesh.primitive_cube_add(radius=radiusVal, view_align=False, enter_editmode=False, location=(a, b, h))
			bpy.ops.transform.resize(value=(0, 0, h*2), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)



from PIL import Image, ImageDraw
image=Image.open('name.bmp')
width = image.size[0] 
height = image.size[1]	
pix = image.load()



file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"w")
for a in range(len(e)):
	for b in range(len(e[a])):
		file.write(str(e[a][b]))
		file.write(',')
file.close()






bpy.ops.mesh.primitive_grid_add(radius=1, view_align=False, enter_editmode=False, location=(1.27318, 8.4546, 8.74063), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 'var_for_hei'), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.object.editmode_toggle()





import bpy
import numpy as np
import os

bpy.ops.object.select_by_layer()
bpy.ops.object.delete(use_global=False)
h=19
v=37
file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"r")
t=file.read()
e=t.split(',')
for i in range(len(e)):
    e[i]=float(e[i])
e=np.array(e)
e=e.reshape(h,v)
file.close()


for x in range(h):
    for y in range(v):
        bpy.ops.mesh.primitive_grid_add(radius=0.1, view_align=False, enter_editmode=False, location=(x, y, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, e[x][y]), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.object.editmode_toggle()



from PIL import Image, ImageDraw
import numpy as np



def imagePrep(imageName,vertScaleDemult=25,inversion=0):
	image=Image.open(imageName)
	v=image.size[0]
	h=image.size[1]
	pix=image.load()
	e=[]
	for a in range(v):
		for b in range(h):
			e.append(pix[a,b])
	e=np.array(e)
	if(inversion==1):
		e=255-e
	e=e/vertScaleDemult
	file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"w")
	for a in range(len(e)):
			file.write(str(e[a]))
			if(a!=len(e)-1):
				file.write(',')
	file.close()
	print('h =',h,'v =',v)


def imageBW(height,width,q1,output_file):
	height=int(height)
	width=int(width)
	img=Image.new('L',(height,width),(255))
	draw = ImageDraw.Draw(img)
	for x in range(height):
		for y in range(width):
			if(int(q1[x][y])>255):
				color=255
			else:
				color=int(q1[x][y])
			draw.point((y,x),(color))
	img.save(output_file, "JPEG")
	del draw



import bpy
import numpy as np
import os

bpy.ops.object.select_by_layer()
bpy.ops.object.delete(use_global=False)
#set value
h=19
v=37
side=0.8
#END
file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"r")
t=file.read()
e=t.split(',')
for i in range(len(e)):
    e[i]=float(e[i])
e=np.array(e)
e=e.reshape(h,v)
file.close()

for x in range(h):
    for y in range(v):
        bpy.ops.mesh.primitive_grid_add(radius=(side*0.5), view_align=False, enter_editmode=False, location=(x, y, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, e[x][y]), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.object.editmode_toggle()

def maps(x,  in_min,  in_max,  out_min,  out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def gray(img):
	img=ImageOps.grayscale(img)
	return img

def sigmoid(x,a=1):#x - value, a - gain
	return 1/(1+m.e**(-1*a*x))


for i in range(10):
	sigmoid((0.1*i*20)-10)



e=byteFromImg2('const_images\\cj.bmp')
e=HexToBin(e)
e=np.swapaxes(e,1,0)
e=arrayTo595(e)

def byteFromImg2(fileName): 
	# импортирует чб изображение, переводит его в серого градации для дальнейшей обработки
	# принимает значение в виде строки
	# родительская функия FelixScreen
	img=Image.open(fileName)
	img=ImageOps.flip(img)
	img=ImageOps.grayscale(img)
	e=img.load()
	imgW=img.size[0]
	imgH=img.size[1]
	q=[]
	for a in range(imgW):
		for b in range(imgH):
			q.append(e[a,b])
	q=np.array(q).reshape(imgW,imgH)
	img.close()
	q=q.swapaxes(0,1)
	return q