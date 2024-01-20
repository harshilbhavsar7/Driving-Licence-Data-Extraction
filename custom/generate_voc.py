import os

def generate_xml(original,image,image_name,predicts,folder):	
		try:
			desfile= os.path.splitext(image_name)[0]+'.xml'
			desdir = os.path.join(folder,desfile)
			h, w, c = image.shape
			with open(desdir,'w') as f:
				content = '''<annotation>
					<folder>images</folder>
					<filename>{}</filename>
					<path>{}</path>
					<source>
						<database>Unknown</database>
					</source>
					<size>
						<width>{}</width>
						<height>{}</height>
						<depth>3</depth>
					</size>
					<segmented>0</segmented>
				'''

				f.write(content.format(image_name,os.path.join(folder,image_name),w,h))	
				for pred in predicts:
					try:
						x1,y1,x2,y2,class_name=int(pred[0]),int(pred[1]),int(pred[2]),int(pred[3]),pred[5]			
						content = '''
						<object>
							<name>{}</name>
							<pose>Unspecified</pose>
							<truncated>0</truncated>
							<difficult>0</difficult>
							<bndbox>
								<xmin>{}</xmin>
								<ymin>{}</ymin>
								<xmax>{}</xmax>
								<ymax>{}</ymax>
							</bndbox>
						</object>
						'''
						f.write(content.format(class_name,x1,y1,x2,y2))
					except Exception as e:
						print(e)
						
				f.write('\n\n</annotation>')
		except Exception as e:
			print(e)




