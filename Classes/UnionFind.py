from Models.StateModel import StateModel


class UnionFind:
    def __init__(self, tree: dict[int, int], weights: dict[int, int], owner: dict[int, str], claimed: dict[str, int], scores: dict[str, int]):
        self.tree: dict[int, int] = {int(k): v for k, v in tree.items()}
        self.weights: dict[int, int] = {int(k): v for k, v in weights.items()}
        self.owner: dict[int, str] = {int(k): v for k, v in owner.items()}
        self.claimed: dict[str, int] = claimed
        self.scores: dict[str, int] = scores
        
    def find(self, id: int) -> int:
        if self.tree[id] == id:
            return id
        # Path compression
        self.tree[id] = self.find(self.tree[id])
        return self.tree[id]
    
    def claim(self, id: int, team: str):
        if self.owner[id] is not None:
            raise ValueError(f"Card {id} is already claimed by {self.owner[id]}")
        self.owner[id] = team
        self.claimed[team] += 1
        
        with StateModel() as sm:
            edges = sm.get_state(id).neighbors
        for e in edges:
            if self.owner[e] == self.owner[id]:
                self.union(id, e)
        
        self.scores[team] = max(self.scores[team], self.weights[self.find(id)])

    def union(self, u: int, v: int):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        
        if self.weights[root_u] < self.weights[root_v]:
            root_u, root_v = root_v, root_u
        self.tree[root_v] = root_u
        self.weights[root_u] += self.weights[root_v]
    
    @staticmethod
    def new_uf(ids: list[int]) -> 'UnionFind':
        tree = {id: id for id in ids}
        weights = {id: 1 for id in ids}
        owner = {id: None for id in ids}
        claimed = {'red': 0, 'blue': 0}
        scores = {'red': 0, 'blue': 0}
        return UnionFind(tree, weights, owner, claimed, scores)
    
    def to_dict(self):
        return self.__dict__
    
    def get_scores(self) -> dict[str, tuple[int, int]]:
        return {
            'red': (self.scores['red'], self.claimed['red']),
            'blue': (self.scores['blue'], self.claimed['blue']),
        }
    
    def get_largest_clusters(self) -> dict[str, list[int]]:
        heads = {
            'red': -1,
            'blue': -1,
        }
        
        for id in self.tree.keys():
            if self.owner[id] is not None:
                if self.weights[id] >= self.scores[self.owner[id]]:
                    heads[self.owner[id]] = id
        
        clusters = {
            'red': [],
            'blue': [],
        }
        
        for id in self.tree.keys():
            if self.find(id) == heads['red']:
                clusters['red'].append(id)
            if self.find(id) == heads['blue']:
                clusters['blue'].append(id)
        
        return clusters
        