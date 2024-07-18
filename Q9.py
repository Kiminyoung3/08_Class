

class Ground:
    def __init__(self, loc, size, build, mon, year):
        self.G_loc = loc
        self.G_size = size
        self.G_build = build
        self.G_mon = mon
        self.G_year = year

    def check(self):
        print("위치:", self.G_loc, "\n평수:", self.G_size, "\n건물:", self.G_build, "\n가격:", self.G_mon, "\n연도:", self.G_year)



my_home = Ground("서울", "35평", "아파트", "30억", "2024년")

my_home.check()
