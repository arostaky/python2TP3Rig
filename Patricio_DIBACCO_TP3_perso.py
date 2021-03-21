import maya.cmds as cmds
cmds.file(f=True, new=True)
# Une classe de personnages
class Perso():
    """Classe de Personnages"""
    def modelTete(self):
        cmds.polyCube(name="tete")
        cmds.move(10, y=True)
        cmds.polySmooth( 'tete.f[0:5]', dv=1 )
    def modelCorp(self):
        cmds.polyCube(name="corp", w = 1, h = 3)
        cmds.move(8, y=True)
        cmds.polySmooth( 'corp.f[0:5]', dv=1 )
    def modelLeftArm(self):
        cmds.polyCube(name="leftArm", w = 2, h = 0.25)
        cmds.scale(0.3, z = True)
        cmds.move(1.3,9,0)
        cmds.polySmooth( 'leftArm.f[0:5]', dv=1 )
    def modelRightArm(self):
        cmds.polyCube(name="rightArm", w = 2, h = 0.25)
        cmds.scale(0.3, z = True)
        cmds.move(-1.3,9,0)
        cmds.polySmooth( 'rightArm.f[0:5]', dv=1 )
    def modelLeftLeg(self):
        cmds.polyCube(name="leftLeg", w = 0.3, h = 3.5)
        cmds.scale(0.3, z = True)
        cmds.move(-0.3,6,0)
        cmds.polySmooth( 'leftLeg.f[0:5]', dv=1 )
    def modelRightLeg(self):
        cmds.polyCube(name="rightLeg", w = 0.3, h = 3.5)
        cmds.scale(0.3, z = True)
        cmds.move(0.3,6,0)
        cmds.polySmooth( 'rightLeg.f[0:5]', dv=1 )
toto=Perso()
toto.modelTete()
toto.modelCorp()
toto.modelLeftArm()
toto.modelRightArm()
toto.modelLeftLeg()
toto.modelRightLeg()
