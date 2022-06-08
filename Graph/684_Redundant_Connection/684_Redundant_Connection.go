type UnionFind struct {
    parent []int
    rank []int
    n int
}

func constructUnionFind(n int) UnionFind {
    parent, rank := make([]int, n), make([]int, n)
    
    for i := 0; i < n; i ++ {
        parent[i] = i
        rank[i] = 1
    }
    
    return UnionFind {
        parent: parent,
        rank: rank,
        n: n,
    }
    
}

func (u *UnionFind) Find(x int) int {
    for x != u.parent[x] {
        u.parent[x] = u.parent[u.parent[x]]
        x = u.parent[x]
    }
    
    return u.parent[x]
}

func (u *UnionFind) Union(n1 int, n2 int) bool {
    n1_root, n2_root := u.Find(n1), u.Find(n2)
    
    if n1_root == n2_root {
        return false
    }
    
    if u.rank[n1_root] > u.rank[n2_root] {
        u.parent[n2_root] = n1_root
    } else if u.rank[n2_root] > u.rank[n1_root] {
        u.parent[n1_root] = n2_root
    } else {
        u.parent[n2_root] = n1_root
        u.rank[n1_root] += 1
    }
    
    return true
}

func findRedundantConnection(edges [][]int) []int {
    disjoint_set := constructUnionFind(len(edges) + 1)
    
    for i := 0; i < len(edges); i++ {
        if disjoint_set.Union(edges[i][0], edges[i][1]) == false {
            return []int{edges[i][0], edges[i][1]}
        }
    }
    
    return []int{}
}
