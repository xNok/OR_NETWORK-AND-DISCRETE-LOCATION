# Network 
import networkx as nx
# Datavisualization tool
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

class Network:
    """
    Wrapper around networkx to analyse our datasets
    """
    
    def __init__(self, dataset, metadata={}):
        """
        Instanciate networkx graph base on the pandas dataset
        /!\ we assume that the dataset is a set of nodes
        
        """
        self.df = dataset.get()
        self.G  = nx.Graph()
        self.G.add_nodes_from(self.df.T.to_dict().items())
        
        self.metadata = metadata
            
    def plot_nodes(self, node_size=None, node_color=None, metadata={
        "figsize": (10,5),
        "window": [-128, -62, 20, 50]
    }):
        
        # Update metadata
        self.metadata = {**self.metadata, **metadata}
        plt.figure(figsize=self.metadata["figsize"])

        # 1. Create the map with cartopy
        ax = plt.axes(projection=ccrs.PlateCarree())
        ## Extent of continental US.
        ax.set_extent(self.metadata["window"])
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)

        # Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
        states_provinces = cfeature.NaturalEarthFeature(
            category='cultural',
            name='admin_1_states_provinces_lines',
            scale='50m',
            facecolor='none')
        ax.add_feature(states_provinces, edgecolor='gray')
        
        pos = {n:(d["LONGITUDE"],d["LATITUDE"]) for n,d in self.G.nodes.items()}
        if node_size:
            if isinstance(node_size, tuple):
                node_size  = [ x * node_size[1]  for n,x in self.G.nodes.data(node_size[0])]
            else:
                node_size  = [ x for n,x in self.G.nodes.data(node_size)]
        if node_color:
            if isinstance(node_color, tuple):
                node_color  = [ x * node_color[1]  for n,x in self.G.nodes.data(node_color[0])]
            else:
                node_color  = [ x for n,x in self.G.nodes.data(node_color)]

        # 2. Plot the graph on the map
        nc = nx.draw_networkx_nodes(self.G, pos, node_size=node_size, node_color=node_color)
        
        nx.draw_networkx_edges(self.G, pos)
        
        if node_color:
            plt.colorbar(nc)