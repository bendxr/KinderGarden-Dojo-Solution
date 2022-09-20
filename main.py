class Garden:
  STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
  FLOWERS = {'C': 'Clover', 'R': 'Radishes', 'G': 'Grass', 'V': 'Violets'}
  
  def __init__(self, garden, students=STUDENTS):
    garden = garden.split()
    flowers = zip(*[iter(garden[0])]*2 + [iter(garden[1])]*2)
    self.pots = dict(zip(sorted(students), flowers))
    if students:
      self.STUDENTS = students
    
  def plants(self, who):
    plantswho = map(self.FLOWERS.get, self.pots[who])
    return f'{" ".join(plantswho)}'

  def list(self):
    for s in self.STUDENTS:
      p = self.plants(s)
      print(f'{s} : {p} \n')


garden = Garden('CRGGVRCGRVCGRVGGGVRRGVVV\nVRCCCGCRRGVCGCRVVCVGCGCV')
garden.list()

small_garden = Garden('VVGGVR\nCCRRGC', ['Allen', 'Kim', 'Lea'])
small_garden.list()
