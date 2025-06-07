#!/usr/bin/env python3
"""
Example usage of the Social Graph Analysis Agent using LangGraph, NetworkX, and Ollama.

This script demonstrates how to:
1. Create and use the social graph agent
2. Analyze different types of social networks
3. Ask various types of questions about social graphs
4. Load custom graph data
"""

import networkx as nx
from social_graph_agent import SocialGraphAgent
from models import NodeData, EdgeData
from graph_tools import SocialGraphAnalyzer
import json


def create_custom_social_network():
    """Create a custom social network for demonstration."""
    
    # Define nodes (people)
    nodes = [
        NodeData(node_id="alice", name="Alice Johnson", attributes={"age": 28, "department": "Engineering", "location": "NYC"}),
        NodeData(node_id="bob", name="Bob Smith", attributes={"age": 32, "department": "Marketing", "location": "LA"}),
        NodeData(node_id="charlie", name="Charlie Brown", attributes={"age": 25, "department": "Engineering", "location": "NYC"}),
        NodeData(node_id="diana", name="Diana Wilson", attributes={"age": 30, "department": "Sales", "location": "Chicago"}),
        NodeData(node_id="eve", name="Eve Davis", attributes={"age": 27, "department": "Engineering", "location": "NYC"}),
        NodeData(node_id="frank", name="Frank Miller", attributes={"age": 35, "department": "Management", "location": "NYC"}),
        NodeData(node_id="grace", name="Grace Lee", attributes={"age": 29, "department": "Marketing", "location": "LA"}),
        NodeData(node_id="henry", name="Henry Taylor", attributes={"age": 31, "department": "Sales", "location": "Chicago"}),
    ]
    
    # Define edges (relationships)
    edges = [
        EdgeData(source="alice", target="charlie", weight=0.9, relationship_type="colleague"),
        EdgeData(source="alice", target="eve", weight=0.8, relationship_type="colleague"),
        EdgeData(source="alice", target="frank", weight=0.6, relationship_type="reports_to"),
        EdgeData(source="bob", target="grace", weight=0.7, relationship_type="colleague"),
        EdgeData(source="bob", target="diana", weight=0.5, relationship_type="cross_department"),
        EdgeData(source="charlie", target="eve", weight=0.9, relationship_type="colleague"),
        EdgeData(source="charlie", target="frank", weight=0.4, relationship_type="reports_to"),
        EdgeData(source="diana", target="henry", weight=0.8, relationship_type="colleague"),
        EdgeData(source="eve", target="frank", weight=0.5, relationship_type="reports_to"),
        EdgeData(source="frank", target="grace", weight=0.3, relationship_type="cross_department"),
        EdgeData(source="grace", target="henry", weight=0.4, relationship_type="cross_department"),
    ]
    
    # Create and load graph
    analyzer = SocialGraphAnalyzer()
    graph = analyzer.load_graph_from_data(nodes, edges)
    
    return graph


def run_example_queries():
    """Run example queries to demonstrate the agent capabilities."""
    
    print("🚀 Initializing Social Graph Analysis Agent...")
    agent = SocialGraphAgent()
    
    # Test Ollama connection
    print("🔗 Testing Ollama connection...")
    if not agent.llm_client.test_connection():
        print("⚠️  Warning: Ollama connection failed. Make sure Ollama is running with gemma2:27b model.")
        print("   You can start Ollama and pull the model with:")
        print("   ollama serve")
        print("   ollama pull gemma3:27b")
    else:
        print("✅ Ollama connection successful!")
    
    print("\n" + "="*60)
    print("DEMO 1: Analysis with Sample Network")
    print("="*60)
    
    # Example queries with generated sample network
    sample_queries = [
        "Who are the most influential people in this network?",
        "What communities or groups exist in this social network?",
        "How well-connected is this network overall?",
        "Which person would cause the most disruption if they left the network?",
    ]
    
    for i, query in enumerate(sample_queries, 1):
        print(f"\n📊 Query {i}: {query}")
        print("-" * 50)
        
        try:
            result = agent.analyze_social_network(query)
            
            if result["error"]:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"📈 Analysis Type: {result['analysis_results'][0]['operation'] if result['analysis_results'] else 'None'}")
                print(f"🤖 AI Insights:\n{result['insights']}")
                
                if result['metrics']:
                    print(f"📊 Key Metrics: {result['metrics']}")
                    
        except Exception as e:
            print(f"❌ Error running query: {str(e)}")
    
    print("\n" + "="*60)
    print("DEMO 2: Analysis with Custom Network")
    print("="*60)
    
    # Create custom network
    print("🏗️  Creating custom organizational network...")
    custom_graph = create_custom_social_network()
    
    custom_queries = [
        "Who has the most influence in this organization?",
        "What departments or groups can you identify?",
        "How would losing Frank affect the organization?",
        "Who are the key connectors between different groups?",
    ]
    
    for i, query in enumerate(custom_queries, 1):
        print(f"\n📊 Query {i}: {query}")
        print("-" * 50)
        
        try:
            result = agent.analyze_social_network(query, graph_data=custom_graph)
            
            if result["error"]:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"📈 Analysis Type: {result['analysis_results'][0]['operation'] if result['analysis_results'] else 'None'}")
                print(f"🤖 AI Insights:\n{result['insights']}")
                
        except Exception as e:
            print(f"❌ Error running query: {str(e)}")
    
    print("\n" + "="*60)
    print("DEMO 3: Specific Analysis Types")
    print("="*60)
    
    # Demonstrate specific analysis types
    specific_queries = [
        "Analyze the robustness of this network",
        "Find the shortest path between any two people",
        "Show me the neighborhood analysis for a central person",
    ]
    
    for i, query in enumerate(specific_queries, 1):
        print(f"\n📊 Specific Analysis {i}: {query}")
        print("-" * 50)
        
        try:
            result = agent.analyze_social_network(query, graph_data=custom_graph)
            
            if result["error"]:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"📈 Analysis Type: {result['analysis_results'][0]['operation'] if result['analysis_results'] else 'None'}")
                print(f"🤖 AI Insights:\n{result['insights']}")
                
        except Exception as e:
            print(f"❌ Error running query: {str(e)}")


def demonstrate_graph_metrics():
    """Demonstrate detailed graph metrics calculation."""
    
    print("\n" + "="*60)
    print("DETAILED METRICS DEMONSTRATION")
    print("="*60)
    
    # Create a larger sample network
    analyzer = SocialGraphAnalyzer()
    graph = analyzer.create_sample_social_graph(num_nodes=30, connection_prob=0.12)
    
    print(f"📊 Generated network with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
    
    # Calculate comprehensive metrics
    print("\n🔢 Calculating comprehensive metrics...")
    metrics = analyzer.calculate_comprehensive_metrics()
    
    print(f"""
📈 NETWORK OVERVIEW:
   • Nodes: {metrics.num_nodes}
   • Edges: {metrics.num_edges}
   • Density: {metrics.density:.4f}
   • Connected Components: {metrics.num_connected_components}
   • Largest Component: {metrics.largest_component_size}
   • Clustering Coefficient: {metrics.clustering_coefficient:.4f}
   
🎯 TOP 3 MOST CENTRAL NODES:
   • Degree: {list(metrics.degree_centrality.items())[:3]}
   • Betweenness: {sorted(metrics.betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]}
   • Closeness: {sorted(metrics.closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]}
    """)
    
    # Community detection
    print("🏘️  Detecting communities...")
    communities = analyzer.detect_communities()
    print(f"   Found {len(communities)} communities")
    print(f"   Community sizes: {[len(c) for c in communities]}")
    
    # Robustness analysis
    print("\n🛡️  Analyzing network robustness...")
    robustness = analyzer.analyze_graph_robustness(num_removals=3)
    print(f"   Original connectivity: {robustness['original_connectivity']}")
    print(f"   Critical nodes identified: {len(robustness['removal_results'])}")


if __name__ == "__main__":
    print("🎯 Social Graph Analysis Agent - Example Usage")
    print("=" * 60)
    
    try:
        # Run the main demonstrations
        run_example_queries()
        
        # Show detailed metrics
        demonstrate_graph_metrics()
        
        print("\n🎉 Demo completed successfully!")
        print("\n💡 Tips for using the agent:")
        print("   • Ask natural language questions about your social network")
        print("   • The agent automatically determines the best analysis approach")
        print("   • You can provide custom graph data or use generated samples")
        print("   • Make sure Ollama is running with the gemma2:27b model for best results")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Demo failed with error: {str(e)}")
        print("   Please check your dependencies and Ollama setup.") 