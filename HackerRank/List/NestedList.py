"""Given the names and grades for each student in a Physics class of N students, store them in a nested list and
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints
2<=N<=5

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Ex


There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
so we order their names alphabetically and print each name on a new line."""

from typing import List, Any, Union

if __name__ == '__main__':
    Matrix: List[Union[List[Any], List[Union[str, float]]]] = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50],
                                                               ['Shaheen', 51]]

    #Matrix: List[Union[List[Any], List[Union[str, float]]]] = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
    #['Akriti', 41], ['Harsh', 39]]
    """print("Enter Number of Students:")
    N = int(input())
    for _ in range(N):
        print("Enter Student Name:")
        name = input()
        print ("Enter Grades for ", name, ' :')
        score = float(input())
        Matrix.append([name,score])"""
    Matrix = sorted(Matrix, key=lambda x: x[1], reverse=False)
    MatrixRowLen = len(Matrix)

    print(Matrix)

    Row: int = 0
    LowestScore = Matrix[Row][1]

    while Matrix[Row][1] == LowestScore:
        Row += 1

    SecondLowestGrade = Matrix[Row][1]
    SecondLowestGradeStudent = list()
    print(Row)
    while Matrix[Row][1] == SecondLowestGrade:
        SecondLowestGradeStudent.append(Matrix[Row][0])
        if Row == MatrixRowLen-1:
            break
        Row += 1

    SecondLowestGradeStudent.sort()
    for student in SecondLowestGradeStudent:
        print(student)