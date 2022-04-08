
import collections
def canFinish(numCourses, prerequisites): 
    courses = collections.defaultdict(set)
    pres = collections.defaultdict(set)
    for course, pre in prerequisites:
        courses[course].add(pre)
        pres[pre].add(course)
    no_pre_courses = [n for n in range(numCourses) if not courses[n]]
    count = 0
    while no_pre_courses:
        no_pre = no_pre_courses.pop()
        count+=1 
        for course in pres[no_pre]:
            courses[course].remove(no_pre)
            if not courses[course]:
                no_pre_courses.append(course)
    return count == numCourses

    '''
    Time complexity: O(E+V) where V is the number of courses, and E is the number of dependencies.

    '''

a = 2 
b = [[1,0]]
a = 2 
b = [[1,0],[0,1]]

print(canFinish(a,b))