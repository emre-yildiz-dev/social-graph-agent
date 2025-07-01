from typing import Dict, List, Optional, Any, TypedDict
from langgraph.graph import StateGraph, END
from models import GraphAnalysisRequest, GraphAnalysisResult
from graph_tools import SocialGraphAnalyzer
from llm_client import OllamaClient
import json


class GraphAgentState(TypedDict):
    """State for the LangGraph social network analysis agent."""
    user_query: str
    graph: Optional[Any]
    analysis_results: List[GraphAnalysisResult]
    current_metrics: Dict[str, float]
    insights: List[str]
    error_message: Optional[str]
    llm_response: str
    analysis_request: Optional[GraphAnalysisRequest]
    next_action: Optional[str]
    nodes: List[Any]
    edges: List[Any]


class SocialGraphAgent:
    """LangGraph agent for social network analysis using NetworkX and Ollama."""
    
    def __init__(self, model_name: str = "gemma3n:latest"):
        """Initialize the social graph analysis agent."""
        self.analyzer = SocialGraphAnalyzer()
        self.llm_client = OllamaClient(model_name)
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow for social network analysis."""
        
        workflow = StateGraph(GraphAgentState)
        
        # Define nodes
        workflow.add_node("initialize", self._initialize_analysis)
        workflow.add_node("determine_analysis", self._determine_analysis_type)
        workflow.add_node("load_graph", self._load_graph_data)
        workflow.add_node("basic_metrics", self._calculate_basic_metrics)
        workflow.add_node("centrality_analysis", self._analyze_centrality)
        workflow.add_node("community_detection", self._detect_communities)
        workflow.add_node("path_analysis", self._analyze_paths)
        workflow.add_node("robustness_analysis", self._analyze_robustness)
        workflow.add_node("neighborhood_analysis", self._analyze_neighborhood)
        workflow.add_node("generate_insights", self._generate_insights)
        workflow.add_node("error_handler", self._handle_error)
        
        # Define edges
        workflow.set_entry_point("initialize")
        
        workflow.add_edge("initialize", "determine_analysis")
        workflow.add_edge("determine_analysis", "load_graph")
        
        # Conditional routing based on analysis type
        workflow.add_conditional_edges(
            "load_graph",
            self._route_analysis,
            {
                "basic_metrics": "basic_metrics",
                "centrality": "centrality_analysis",
                "community_detection": "community_detection",
                "path_analysis": "path_analysis",
                "robustness": "robustness_analysis",
                "neighborhood": "neighborhood_analysis",
                "error": "error_handler"
            }
        )
        
        # All analysis nodes go to insights generation
        workflow.add_edge("basic_metrics", "generate_insights")
        workflow.add_edge("centrality_analysis", "generate_insights")
        workflow.add_edge("community_detection", "generate_insights")
        workflow.add_edge("path_analysis", "generate_insights")
        workflow.add_edge("robustness_analysis", "generate_insights")
        workflow.add_edge("neighborhood_analysis", "generate_insights")
        
        # End points
        workflow.add_edge("generate_insights", END)
        workflow.add_edge("error_handler", END)
        
        return workflow.compile()
    
    def _initialize_analysis(self, state: GraphAgentState) -> GraphAgentState:
        """Initialize the analysis process."""
        state["analysis_results"] = []
        state["current_metrics"] = {}
        state["insights"] = []
        state["error_message"] = None
        return state
    
    def _determine_analysis_type(self, state: GraphAgentState) -> GraphAgentState:
        """Determine what type of analysis to perform based on user query."""
        try:
            analysis_decision = self.llm_client.determine_analysis_approach(state["user_query"])
            
            state["analysis_request"] = GraphAnalysisRequest(
                operation=analysis_decision.get("analysis_type", "basic_metrics"),
                parameters=analysis_decision.get("parameters", {}),
                target_nodes=analysis_decision.get("parameters", {}).get("target_nodes")
            )
            
            state["next_action"] = analysis_decision.get("analysis_type", "basic_metrics")
            
        except Exception as e:
            state["error_message"] = f"Error determining analysis type: {str(e)}"
            state["next_action"] = "error"
        
        return state
    
    def _load_graph_data(self, state: GraphAgentState) -> GraphAgentState:
        """Load or create graph data for analysis."""
        try:
            if state["graph"] is None:
                # Create sample graph if no graph provided
                self.analyzer.create_sample_social_graph(num_nodes=25, connection_prob=0.15)
                state["graph"] = self.analyzer.graph
            else:
                # Use provided graph
                self.analyzer.graph = state["graph"]
                
        except Exception as e:
            state["error_message"] = f"Error loading graph data: {str(e)}"
            state["next_action"] = "error"
        
        return state
    
    def _route_analysis(self, state: GraphAgentState) -> str:
        """Route to appropriate analysis based on the determined analysis type."""
        if state.get("error_message"):
            return "error"
        
        analysis_request = state.get("analysis_request")
        analysis_type = analysis_request.operation if analysis_request else "basic_metrics"
        
        # Map analysis types to node names
        routing_map = {
            "basic_metrics": "basic_metrics",
            "centrality": "centrality",
            "community_detection": "community_detection",
            "path_analysis": "path_analysis",
            "robustness": "robustness",
            "neighborhood": "neighborhood"
        }
        
        return routing_map.get(analysis_type, "basic_metrics")
    
    def _calculate_basic_metrics(self, state: GraphAgentState) -> GraphAgentState:
        """Calculate comprehensive network metrics."""
        try:
            metrics = self.analyzer.calculate_comprehensive_metrics()
            
            result = GraphAnalysisResult(
                operation="basic_metrics",
                result=metrics.to_summary_dict(),
                metrics=metrics.to_summary_dict()["basic_stats"],
                description="Comprehensive network metrics analysis"
            )
            
            state["analysis_results"].append(result)
            state["current_metrics"].update(metrics.to_summary_dict()["basic_stats"])
            
        except Exception as e:
            state["error_message"] = f"Error calculating basic metrics: {str(e)}"
        
        return state
    
    def _analyze_centrality(self, state: GraphAgentState) -> GraphAgentState:
        """Analyze node centrality and influence."""
        try:
            analysis_request = state.get("analysis_request")
            top_k = analysis_request.parameters.get("top_k", 5) if analysis_request else 5
            influential_nodes = self.analyzer.find_influential_nodes(top_k=top_k)
            
            result = GraphAnalysisResult(
                operation="centrality",
                result=influential_nodes,
                description=f"Top {top_k} influential nodes by different centrality measures"
            )
            
            state["analysis_results"].append(result)
            
        except Exception as e:
            state["error_message"] = f"Error analyzing centrality: {str(e)}"
        
        return state
    
    def _detect_communities(self, state: GraphAgentState) -> GraphAgentState:
        """Detect communities in the social network."""
        try:
            analysis_request = state.get("analysis_request")
            method = analysis_request.parameters.get("method", "greedy_modularity") if analysis_request else "greedy_modularity"
            communities = self.analyzer.detect_communities(method=method)
            
            # Convert sets to lists for serialization
            communities_data = [list(community) for community in communities]
            
            result = GraphAnalysisResult(
                operation="community_detection",
                result={
                    "communities": communities_data,
                    "num_communities": len(communities),
                    "community_sizes": [len(c) for c in communities]
                },
                description=f"Community detection using {method} method"
            )
            
            state["analysis_results"].append(result)
            
        except Exception as e:
            state["error_message"] = f"Error detecting communities: {str(e)}"
        
        return state
    
    def _analyze_paths(self, state: GraphAgentState) -> GraphAgentState:
        """Analyze shortest paths in the network."""
        try:
            analysis_request = state.get("analysis_request")
            params = analysis_request.parameters if analysis_request else {}
            source = params.get("source")
            target = params.get("target")
            
            if not source:
                # If no source specified, use a random node
                source = list(self.analyzer.graph.nodes())[0]
            
            path_results = self.analyzer.find_shortest_paths(source, target)
            
            result = GraphAnalysisResult(
                operation="path_analysis",
                result=path_results,
                description=f"Shortest path analysis from {source}"
            )
            
            state["analysis_results"].append(result)
            
        except Exception as e:
            state["error_message"] = f"Error analyzing paths: {str(e)}"
        
        return state
    
    def _analyze_robustness(self, state: GraphAgentState) -> GraphAgentState:
        """Analyze network robustness."""
        try:
            analysis_request = state.get("analysis_request")
            num_removals = analysis_request.parameters.get("num_removals", 5) if analysis_request else 5
            robustness_results = self.analyzer.analyze_graph_robustness(num_removals=num_removals)
            
            result = GraphAnalysisResult(
                operation="robustness",
                result=robustness_results,
                description=f"Network robustness analysis with {num_removals} node removals"
            )
            
            state["analysis_results"].append(result)
            
        except Exception as e:
            state["error_message"] = f"Error analyzing robustness: {str(e)}"
        
        return state
    
    def _analyze_neighborhood(self, state: GraphAgentState) -> GraphAgentState:
        """Analyze node neighborhoods."""
        try:
            analysis_request = state.get("analysis_request")
            params = analysis_request.parameters if analysis_request else {}
            node_id = params.get("node_id")
            radius = params.get("radius", 1)
            
            if not node_id:
                # Use a random node if none specified
                node_id = list(self.analyzer.graph.nodes())[0]
            
            neighborhood_results = self.analyzer.analyze_node_neighborhood(str(node_id), radius)
            
            result = GraphAnalysisResult(
                operation="neighborhood",
                result=neighborhood_results,
                description=f"Neighborhood analysis for node {node_id} with radius {radius}"
            )
            
            state["analysis_results"].append(result)
            
        except Exception as e:
            state["error_message"] = f"Error analyzing neighborhood: {str(e)}"
        
        return state
    
    def _generate_insights(self, state: GraphAgentState) -> GraphAgentState:
        """Generate natural language insights using LLM."""
        try:
            if not state.get("analysis_results"):
                state["llm_response"] = "No analysis results available to generate insights."
                return state
            
            # Combine all analysis results
            combined_results = {}
            for result in state["analysis_results"]:
                combined_results[result.operation] = result.result
            
            # Generate insights based on analysis type
            analysis_request = state.get("analysis_request")
            analysis_type = analysis_request.operation if analysis_request else "basic_metrics"
            
            if analysis_type == "centrality":
                state["llm_response"] = self.llm_client.explain_centrality_results(
                    combined_results.get("centrality", {}), 
                    state["user_query"]
                )
            elif analysis_type == "community_detection":
                communities = combined_results.get("community_detection", {}).get("communities", [])
                state["llm_response"] = self.llm_client.analyze_communities(
                    [set(c) for c in communities], 
                    combined_results, 
                    state["user_query"]
                )
            elif analysis_type == "robustness":
                state["llm_response"] = self.llm_client.interpret_robustness_analysis(
                    combined_results.get("robustness", {}), 
                    state["user_query"]
                )
            else:
                # General analysis for other types
                state["llm_response"] = self.llm_client.general_graph_analysis(
                    combined_results, 
                    state["user_query"]
                )
            
        except Exception as e:
            state["error_message"] = f"Error generating insights: {str(e)}"
            state["llm_response"] = f"Unable to generate insights due to error: {str(e)}"
        
        return state
    
    def _handle_error(self, state: GraphAgentState) -> GraphAgentState:
        """Handle errors that occurred during analysis."""
        error_msg = state.get("error_message") or "Unknown error occurred"
        state["llm_response"] = f"Analysis failed: {error_msg}"
        return state
    
    def analyze_social_network(self, user_query: str, graph_data: Optional[Any] = None) -> Dict[str, Any]:
        """Main method to analyze a social network based on user query."""
        
        # Initialize state
        initial_state = {
            "user_query": user_query,
            "graph": graph_data,
            "analysis_results": [],
            "current_metrics": {},
            "insights": [],
            "error_message": None,
            "llm_response": "",
            "analysis_request": None,
            "next_action": None,
            "nodes": [],
            "edges": []
        }
        
        # Run the workflow
        final_state = self.graph.invoke(initial_state)
        
        # Return results
        return {
            "user_query": final_state.get("user_query", ""),
            "analysis_results": [result.dict() if hasattr(result, 'dict') else result for result in final_state.get("analysis_results", [])],
            "insights": final_state.get("llm_response", ""),
            "metrics": final_state.get("current_metrics", {}),
            "error": final_state.get("error_message")
        }


# Example usage and testing
if __name__ == "__main__":
    # Create agent
    agent = SocialGraphAgent()
    
    # Test with sample queries
    test_queries = [
        "Who are the most influential people in this network?",
        "What communities exist in this social network?",
        "How robust is this network to key people leaving?",
        "What are the basic statistics of this network?"
    ]
    
    for query in test_queries:
        print(f"\n{'='*50}")
        print(f"Query: {query}")
        print(f"{'='*50}")
        
        result = agent.analyze_social_network(query)
        
        if result["error"]:
            print(f"Error: {result['error']}")
        else:
            print(f"Analysis: {result['analysis_results']}")
            print(f"Insights: {result['insights']}") 