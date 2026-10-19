
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = [list(c) for c in initial_centroids]

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = [
                sum((x - y) ** 2 for x, y in zip(point, centroid))
                for centroid in centroids
            ]
            closest = distances.index(min(distances))
            clusters[closest].append(point)

        new_centroids = []

        for i, cluster in enumerate(clusters):
            if cluster:
                centroid = [
                    sum(point[j] for point in cluster) / len(cluster)
                    for j in range(len(centroids[i]))
                ]
                new_centroids.append(centroid)
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            centroids = new_centroids
            break

        centroids = new_centroids

    final_centroids = [
        tuple(round(value, 4) for value in centroid)
        for centroid in centroids
    ]

    return final_centroids
