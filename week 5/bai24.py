class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def so_sanh_thuat_toan(self):
        print("Dijkstra: O(V^2) hoac O(E log V) - Chi ap dung cho canh trong so khong am.")
        print("Bellman-Ford: O(V*E) - Chay duoc tren canh am, phat hien chu trinh am.")
        print("A*: Su dung ham Heuristic hop le de dinh huong giam so dinh can duyet truyen thong.")

g = Graph(1)
g.so_sanh_thuat_toan()