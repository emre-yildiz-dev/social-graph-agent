#!/usr/bin/env python3
"""
Interactive Question-Answer Script for Social Graph Analysis Agent

This script provides an interactive command-line interface where users can:
1. Ask natural language questions about social networks
2. Get real-time analysis and insights
3. Choose between sample networks or load custom data
4. Continue asking questions in a conversational manner
"""

import sys
import json
import os
from typing import Optional, Any
import networkx as nx
from social_graph_agent import SocialGraphAgent
from models import NodeData, EdgeData
from graph_tools import SocialGraphAnalyzer
from real_world_analysis import RealWorldGraphAnalyzer


class InteractiveQA:
    """Interactive Question-Answer interface for the Social Graph Agent."""
    
    def __init__(self):
        """Initialize the interactive Q&A system."""
        self.agent = None
        self.current_graph = None
        self.graph_type = None
        
    def print_banner(self):
        """Print welcome banner."""
        print("🤖 " + "="*60)
        print("     SOCIAL GRAPH ANALYSIS - INTERACTIVE Q&A")
        print("="*63)
        print("Ask natural language questions about social networks!")
        print("Type 'help' for commands, 'quit' or 'exit' to leave.")
        print("="*63)
    
    def print_help(self):
        """Print help information."""
        print("\n📚 HELP - Available Commands:")
        print("-" * 40)
        print("🔤 QUESTIONS: Ask any natural language question about the network")
        print("   Examples:")
        print("   • 'Who are the most influential people?'")
        print("   • 'What communities exist in this network?'")
        print("   • 'How robust is this network?'")
        print("   • 'Show me the shortest path between two people'")
        print("\n⚙️  COMMANDS:")
        print("   • help        - Show this help message")
        print("   • status      - Show current network status")
        print("   • sample      - Load a new sample network")
        print("   • custom      - Load custom network (organizational demo)")
        print("   • dataset     - Load real-world dataset from file")
        print("   • facebook    - Load Facebook social circles dataset")
        print("   • email       - Load European email network dataset") 
        print("   • metrics     - Show detailed network metrics")
        print("   • clear       - Clear screen")
        print("   • quit/exit   - Exit the program")
        print("-" * 40)
    
    def initialize_agent(self):
        """Initialize the social graph agent."""
        print("🚀 Initializing Social Graph Analysis Agent...")
        
        try:
            self.agent = SocialGraphAgent()
            print("✅ Agent initialized successfully!")
            
            # Test Ollama connection
            print("🔗 Testing Ollama connection...")
            if not self.agent.llm_client.test_connection():
                print("⚠️  Warning: Ollama connection failed.")
                print("   Make sure Ollama is running with the gemma3:27b model:")
                print("   > ollama serve")
                print("   > ollama pull gemma3:27b")
                print("   The agent will still work but with limited AI insights.")
            else:
                print("✅ Ollama connection successful!")
                
            return True
            
        except Exception as e:
            print(f"❌ Error initializing agent: {str(e)}")
            return False
    
    def load_sample_network(self):
        """Load a sample social network."""
        try:
            print("🏗️  Generating sample social network...")
            analyzer = SocialGraphAnalyzer()
            self.current_graph = analyzer.create_sample_social_graph(num_nodes=25, connection_prob=0.15)
            self.graph_type = "sample"
            
            print(f"✅ Sample network loaded!")
            print(f"   📊 {self.current_graph.number_of_nodes()} nodes, {self.current_graph.number_of_edges()} edges")
            
        except Exception as e:
            print(f"❌ Error loading sample network: {str(e)}")
    
    def load_custom_network(self):
        """Load a custom organizational network."""
        try:
            print("🏗️  Creating custom organizational network...")
            
            # Define nodes (people in organization)
            nodes = [
                NodeData(node_id="alice", name="Alice Johnson", attributes={"role": "Senior Engineer", "department": "Engineering"}),
                NodeData(node_id="bob", name="Bob Smith", attributes={"role": "Marketing Manager", "department": "Marketing"}),
                NodeData(node_id="charlie", name="Charlie Brown", attributes={"role": "Junior Engineer", "department": "Engineering"}),
                NodeData(node_id="diana", name="Diana Wilson", attributes={"role": "Sales Rep", "department": "Sales"}),
                NodeData(node_id="eve", name="Eve Davis", attributes={"role": "Engineer", "department": "Engineering"}),
                NodeData(node_id="frank", name="Frank Miller", attributes={"role": "Engineering Manager", "department": "Management"}),
                NodeData(node_id="grace", name="Grace Lee", attributes={"role": "Marketing Specialist", "department": "Marketing"}),
                NodeData(node_id="henry", name="Henry Taylor", attributes={"role": "Sales Manager", "department": "Sales"}),
                NodeData(node_id="ivy", name="Ivy Chen", attributes={"role": "Product Manager", "department": "Product"}),
                NodeData(node_id="jack", name="Jack Wilson", attributes={"role": "CEO", "department": "Executive"}),
            ]
            
            # Define edges (relationships)
            edges = [
                EdgeData(source="alice", target="charlie", weight=0.9, relationship_type="mentor"),
                EdgeData(source="alice", target="eve", weight=0.8, relationship_type="colleague"),
                EdgeData(source="alice", target="frank", weight=0.7, relationship_type="reports_to"),
                EdgeData(source="bob", target="grace", weight=0.9, relationship_type="manager"),
                EdgeData(source="bob", target="ivy", weight=0.6, relationship_type="collaboration"),
                EdgeData(source="charlie", target="eve", weight=0.8, relationship_type="colleague"),
                EdgeData(source="diana", target="henry", weight=0.7, relationship_type="reports_to"),
                EdgeData(source="frank", target="jack", weight=0.8, relationship_type="reports_to"),
                EdgeData(source="henry", target="jack", weight=0.7, relationship_type="reports_to"),
                EdgeData(source="bob", target="jack", weight=0.6, relationship_type="reports_to"),
                EdgeData(source="ivy", target="jack", weight=0.5, relationship_type="reports_to"),
                EdgeData(source="alice", target="ivy", weight=0.4, relationship_type="cross_functional"),
                EdgeData(source="eve", target="ivy", weight=0.3, relationship_type="cross_functional"),
            ]
            
            # Create and load graph
            analyzer = SocialGraphAnalyzer()
            self.current_graph = analyzer.load_graph_from_data(nodes, edges)
            self.graph_type = "organizational"
            
            print(f"✅ Organizational network loaded!")
            print(f"   📊 {self.current_graph.number_of_nodes()} people, {self.current_graph.number_of_edges()} relationships")
            print("   🏢 Departments: Engineering, Marketing, Sales, Product, Executive")
            
        except Exception as e:
            print(f"❌ Error loading custom network: {str(e)}")
    
    def load_dataset_from_file(self):
        """Load a dataset from a file path."""
        try:
            print("\n📁 Available datasets in 'datasets/' folder:")
            if os.path.exists("datasets"):
                files = [f for f in os.listdir("datasets") if f.endswith(('.txt', '.csv', '.json', '.graphml'))]
                if files:
                    for i, filename in enumerate(files, 1):
                        print(f"   {i}. {filename}")
                    
                    choice = input("\n🔢 Enter file number or filename: ").strip()
                    
                    # Handle numeric choice
                    if choice.isdigit() and 1 <= int(choice) <= len(files):
                        filename = files[int(choice) - 1]
                    else:
                        filename = choice
                    
                    filepath = os.path.join("datasets", filename)
                    if not os.path.exists(filepath):
                        filepath = choice  # Try as direct path
                    
                    if os.path.exists(filepath):
                        self._load_file(filepath, os.path.splitext(filename)[0])
                    else:
                        print(f"❌ File not found: {filepath}")
                else:
                    print("   No dataset files found")
                    filepath = input("🔤 Enter full file path: ").strip()
                    if os.path.exists(filepath):
                        filename = os.path.basename(filepath)
                        self._load_file(filepath, os.path.splitext(filename)[0])
                    else:
                        print(f"❌ File not found: {filepath}")
            else:
                filepath = input("🔤 Enter full file path: ").strip()
                if os.path.exists(filepath):
                    filename = os.path.basename(filepath)
                    self._load_file(filepath, os.path.splitext(filename)[0])
                else:
                    print(f"❌ File not found: {filepath}")
                    
        except Exception as e:
            print(f"❌ Error loading dataset: {str(e)}")
    
    def load_facebook_dataset(self):
        """Load the Facebook social circles dataset."""
        facebook_path = "datasets/facebook_combined.txt"
        if os.path.exists(facebook_path):
            self._load_file(facebook_path, "facebook")
        else:
            print(f"❌ Facebook dataset not found at: {facebook_path}")
            print("   Make sure you've downloaded the dataset first.")
    
    def load_email_dataset(self):
        """Load the European email network dataset."""
        email_path = "datasets/email-Eu-core.txt"
        if os.path.exists(email_path):
            self._load_file(email_path, "email")
        else:
            print(f"❌ Email dataset not found at: {email_path}")
            print("   Make sure you've downloaded the dataset first.")
    
    def _load_file(self, filepath: str, dataset_name: str):
        """Internal method to load a file using RealWorldGraphAnalyzer."""
        try:
            print(f"🏗️  Loading {dataset_name} dataset from: {filepath}")
            
            analyzer = RealWorldGraphAnalyzer()
            
            # Determine delimiter based on file extension and content
            delimiter = " "
            if filepath.endswith('.csv'):
                delimiter = ","
            elif filepath.endswith('.txt'):
                # Check if it's tab-separated by peeking at the file
                with open(filepath, 'r') as f:
                    first_line = f.readline().strip()
                    if '\t' in first_line and ' ' not in first_line.replace('\t', ''):
                        delimiter = "\t"
            
            graph = analyzer.auto_detect_and_load(filepath, delimiter=delimiter)
            
            # Basic preprocessing
            self.current_graph = analyzer.validate_and_preprocess(
                graph, 
                remove_self_loops=True, 
                remove_isolates=False, 
                largest_component_only=False
            )
            
            self.graph_type = f"{dataset_name}_dataset"
            
            print(f"✅ {dataset_name.title()} dataset loaded successfully!")
            print(f"   📊 {self.current_graph.number_of_nodes()} nodes, {self.current_graph.number_of_edges()} edges")
            
            # Show basic info about the dataset
            if hasattr(analyzer, 'graph_info') and analyzer.graph_info:
                info = analyzer.graph_info
                print(f"   📋 Format: {info.get('format', 'Unknown')}")
                print(f"   🔄 Type: {'Directed' if info.get('directed') else 'Undirected'}")
                
        except Exception as e:
            print(f"❌ Error loading {dataset_name} dataset: {str(e)}")
    
    def show_status(self):
        """Show current system status."""
        print("\n📊 CURRENT STATUS:")
        print("-" * 30)
        
        if self.agent:
            print("✅ Agent: Initialized")
            ollama_status = "✅ Connected" if self.agent.llm_client.test_connection() else "❌ Disconnected"
            print(f"🔗 Ollama: {ollama_status}")
        else:
            print("❌ Agent: Not initialized")
        
        if self.current_graph:
            print(f"📈 Network: {self.graph_type} ({self.current_graph.number_of_nodes()} nodes, {self.current_graph.number_of_edges()} edges)")
        else:
            print("📈 Network: None loaded")
        print("-" * 30)
    
    def show_detailed_metrics(self):
        """Show detailed network metrics."""
        if not self.current_graph:
            print("❌ No network loaded. Use 'sample', 'custom', 'facebook', 'email', or 'dataset' to load a network first.")
            return
        
        try:
            print("\n📊 DETAILED NETWORK METRICS:")
            print("=" * 40)
            
            analyzer = SocialGraphAnalyzer()
            analyzer.graph = self.current_graph
            metrics = analyzer.calculate_comprehensive_metrics()
            
            print(f"""
🏗️  BASIC STRUCTURE:
   • Nodes: {metrics.num_nodes}
   • Edges: {metrics.num_edges}
   • Density: {metrics.density:.4f}
   • Average Degree: {(2 * self.current_graph.number_of_edges()) / metrics.num_nodes:.2f}

🔗 CONNECTIVITY:
   • Connected Components: {metrics.num_connected_components}
   • Largest Component: {metrics.largest_component_size}
   • Clustering Coefficient: {metrics.clustering_coefficient:.4f}

🎯 TOP 3 CENTRAL NODES:""")
            
            # Show top nodes by different centrality measures
            degree_top = sorted(metrics.degree_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
            betweenness_top = sorted(metrics.betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
            closeness_top = sorted(metrics.closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
            
            print(f"   • By Degree: {[(node, f'{score:.3f}') for node, score in degree_top]}")
            print(f"   • By Betweenness: {[(node, f'{score:.3f}') for node, score in betweenness_top]}")
            print(f"   • By Closeness: {[(node, f'{score:.3f}') for node, score in closeness_top]}")
            
            # Community detection
            communities = analyzer.detect_communities()
            print(f"\n🏘️  COMMUNITIES:")
            print(f"   • Number of communities: {len(communities)}")
            print(f"   • Community sizes: {[len(c) for c in communities]}")
            
            print("=" * 40)
            
        except Exception as e:
            print(f"❌ Error calculating metrics: {str(e)}")
    
    def process_question(self, question: str) -> bool:
        """Process a user question and return whether to continue."""
        
        # Handle commands
        question_lower = question.lower().strip()
        
        if question_lower in ['quit', 'exit', 'q']:
            return False
        elif question_lower == 'help':
            self.print_help()
            return True
        elif question_lower == 'status':
            self.show_status()
            return True
        elif question_lower == 'sample':
            self.load_sample_network()
            return True
        elif question_lower == 'custom':
            self.load_custom_network()
            return True
        elif question_lower == 'dataset':
            self.load_dataset_from_file()
            return True
        elif question_lower == 'facebook':
            self.load_facebook_dataset()
            return True
        elif question_lower == 'email':
            self.load_email_dataset()
            return True
        elif question_lower == 'metrics':
            self.show_detailed_metrics()
            return True
        elif question_lower == 'clear':
            print("\033[2J\033[H")  # Clear screen
            self.print_banner()
            return True
        
        # Process as analysis question
        if not self.agent:
            print("❌ Agent not initialized. Please restart the program.")
            return True
        
        if not self.current_graph:
            print("❌ No network loaded. Use 'sample', 'custom', 'facebook', 'email', or 'dataset' to load a network first.")
            return True
        
        try:
            print(f"\n🤔 Analyzing: '{question}'")
            print("⏳ Processing...")
            
            result = self.agent.analyze_social_network(question, graph_data=self.current_graph)
            
            print("\n" + "="*50)
            
            if result["error"]:
                print(f"❌ Error: {result['error']}")
            else:
                # Show analysis type
                if result['analysis_results']:
                    analysis_type = result['analysis_results'][0].get('operation', 'unknown')
                    print(f"📈 Analysis Type: {analysis_type}")
                
                # Show AI insights
                if result['insights']:
                    print(f"\n🤖 AI Analysis:\n{result['insights']}")
                
                # Show key metrics if available
                if result['metrics']:
                    print(f"\n📊 Key Metrics:")
                    for key, value in result['metrics'].items():
                        if isinstance(value, float):
                            print(f"   • {key}: {value:.4f}")
                        else:
                            print(f"   • {key}: {value}")
                
                # Show detailed results if available
                if result['analysis_results']:
                    for analysis in result['analysis_results']:
                        if 'result' in analysis and analysis['result']:
                            print(f"\n📋 Detailed Results ({analysis.get('operation', 'unknown')}):")
                            result_data = analysis['result']
                            if isinstance(result_data, dict):
                                for key, value in result_data.items():
                                    if isinstance(value, (list, dict)) and len(str(value)) > 100:
                                        print(f"   • {key}: [Complex data - {len(value) if hasattr(value, '__len__') else 'N/A'} items]")
                                    else:
                                        print(f"   • {key}: {value}")
            
            print("="*50)
            
        except Exception as e:
            print(f"❌ Error processing question: {str(e)}")
        
        return True
    
    def run(self):
        """Run the interactive Q&A session."""
        self.print_banner()
        
        # Initialize agent
        if not self.initialize_agent():
            print("❌ Failed to initialize agent. Exiting.")
            return
        
        # Load default network
        print("\n🏗️  Loading default sample network...")
        self.load_sample_network()
        
        print("\n💡 Ready! Ask me anything about the social network!")
        print("   Type 'help' for commands or start asking questions.")
        
        # Main interaction loop
        while True:
            try:
                print("\n" + "-"*30)
                question = input("🤔 Your Question: ").strip()
                
                if not question:
                    continue
                
                if not self.process_question(question):
                    break
                    
            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Session ended. Goodbye!")
                break
        
        print("👋 Thanks for using the Social Graph Analysis Agent!")


if __name__ == "__main__":
    print("Starting Interactive Q&A Session...")
    
    try:
        qa_system = InteractiveQA()
        qa_system.run()
    except Exception as e:
        print(f"❌ Failed to start Q&A system: {str(e)}")
        sys.exit(1) 