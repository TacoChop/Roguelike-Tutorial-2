from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

#Friendly
player = Actor(
    char='@',
    color=(255, 255, 255),
    name='Player',
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

#Enemies
maint_bot = Actor(
    char='o',
    color=(222, 158, 40),
    name='\u001b[36;1mMaintainence Bot\u001b[0m',
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

sec_bot = Actor(
    char='V',
    color=(30, 56, 29),
    name='\u001b[31mSecurity Bot\u001b[0m',
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)