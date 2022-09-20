class Garden:
  STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
  FLOWERS = {'C': 'Clover', 'R': 'Radishes', 'G': 'Grass', 'V': 'Violets'}
  
  def __init__(self, garden, students=STUDENTS):
    # parameters
    # garden <string>: plants sowed, ordered by row
    # students <array> (optional): students that have a garden
    self.students = {s: [] for s in students}
    for row in garden.split('\n'):
      for i in range(0, len(row), 2):
        s = students[i//2]
        self.students[s].append(Garden.FLOWERS[row[i]])
        self.students[s].append(Garden.FLOWERS[row[i+1]])
    
  def plants(self, who):
    # main method to implemented  ; the one that will be tested
    # returns a string: the 4 species sowed in who's garden
    return " ".join(self.students[who])
    
  def list(self):
    # helper method ; optional
    # returns a string : the list of the species sowed in the garden, person by person
    # <student>: <plant1> <plant2> <plant3> <plant4>
    return "\n".join(f"{student}: {self.plants(student)}" for student in self.students)

garden = Garden('CRGGVRCGRVCGRVGGGVRRGVVV\nVRCCCGCRRGVCGCRVVCVGCGCV')
print(garden.list())

small_garden = Garden('VVGGVR\nCCRRGC', ['Allen', 'Kim', 'Lea'])
print(small_garden.list())
