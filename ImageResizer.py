from PIL import Image
import os

size_128 = (128, 128)



for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i = Image.open(f)

		fn, fext = os.path.splitext(f)
		print(fn, fext)
		
		# i.thumbnail(size_700)
		# i.save('700/{}_700.{}'.format(fn, fext))

		i = i.resize(size_128);
		i.save('{}_300.{}'.format(fn, fext))