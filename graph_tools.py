from typing import Dict, List, Optional, Tuple, Any, Set
import networkx as nx
import numpy as np
from models import GraphMetrics, NodeData, EdgeData, GraphAnalysisResult
import warnings


class SocialGraphAnalyzer:
    """Comprehensive social graph analysis tools using NetworkX."""
    
    def __init__(self, graph: Optional[nx.Graph] = None):
        """Initialize with an optional NetworkX graph."""
        self.graph = graph or nx.Graph()
    
    def load_graph_from_data(self, nodes: List[NodeData], edges: List[EdgeData]) -> nx.Graph:
        """Load graph from structured node and edge data."""
        self.graph = nx.Graph()
        
        # Add nodes with attributes
        for node in nodes:
            self.graph.add_node(
                node.node_id,
                name=node.name,
                **node.attributes
            )
        
        # Add edges with attributes
        for edge in edges:
            self.graph.add_edge(
                edge.source,
                edge.target,
                weight=edge.weight,
                relationship_type=edge.relationship_type,
                **edge.attributes
            )
        
        return self.graph
    
    def create_sample_social_graph(self, num_nodes: int = 20, connection_prob: float = 0.15) -> nx.Graph:
        """Create a sample social network for testing."""
        # Create a random graph with some structure
        temp_graph = nx.erdos_renyi_graph(num_nodes, connection_prob)
        
        # Create new graph with string node IDs
        self.graph = nx.Graph()
        
        # Add nodes with string IDs and realistic attributes
        names = [f"Person_{i}" for i in range(num_nodes)]
        ages = np.random.randint(18, 65, num_nodes)
        locations = np.random.choice(['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix'], num_nodes)
        
        # Create mapping from integer to string node IDs
        node_mapping = {i: f"person_{i}" for i in range(num_nodes)}
        
        # Add nodes with string IDs
        for i in range(num_nodes):
            node_id = node_mapping[i]
            self.graph.add_node(node_id, **{
                'name': names[i],
                'age': int(ages[i]),
                'location': locations[i]
            })
        
        # Add edges with string node IDs
        for edge in temp_graph.edges():
            source = node_mapping[edge[0]]
            target = node_mapping[edge[1]]
            self.graph.add_edge(source, target, **{
                'weight': np.random.uniform(0.1, 1.0),
                'relationship_type': np.random.choice([
                    'friend', 'colleague', 'family', 'acquaintance'
                ])
            })
        
        return self.graph
    
    def calculate_comprehensive_metrics(self) -> GraphMetrics:
        """Calculate comprehensive social network metrics."""
        if not self.graph:
            raise ValueError("No graph loaded")
        
        # Basic metrics
        num_nodes = self.graph.number_of_nodes()
        num_edges = self.graph.number_of_edges()
        density = nx.density(self.graph)
        
        # Centrality metrics
        degree_centrality = nx.degree_centrality(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        closeness_centrality = nx.closeness_centrality(self.graph)
        
        # Handle eigenvector centrality carefully
        try:
            eigenvector_centrality = nx.eigenvector_centrality(self.graph, max_iter=1000)
        except nx.PowerIterationFailedConvergence:
            warnings.warn("Eigenvector centrality did not converge, using zeros")
            eigenvector_centrality = {node: 0.0 for node in self.graph.nodes()}
        
        # Clustering metrics
        clustering_coefficient = nx.transitivity(self.graph)
        average_clustering = nx.average_clustering(self.graph)
        
        # Path metrics (only for connected graphs)
        average_shortest_path_length = None
        diameter = None
        if nx.is_connected(self.graph):
            average_shortest_path_length = nx.average_shortest_path_length(self.graph)
            diameter = nx.diameter(self.graph)
        
        # Component analysis
        connected_components = list(nx.connected_components(self.graph))
        num_connected_components = len(connected_components)
        largest_component_size = len(max(connected_components, key=len)) if connected_components else 0
        
        return GraphMetrics(
            num_nodes=num_nodes,
            num_edges=num_edges,
            density=density,
            degree_centrality=degree_centrality,
            betweenness_centrality=betweenness_centrality,
            closeness_centrality=closeness_centrality,
            eigenvector_centrality=eigenvector_centrality,
            clustering_coefficient=clustering_coefficient,
            average_clustering=average_clustering,
            average_shortest_path_length=average_shortest_path_length,
            diameter=diameter,
            num_connected_components=num_connected_components,
            largest_component_size=largest_component_size
        )
    
    def find_influential_nodes(self, top_k: int = 5) -> Dict[str, List[Tuple[str, float]]]:
        """Find the most influential nodes by different centrality measures."""
        metrics = self.calculate_comprehensive_metrics()
        
        return {
            'degree': sorted(metrics.degree_centrality.items(), key=lambda x: x[1], reverse=True)[:top_k],
            'betweenness': sorted(metrics.betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:top_k],
            'closeness': sorted(metrics.closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:top_k],
            'eigenvector': sorted(metrics.eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:top_k]
        }
    
    def detect_communities(self, method: str = 'louvain') -> List[Set[str]]:
        """Detect communities in the social network."""
        if method == 'louvain':
            try:
                import community as community_louvain
                partition = community_louvain.best_partition(self.graph)
                communities = {}
                for node, comm_id in partition.items():
                    if comm_id not in communities:
                        communities[comm_id] = set()
                    communities[comm_id].add(node)
                return list(communities.values())
            except ImportError:
                # Fallback to greedy modularity communities
                return self._greedy_modularity_communities()
        
        elif method == 'greedy_modularity':
            return self._greedy_modularity_communities()
        
        else:
            raise ValueError(f"Unknown community detection method: {method}")
    
    def _greedy_modularity_communities(self) -> List[Set[str]]:
        """Fallback community detection using greedy modularity."""
        communities = nx.algorithms.community.greedy_modularity_communities(self.graph)
        return [set(community) for community in communities]
    
    def analyze_node_neighborhood(self, node_id: str, radius: int = 1) -> Dict[str, Any]:
        """Analyze the neighborhood of a specific node."""
        if node_id not in self.graph:
            raise ValueError(f"Node {node_id} not found in graph")
        
        # Get neighbors within radius
        neighbors = set()
        current_level = {node_id}
        
        for _ in range(radius):
            next_level = set()
            for node in current_level:
                next_level.update(self.graph.neighbors(node))
            neighbors.update(next_level)
            current_level = next_level - neighbors
        
        neighbors.discard(node_id)  # Remove the center node itself
        
        # Create subgraph
        subgraph = self.graph.subgraph([node_id] + list(neighbors))
        
        # Calculate local metrics
        local_density = nx.density(subgraph)
        local_clustering = nx.clustering(self.graph, node_id)
        degree = self.graph.degree(node_id)
        
        return {
            'node_id': node_id,
            'neighbors': list(neighbors),
            'neighborhood_size': len(neighbors),
            'degree': degree,
            'local_clustering': local_clustering,
            'local_density': local_density,
            'subgraph_edges': subgraph.number_of_edges()
        }
    
    def find_shortest_paths(self, source: str, target: Optional[str] = None) -> Dict[str, Any]:
        """Find shortest paths from source to target or all nodes."""
        if source not in self.graph:
            raise ValueError(f"Source node {source} not found in graph")
        
        if target:
            if target not in self.graph:
                raise ValueError(f"Target node {target} not found in graph")
            
            try:
                path = nx.shortest_path(self.graph, source, target)
                length = nx.shortest_path_length(self.graph, source, target)
                return {
                    'source': source,
                    'target': target,
                    'path': path,
                    'length': length
                }
            except nx.NetworkXNoPath:
                return {
                    'source': source,
                    'target': target,
                    'path': None,
                    'length': float('inf'),
                    'error': 'No path exists'
                }
        else:
            # All shortest paths from source
            paths = nx.single_source_shortest_path(self.graph, source)
            lengths = nx.single_source_shortest_path_length(self.graph, source)
            
            return {
                'source': source,
                'paths': paths,
                'lengths': lengths,
                'reachable_nodes': len(paths)
            }
    
    def analyze_graph_robustness(self, num_removals: int = 5) -> Dict[str, Any]:
        """Analyze network robustness by simulating node removals."""
        original_metrics = self.calculate_comprehensive_metrics()
        
        # Get most central nodes
        central_nodes = sorted(
            original_metrics.betweenness_centrality.items(),
            key=lambda x: x[1],
            reverse=True
        )[:num_removals]
        
        robustness_results = []
        
        for node_id, centrality in central_nodes:
            # Create copy and remove node
            temp_graph = self.graph.copy()
            temp_graph.remove_node(node_id)
            
            # Calculate new metrics
            analyzer = SocialGraphAnalyzer(temp_graph)
            new_metrics = analyzer.calculate_comprehensive_metrics()
            
            robustness_results.append({
                'removed_node': node_id,
                'original_centrality': centrality,
                'connectivity_change': {
                    'components_before': original_metrics.num_connected_components,
                    'components_after': new_metrics.num_connected_components,
                    'largest_component_before': original_metrics.largest_component_size,
                    'largest_component_after': new_metrics.largest_component_size
                }
            })
        
        return {
            'original_connectivity': {
                'components': original_metrics.num_connected_components,
                'largest_component': original_metrics.largest_component_size
            },
            'removal_results': robustness_results
        } 