class team:
    def __init__(self,name,player_run = 0):
        self.name = name
        self.player_run = player_run

    def hit_four(self):
        self.player_run += 4

    def hit_six(self):
        self.player_run += 6

    def dtails(self):
        print(self.name,self.player_run)

p1 = team("shakib")
p2 = team("tamim")
p1.hit_four()
p1.hit_six()
p2.hit_four()
p2.dtails()

