import networkx as nx
import matplotlib.pyplot as plt

# Create the original graph
G = nx.Graph()



# Define the new route
new_route = [
    "Sungai Wang Plaza", "The Exchange TRX", "Berjaya Times Square", 
    "Lalaport Bukit Bintang City Centre", "Mid Valley Megamall", 
    "One Utama", "The Starling", "Sunway Pyramid", "IOI City Mall", 
    "Sunway Velocity Mall", "MyTOWN Shopping Centre", 
    "Sunway Putra Mall", "Quill City Mall Kuala Lumpur", 
    "Suria KLCC", "Pavilion Kuala Lumpur", "Sungai Wang Plaza"
]

# Define the distance matrix (example data; replace with actual values)
distance_matrix = {
    "Pavilion Kuala Lumpur": {
        "Suria KLCC": 2.1,
        "Mid Valley Megamall": 8.1,
        "MyTOWN Shopping Centre": 3.7,
        "Sunway Pyramid": 17.3,
        "The Exchange TRX": 1.4,
        "Sunway Putra Mall": 4.7,
        "Quill City Mall Kuala Lumpur": 4.2,
        "Sunway Velocity Mall": 3.5,
        "IOI City Mall": 25.9,
        "One Utama": 16.6,
        "The Starling": 15.2,
        "Sungai Wang Plaza": 0.6,
        "Lalaport Bukit Bintang City Centre": 1.2,
        "Berjaya Times Square": 0.9,
    },
    "Suria KLCC": {
        "Pavilion Kuala Lumpur": 2.9,
        "Mid Valley Megamall": 13,
        "MyTOWN Shopping Centre": 5.1,
        "Sunway Pyramid": 21.6,
        "The Exchange TRX": 3.4,
        "Sunway Putra Mall": 6.4,
        "Quill City Mall Kuala Lumpur": 5.9,
        "Sunway Velocity Mall": 5.7,
        "IOI City Mall": 29.2,
        "One Utama": 19.4,
        "The Starling": 18.8,
        "Sungai Wang Plaza": 3.4,
        "Lalaport Bukit Bintang City Centre": 3.8,
        "Berjaya Times Square": 3.4,
    },
    "Mid Valley Megamall": {
        "Pavilion Kuala Lumpur": 9.3,
        "Suria KLCC": 11,
        "MyTOWN Shopping Centre": 11.1,
        "Sunway Pyramid": 11.3,
        "The Exchange TRX": 9.4,
        "Sunway Putra Mall": 9.9,
        "Quill City Mall Kuala Lumpur": 9.3,
        "Sunway Velocity Mall": 10.9,
        "IOI City Mall": 25.5,
        "One Utama": 11.4,
        "The Starling": 10.8,
        "Sungai Wang Plaza": 9.5,
        "Lalaport Bukit Bintang City Centre": 8.8,
        "Berjaya Times Square": 8.4,
    },
    "MyTOWN Shopping Centre": {
        "Pavilion Kuala Lumpur": 3.2,
        "Suria KLCC": 4.5,
        "Mid Valley Megamall": 9.4,
        "Sunway Pyramid": 18.8,
        "The Exchange TRX": 2.9,
        "Sunway Putra Mall": 6.8,
        "Quill City Mall Kuala Lumpur": 6.2,
        "Sunway Velocity Mall": 1.7,
        "IOI City Mall": 24.7,
        "One Utama": 17.5,
        "The Starling": 17.8,
        "Sungai Wang Plaza": 3.4,
        "Lalaport Bukit Bintang City Centre": 2.2,
        "Berjaya Times Square": 2.1,
    },
    "Sunway Pyramid": {
        "Pavilion Kuala Lumpur": 21.8,
        "Suria KLCC": 23.8,
        "Mid Valley Megamall": 15.3,
        "MyTOWN Shopping Centre": 22.4,
        "The Exchange TRX": 22.1,
        "Sunway Putra Mall": 21.8,
        "Quill City Mall Kuala Lumpur": 21.3,
        "Sunway Velocity Mall": 21.4,
        "IOI City Mall": 24,
        "One Utama": 15.7,
        "The Starling": 13.9,
        "Sungai Wang Plaza": 22,
        "Lalaport Bukit Bintang City Centre": 21.5,
        "Berjaya Times Square": 21.2,
    },
    "The Exchange TRX": {
        "Pavilion Kuala Lumpur": 2.6,
        "Suria KLCC": 4,
        "Mid Valley Megamall": 8.9,
        "MyTOWN Shopping Centre": 2.3,
        "Sunway Pyramid": 19.2,
        "Sunway Putra Mall": 7.5,
        "Quill City Mall Kuala Lumpur": 8.9,
        "Sunway Velocity Mall": 2.8,
        "IOI City Mall": 25.3,
        "One Utama": 17.3,
        "The Starling": 17.6,
        "Sungai Wang Plaza": 2.9,
        "Lalaport Bukit Bintang City Centre": 2,
        "Berjaya Times Square": 1.7,
    },
    "Sunway Putra Mall": {
        "Pavilion Kuala Lumpur": 4.6,
        "Suria KLCC": 4.6,
        "Mid Valley Megamall": 7.9,
        "MyTOWN Shopping Centre": 6.9,
        "Sunway Pyramid": 18,
        "The Exchange TRX": 5.3,
        "Quill City Mall Kuala Lumpur": 2.1,
        "Sunway Velocity Mall": 7.5,
        "IOI City Mall": 29,
        "One Utama": 12.1,
        "The Starling": 14,
        "Sungai Wang Plaza": 5,
        "Lalaport Bukit Bintang City Centre": 6,
        "Berjaya Times Square": 5.4,
    },
    "Quill City Mall Kuala Lumpur": {
        "Pavilion Kuala Lumpur": 2.6,
        "Suria KLCC": 1.7,
        "Mid Valley Megamall": 8.5,
        "MyTOWN Shopping Centre": 6.1,
        "Sunway Pyramid": 18.6,
        "The Exchange TRX": 3.3,
        "Sunway Putra Mall": 2.2,
        "Sunway Velocity Mall": 6.8,
        "IOI City Mall": 28.6,
        "One Utama": 15.4,
        "The Starling": 15.2,
        "Sungai Wang Plaza": 2.9,
        "Lalaport Bukit Bintang City Centre": 3.7,
        "Berjaya Times Square": 3.4,
    },
    "Sunway Velocity Mall": {
        "Pavilion Kuala Lumpur": 3.9,
        "Suria KLCC": 5.4,
        "Mid Valley Megamall": 9.7,
        "MyTOWN Shopping Centre": 0.65,
        "Sunway Pyramid": 19,
        "The Exchange TRX": 3.7,
        "Sunway Putra Mall": 9,
        "Quill City Mall Kuala Lumpur": 7.4,
        "IOI City Mall": 24.2,
        "One Utama": 18.1,
        "The Starling": 17,
        "Sungai Wang Plaza": 3.6,
        "Lalaport Bukit Bintang City Centre": 2.8,
        "Berjaya Times Square": 3.1,
    },
    "IOI City Mall": {
        "Pavilion Kuala Lumpur": 26,
        "Suria KLCC": 32.1,
        "Mid Valley Megamall": 23.9,
        "MyTOWN Shopping Centre": 23.7,
        "Sunway Pyramid": 24.4,
        "The Exchange TRX": 26.6,
        "Sunway Putra Mall": 29.1,
        "Quill City Mall Kuala Lumpur": 28.6,
        "Sunway Velocity Mall": 23,
        "One Utama": 32.7,
        "The Starling": 33,
        "Sungai Wang Plaza": 26.3,
        "Lalaport Bukit Bintang City Centre": 24.3,
        "Berjaya Times Square": 26.5,
    },
     "One Utama": {
        "The Starling": 2.8, "Sungai Wang Plaza": 15.2, "Lalaport Bukit Bintang City Centre": 17.7,
        "Berjaya Times Square": 17, "Pavilion Kuala Lumpur": 16.5, "Suria KLCC": 17.1,
        "Mid Valley Megamall": 11.6, "MyTOWN Shopping Centre": 19.9, "Sunway Pyramid": 14.1,
        "The Exchange TRX": 17.5, "Sunway Putra Mall": 15.1, "Quill City Mall Kuala Lumpur": 14.6,
        "Sunway Velocity Mall": 18.7, "IOI City Mall": 35.3
    },
    "The Starling": {
        "One Utama": 2.8, "Sungai Wang Plaza": 15.6, "Lalaport Bukit Bintang City Centre": 14.7,
        "Berjaya Times Square": 14.8, "Pavilion Kuala Lumpur": 14.2, "Suria KLCC": 15.9,
        "Mid Valley Megamall": 9.3, "MyTOWN Shopping Centre": 17.6, "Sunway Pyramid": 11.3,
        "The Exchange TRX": 14.9, "Sunway Putra Mall": 13.5, "Quill City Mall Kuala Lumpur": 12.9,
        "Sunway Velocity Mall": 16.5, "IOI City Mall": 32.5
    },
    "Sungai Wang Plaza": {
        "One Utama": 15.2, "The Starling": 15.6, "Lalaport Bukit Bintang City Centre": 1,
        "Berjaya Times Square": 0.5, "Pavilion Kuala Lumpur": 1.4, "Suria KLCC": 1.9,
        "Mid Valley Megamall": 7.7, "MyTOWN Shopping Centre": 3.4, "Sunway Pyramid": 17.1,
        "The Exchange TRX": 1.5, "Sunway Putra Mall": 4.6, "Quill City Mall Kuala Lumpur": 4,
        "Sunway Velocity Mall": 3.1, "IOI City Mall": 25.7
    },
    "Lalaport Bukit Bintang City Centre": {
        "One Utama": 17.7, "The Starling": 14.7, "Sungai Wang Plaza": 1, "Berjaya Times Square": 2.3,
        "Pavilion Kuala Lumpur": 3.7, "Suria KLCC": 7.6, "Mid Valley Megamall": 6.4,
        "MyTOWN Shopping Centre": 3.4, "Sunway Pyramid": 16.1, "The Exchange TRX": 3.2,
        "Sunway Putra Mall": 6.1, "Quill City Mall Kuala Lumpur": 5.6, "Sunway Velocity Mall": 3.5,
        "IOI City Mall": 25
    },
    "Berjaya Times Square": {
        "One Utama": 17, "The Starling": 14.8, "Sungai Wang Plaza": 0.5, "Lalaport Bukit Bintang City Centre": 2.3,
        "Pavilion Kuala Lumpur": 2.6, "Suria KLCC": 6.6, "Mid Valley Megamall": 7.2,
        "MyTOWN Shopping Centre": 2.6, "Sunway Pyramid": 16.5, "The Exchange TRX": 1.9,
        "Sunway Putra Mall": 6.5, "Quill City Mall Kuala Lumpur": 5.9, "Sunway Velocity Mall": 2.7,
        "IOI City Mall": 25
    }
}


# Create a graph
G = nx.Graph()

# Add nodes and edges with weights
for source, destinations in distance_matrix.items():
    for destination, weight in destinations.items():
        G.add_edge(source, destination, weight=weight)

# Draw the network
pos = nx.spring_layout(G, seed=42)  # Positions nodes
nx.draw(G, pos, with_labels=True, node_size=4000, node_color="lightblue", font_size=6)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("TSP Network Diagram")
plt.show()

# Add the new route to the graph
G_route = G.copy()  # Copy the original graph to keep it intact
for i in range(len(new_route) - 1):
    source = new_route[i]
    destination = new_route[i + 1]
    weight = distance_matrix[source].get(destination, 0)  # Fetch the distance
    G_route.add_edge(source, destination, weight=weight)

# Preserve the original layout (using spring_layout from the original graph)
pos = nx.spring_layout(G, seed=42)  # Preserve the layout

# Draw the graph with the new route on top
plt.figure(figsize=(12, 10))
nx.draw(G_route, pos, with_labels=True, node_size=4000, node_color="lightgreen", font_size=8)

# Highlight the new route edges in red for emphasis
new_route_edges = list(zip(new_route[:-1], new_route[1:]))
nx.draw_networkx_edges(G_route, pos, edgelist=new_route_edges, edge_color="red", width=2)

# Draw edge labels (distances)
labels = nx.get_edge_attributes(G_route, 'weight')
nx.draw_networkx_edge_labels(G_route, pos, edge_labels=labels)

plt.title("Network Graph with New Route Highlighted in Red")
plt.show()


