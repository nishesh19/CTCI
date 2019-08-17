'''
4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
'''


def topologicalSort(dependencies: dict, project, visited: set, buildOrder: list):
    if project not in visited:
        visited.add(project)
        dependentProjects = dependencies[project]
        for dpnProject in dependentProjects:
            topologicalSort(dependencies, dpnProject, visited, buildOrder)
        buildOrder.append(project)


projects = input().split(',')
no = int(input())

graph = {x: [] for x in projects}

for i in range(no):
    dependencies = input().split(',')
    graph[dependencies[0]].append(dependencies[1])

visited = set()
ordering = []

for project in projects:
    topologicalSort(graph, project, visited, ordering)

while ordering:
    print(ordering.pop())
