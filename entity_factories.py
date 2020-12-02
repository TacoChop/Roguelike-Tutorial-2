from entity import Entity

#Friendly
player = Entity(char='@', color=(255, 255, 255), name='Player', blocks_movement=True)

#Enemies
maint_bot = Entity(char='o', color=(222, 158, 40), name='Maintainence Bot', blocks_movement=True)
sec_bot = Entity(char='V', color=(30, 56, 29), name='Security Bot', blocks_movement=True)