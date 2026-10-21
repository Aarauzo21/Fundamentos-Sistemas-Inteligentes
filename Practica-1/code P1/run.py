# Search methods

import search

ruta_1 = search.GPSProblem('A', 'B'
                       , search.romania)
ruta_2 = search.GPSProblem('O', 'E'
                       , search.romania)

print(search.breadth_first_graph_search(ruta_1).path())
print(search.depth_first_graph_search(ruta_1).path())

print("=== RUTA 1: De Arad (A) a Bucarest (B) ===")

print("\n--- Pathcost ---")
resultado_1A = search.ramificacion_solo_path_cost_search(ruta_1)
print("Camino:", resultado_1A.path())

print("\n--- Pathcost + Subestimacion ---")
resultado_1B = search.subestimacion_graph_search(ruta_1)
print("Camino:", resultado_1B.path())


print("\n\n=== RUTA 2: De Oradea (O) a Eforie (E) ===")

print("\n--- Pathcost  ---")
resultado_2A = search.ramificacion_solo_path_cost_search(ruta_2)
print("Camino:", resultado_2A.path())

print("\n--- Pathcost + Subestimacion ---")
resultado_2B = search.subestimacion_graph_search(ruta_2)
print("Camino:", resultado_2B.path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
