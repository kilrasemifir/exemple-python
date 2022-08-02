from short_path import Ville, Route, short_path

if __name__ == "__main__":
    # Nodes
    paris = Ville("Paris")
    lille = Ville("Lille")
    strasbourg = Ville("Strasbourg")
    lyon = Ville("Lyon")

    # Edges
    paris_lille_train = Route(paris, lille, 60, "train", 60)
    paris_lille_bus = Route(paris, lille, 10, "bus", 100)
    paris.out_edges = [paris_lille_train, paris_lille_bus]

    lyon_paris_train = Route(lyon, paris, 100, "train", 120)
    lyon_strasbourg_bus = Route(lyon, strasbourg, 50, "train", 160)
    lyon.out_edges.append(lyon_paris_train)
    lyon.out_edges.append(lyon_strasbourg_bus)

    strasbourg_lille = Route(strasbourg, lille, 20, "bus", 180)
    strasbourg.out_edges.append(strasbourg_lille)

    # Calcul du plus court chemin
    path, weight = short_path(lyon, lille, lambda edge: edge.temps)
    print("Le plus court chemin entre Lille et Lyon est:", path, "avec un poids de", weight)




