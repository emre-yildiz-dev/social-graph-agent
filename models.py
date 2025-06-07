from typing import Dict, List, Optional, Set, Any, Tuple
from pydantic import BaseModel, Field
import networkx as nx


class NodeData(BaseModel):
    """Data structure for a node in the social graph."""
    node_id: str
    name: Optional[str] = None
    attributes: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True


class EdgeData(BaseModel):
    """Data structure for an edge in the social graph."""
    source: str
    target: str
    weight: Optional[float] = 1.0
    relationship_type: Optional[str] = None
    attributes: Dict[str, Any] = Field(default_factory=dict)


class GraphAnalysisRequest(BaseModel):
    """Request for graph analysis operations."""
    operation: str = Field(..., description="The type of analysis to perform")
    parameters: Dict[str, Any] = Field(default_factory=dict)
    target_nodes: Optional[List[str]] = None


class GraphAnalysisResult(BaseModel):
    """Result of a graph analysis operation."""
    operation: str
    result: Any
    metrics: Optional[Dict[str, float]] = None
    description: str = ""


class AgentState(BaseModel):
    """State for the LangGraph social network analysis agent."""
    
    # Graph data
    graph: Optional[Any] = Field(default=None, description="NetworkX graph object")
    nodes: List[NodeData] = Field(default_factory=list)
    edges: List[EdgeData] = Field(default_factory=list)
    
    # Analysis requests and results
    analysis_request: Optional[GraphAnalysisRequest] = None
    analysis_results: List[GraphAnalysisResult] = Field(default_factory=list)
    
    # LLM interaction
    user_query: str = ""
    llm_response: str = ""
    
    # Analysis context
    current_metrics: Dict[str, float] = Field(default_factory=dict)
    insights: List[str] = Field(default_factory=list)
    
    # Control flow
    next_action: Optional[str] = None
    error_message: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True


class GraphMetrics(BaseModel):
    """Comprehensive metrics for social graph analysis."""
    
    # Basic metrics
    num_nodes: int
    num_edges: int
    density: float
    
    # Centrality metrics
    degree_centrality: Dict[str, float] = Field(default_factory=dict)
    betweenness_centrality: Dict[str, float] = Field(default_factory=dict)
    closeness_centrality: Dict[str, float] = Field(default_factory=dict)
    eigenvector_centrality: Dict[str, float] = Field(default_factory=dict)
    
    # Community metrics
    clustering_coefficient: float
    average_clustering: float
    
    # Path metrics
    average_shortest_path_length: Optional[float] = None
    diameter: Optional[int] = None
    
    # Component analysis
    num_connected_components: int
    largest_component_size: int
    
    def to_summary_dict(self) -> Dict[str, Any]:
        """Convert to a summary dictionary for LLM consumption."""
        return {
            "basic_stats": {
                "nodes": self.num_nodes,
                "edges": self.num_edges,
                "density": round(self.density, 4)
            },
            "connectivity": {
                "clustering_coefficient": round(self.clustering_coefficient, 4),
                "connected_components": self.num_connected_components,
                "largest_component_size": self.largest_component_size
            },
            "centrality_leaders": {
                "degree": self._top_k_dict(self.degree_centrality, 5),
                "betweenness": self._top_k_dict(self.betweenness_centrality, 5),
                "closeness": self._top_k_dict(self.closeness_centrality, 5),
                "eigenvector": self._top_k_dict(self.eigenvector_centrality, 5)
            }
        }
    
    def _top_k_dict(self, d: Dict[str, float], k: int) -> Dict[str, float]:
        """Get top k items from dictionary by value."""
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]) 