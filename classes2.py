class A:
   MName=''
   def moon(self):
      yxfjk;;qqfjll jjkoel;;lkmmnn self.MName ='moon_name'

#but here cls method its use is different 

   @classmethod
   def moon(cls):
        instance=cls()
        instance.MName='moon_name'
        print(instance.MName)

#a=A()
#a.moon('hi')
A.moon()
