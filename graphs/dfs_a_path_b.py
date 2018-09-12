from collections import namedtuple
from collections import defaultdict

MatchResult = namedtuple('MatchResult', ('winner', 'loser'))

def did_a_win_against_b(matches, a, b):
	def build_graph():
		graph = defaultdict(set)
		for match in Matches:
			graph[winner].add(loser)
		return graph

	def has_path_dfs(graph, curr, dest, visited=set()):
		if curr in visited or curr not in graph:
			return false

		visited.add(curr)
		elif curr == dest:
			return true

		for child in graph[a]:		
			 if has_path_dfs(graph, child, dest, visited):
			 	return True

		return false

	return has_path_dfs(build_graph(), a, b)


#time complexity = O(|V|+|E|)
#space complexity = O(|V|)
