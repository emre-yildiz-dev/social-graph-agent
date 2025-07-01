#!/usr/bin/env python3
"""
Real-World Graph Data Analysis Script

This script is designed to analyze real-world social network datasets including:
- Social media networks (Twitter, Facebook, etc.)
- Collaboration networks (research, GitHub, etc.)
- Communication networks (email, messages, etc.)
- Organization networks (company hierarchies, etc.)

Supports multiple input formats:
- CSV files (edge lists, adjacency lists)
- JSON files (nodes and edges)
- GraphML files
- NetworkX pickle files
- Adjacency matrices

Features:
- Data validation and preprocessing
- Comprehensive network analysis
- Performance optimization for large graphs
- Detailed reporting and insights
- Export capabilities
"""

import os
import sys
import json
import csv
import pickle
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Union
import pandas as pd
import networkx as nx
from datetime import datetime

from social_graph_agent import SocialGraphAgent
from models import NodeData, EdgeData, GraphMetrics
from graph_tools import SocialGraphAnalyzer


class RealWorldGraphAnalyzer:
    """Analyzer for real-world graph datasets."""
    
    def __init__(self, model_name: str = "gemma3n:latest"):
        """Initialize the real-world graph analyzer."""
        self.agent = SocialGraphAgent(model_name)
        self.analyzer = SocialGraphAnalyzer()
        self.graph = None
        self.graph_info = {}
        self.analysis_results = {}
        
    def load_graph_from_csv_edgelist(self, filepath: str, source_col: Union[str, int] = "source", 
                                   target_col: Union[str, int] = "target", weight_col: Optional[Union[str, int]] = None,
                                   directed: bool = False, delimiter: str = ",") -> nx.Graph:
        """Load graph from CSV edge list format."""
        print(f"📁 Loading graph from CSV edge list: {filepath}")
        
        try:
            df = pd.read_csv(filepath, delimiter=delimiter, comment='#', header=None)
            print(f"   📊 Found {len(df)} edges in file")
            
            # For files with no headers, use column indices
            if source_col == "source":
                source_col = 0
            if target_col == "target":  
                target_col = 1
            
            # Validate required columns
            max_col = max(source_col if isinstance(source_col, int) else 0, 
                         target_col if isinstance(target_col, int) else 1)
            if max_col >= len(df.columns):
                raise ValueError(f"Required column index {max_col} not found. Available columns: {len(df.columns)}")
            
            # Create graph
            if directed:
                G = nx.DiGraph()
                print("   🔄 Creating directed graph")
            else:
                G = nx.Graph()
                print("   🔄 Creating undirected graph")
            
            # Add edges
            for _, row in df.iterrows():
                source = str(row[source_col])
                target = str(row[target_col])
                
                if weight_col is not None and isinstance(weight_col, int) and weight_col < len(df.columns):
                    weight = float(row[weight_col])
                    G.add_edge(source, target, weight=weight)
                else:
                    G.add_edge(source, target)
            
            self.graph_info = {
                "source": filepath,
                "format": "CSV EdgeList",
                "directed": directed,
                "loaded_at": datetime.now().isoformat(),
                "original_edges": len(df),
                "final_nodes": G.number_of_nodes(),
                "final_edges": G.number_of_edges()
            }
            
            print(f"   ✅ Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
            return G
            
        except Exception as e:
            print(f"   ❌ Error loading CSV: {str(e)}")
            raise
    
    def load_graph_from_json(self, filepath: str) -> nx.Graph:
        """Load graph from JSON format (nodes and edges arrays)."""
        print(f"📁 Loading graph from JSON: {filepath}")
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Support different JSON formats
            if 'nodes' in data and 'edges' in data:
                # Standard format: {"nodes": [...], "edges": [...]}
                nodes_data = data['nodes']
                edges_data = data['edges']
            elif 'links' in data:
                # D3.js format: {"nodes": [...], "links": [...]}
                nodes_data = data.get('nodes', [])
                edges_data = data['links']
            else:
                raise ValueError("JSON must contain 'nodes' and 'edges' (or 'links') arrays")
            
            # Determine if directed
            directed = data.get('directed', False)
            G = nx.DiGraph() if directed else nx.Graph()
            
            # Add nodes
            for node in nodes_data:
                if isinstance(node, dict):
                    node_id = node.get('id', node.get('name'))
                    attributes = {k: v for k, v in node.items() if k not in ['id', 'name']}
                    G.add_node(str(node_id), **attributes)
                else:
                    G.add_node(str(node))
            
            # Add edges
            for edge in edges_data:
                if isinstance(edge, dict):
                    source = str(edge.get('source', edge.get('from')))
                    target = str(edge.get('target', edge.get('to')))
                    weight = edge.get('weight', edge.get('value', 1.0))
                    attributes = {k: v for k, v in edge.items() if k not in ['source', 'target', 'from', 'to']}
                    G.add_edge(source, target, weight=weight, **attributes)
                elif isinstance(edge, (list, tuple)) and len(edge) >= 2:
                    G.add_edge(str(edge[0]), str(edge[1]))
            
            self.graph_info = {
                "source": filepath,
                "format": "JSON",
                "directed": directed,
                "loaded_at": datetime.now().isoformat(),
                "original_nodes": len(nodes_data),
                "original_edges": len(edges_data),
                "final_nodes": G.number_of_nodes(),
                "final_edges": G.number_of_edges()
            }
            
            print(f"   ✅ Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
            return G
            
        except Exception as e:
            print(f"   ❌ Error loading JSON: {str(e)}")
            raise
    
    def load_graph_from_graphml(self, filepath: str) -> nx.Graph:
        """Load graph from GraphML format."""
        print(f"📁 Loading graph from GraphML: {filepath}")
        
        try:
            G = nx.read_graphml(filepath)
            
            self.graph_info = {
                "source": filepath,
                "format": "GraphML",
                "directed": G.is_directed(),
                "loaded_at": datetime.now().isoformat(),
                "final_nodes": G.number_of_nodes(),
                "final_edges": G.number_of_edges()
            }
            
            print(f"   ✅ Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
            return G
            
        except Exception as e:
            print(f"   ❌ Error loading GraphML: {str(e)}")
            raise
    
    def load_graph_from_adjacency_matrix(self, filepath: str, delimiter: str = ",") -> nx.Graph:
        """Load graph from adjacency matrix CSV."""
        print(f"📁 Loading graph from adjacency matrix: {filepath}")
        
        try:
            df = pd.read_csv(filepath, delimiter=delimiter, index_col=0)
            
            # Convert to NetworkX graph
            G = nx.from_pandas_adjacency(df)
            
            self.graph_info = {
                "source": filepath,
                "format": "Adjacency Matrix",
                "directed": False,
                "loaded_at": datetime.now().isoformat(),
                "matrix_size": f"{df.shape[0]}x{df.shape[1]}",
                "final_nodes": G.number_of_nodes(),
                "final_edges": G.number_of_edges()
            }
            
            print(f"   ✅ Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
            return G
            
        except Exception as e:
            print(f"   ❌ Error loading adjacency matrix: {str(e)}")
            raise
    
    def auto_detect_and_load(self, filepath: str, **kwargs) -> nx.Graph:
        """Auto-detect file format and load appropriately."""
        filepath = Path(filepath)
        
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        extension = filepath.suffix.lower()
        
        print(f"🔍 Auto-detecting format for: {filepath.name}")
        
        if extension in ['.csv', '.txt']:
            # Try to determine if it's an edge list or adjacency matrix
            try:
                # Use appropriate delimiter for .txt files
                delimiter = kwargs.get('delimiter', '\t' if extension == '.txt' else ',')
                df = pd.read_csv(filepath, delimiter=delimiter, nrows=5, comment='#')
                
                if len(df.columns) == len(df.index) and all(col in df.index for col in df.columns):
                    # Likely adjacency matrix
                    print("   📊 Detected: Adjacency Matrix")
                    return self.load_graph_from_adjacency_matrix(str(filepath), **kwargs)
                else:
                    # Likely edge list
                    print("   📊 Detected: Edge List")
                    return self.load_graph_from_csv_edgelist(str(filepath), **kwargs)
            except Exception:
                # Default to edge list if detection fails
                print("   📊 Detected: Edge List (default)")
                return self.load_graph_from_csv_edgelist(str(filepath), **kwargs)
                
        elif extension == '.json':
            print("   📊 Detected: JSON")
            return self.load_graph_from_json(str(filepath))
            
        elif extension in ['.graphml', '.xml']:
            print("   📊 Detected: GraphML")
            return self.load_graph_from_graphml(str(filepath))
            
        elif extension in ['.pkl', '.pickle']:
            print("   📊 Detected: NetworkX Pickle")
            return nx.read_gpickle(str(filepath))
            
        else:
            raise ValueError(f"Unsupported file format: {extension}")
    
    def validate_and_preprocess(self, G: nx.Graph, remove_self_loops: bool = True,
                              remove_isolates: bool = False, largest_component_only: bool = False) -> nx.Graph:
        """Validate and preprocess the graph."""
        print("🔧 Validating and preprocessing graph...")
        
        original_nodes = G.number_of_nodes()
        original_edges = G.number_of_edges()
        
        # Remove self loops
        if remove_self_loops:
            self_loops = list(nx.selfloop_edges(G))
            if self_loops:
                G.remove_edges_from(self_loops)
                print(f"   🔄 Removed {len(self_loops)} self loops")
        
        # Remove isolated nodes
        if remove_isolates:
            isolates = list(nx.isolates(G))
            if isolates:
                G.remove_nodes_from(isolates)
                print(f"   🔄 Removed {len(isolates)} isolated nodes")
        
        # Keep only largest connected component
        if largest_component_only and not nx.is_connected(G):
            largest_cc = max(nx.connected_components(G), key=len)
            G = G.subgraph(largest_cc).copy()
            print(f"   🔄 Keeping largest component: {len(largest_cc)} nodes")
        
        print(f"   ✅ Preprocessing complete: {original_nodes}→{G.number_of_nodes()} nodes, {original_edges}→{G.number_of_edges()} edges")
        
        # Update graph info
        self.graph_info.update({
            "preprocessing": {
                "remove_self_loops": remove_self_loops,
                "remove_isolates": remove_isolates,
                "largest_component_only": largest_component_only,
                "original_nodes": original_nodes,
                "original_edges": original_edges,
                "final_nodes": G.number_of_nodes(),
                "final_edges": G.number_of_edges()
            }
        })
        
        return G
    
    def analyze_graph_comprehensively(self, query: str = "Provide a comprehensive analysis of this real-world social network") -> Dict[str, Any]:
        """Perform comprehensive analysis of the loaded graph."""
        if self.graph is None:
            raise ValueError("No graph loaded. Please load a graph first.")
        
        print("📊 Performing comprehensive analysis...")
        
        # Set the graph in analyzer
        self.analyzer.graph = self.graph
        
        # Calculate all metrics
        print("   🔢 Calculating network metrics...")
        metrics = self.analyzer.calculate_comprehensive_metrics()
        
        # Detect communities
        print("   🏘️  Detecting communities...")
        communities = self.analyzer.detect_communities()
        
        # Find influential nodes
        print("   🎯 Identifying influential nodes...")
        influential = self.analyzer.find_influential_nodes(top_k=10)
        
        # Analyze robustness (for smaller graphs)
        robustness = None
        if self.graph.number_of_nodes() <= 1000:
            print("   🛡️  Analyzing network robustness...")
            robustness = self.analyzer.analyze_graph_robustness(num_removals=min(5, self.graph.number_of_nodes()//10))
        else:
            print("   ⚠️  Skipping robustness analysis (graph too large)")
        
        # Get AI insights
        print("   🤖 Generating AI insights...")
        try:
            insights = self.agent.analyze_social_network(query, graph_data=self.graph)
        except Exception as e:
            print(f"   ⚠️  AI analysis failed: {str(e)}")
            insights = {"insights": "AI analysis not available", "error": str(e)}
        
        # Compile results
        self.analysis_results = {
            "graph_info": self.graph_info,
            "metrics": metrics.to_summary_dict(),
            "communities": {
                "count": len(communities),
                "sizes": [len(c) for c in communities],
                "modularity": nx.community.modularity(self.graph, communities) if communities else 0
            },
            "influential_nodes": influential,
            "robustness": robustness,
            "ai_insights": insights.get("insights", ""),
            "analysis_timestamp": datetime.now().isoformat()
        }
        
        return self.analysis_results
    
    def _format_number(self, value: Any, decimals: int = 4) -> str:
        """Safely format a number for display."""
        if value == 'N/A' or value is None:
            return 'N/A'
        try:
            return f"{float(value):.{decimals}f}"
        except (ValueError, TypeError):
            return str(value)
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """Generate a comprehensive analysis report."""
        if not self.analysis_results:
            raise ValueError("No analysis results available. Run analyze_graph_comprehensively first.")
        
        report_lines = []
        
        # Header
        report_lines.extend([
            "="*80,
            "REAL-WORLD SOCIAL NETWORK ANALYSIS REPORT",
            "="*80,
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            ""
        ])
        
        # Graph Information
        graph_info = self.analysis_results["graph_info"]
        report_lines.extend([
            "📊 DATASET INFORMATION:",
            "-" * 40,
            f"Source: {graph_info.get('source', 'Unknown')}",
            f"Format: {graph_info.get('format', 'Unknown')}",
            f"Type: {'Directed' if graph_info.get('directed') else 'Undirected'}",
            f"Loaded: {graph_info.get('loaded_at', 'Unknown')}",
            ""
        ])
        
        if "preprocessing" in graph_info:
            prep = graph_info["preprocessing"]
            report_lines.extend([
                "🔧 PREPROCESSING:",
                f"Original: {prep['original_nodes']} nodes, {prep['original_edges']} edges",
                f"Final: {prep['final_nodes']} nodes, {prep['final_edges']} edges",
                f"Self loops removed: {prep['remove_self_loops']}",
                f"Isolates removed: {prep['remove_isolates']}",
                f"Largest component only: {prep['largest_component_only']}",
                ""
            ])
        
        # Network Metrics
        metrics = self.analysis_results["metrics"]
        basic_stats = metrics.get("basic_stats", {})
        
        report_lines.extend([
            "📈 NETWORK METRICS:",
            "-" * 40,
            f"Nodes: {basic_stats.get('num_nodes', 'N/A')}",
            f"Edges: {basic_stats.get('num_edges', 'N/A')}",
            f"Density: {self._format_number(basic_stats.get('density', 'N/A'), 6)}",
            f"Average Degree: {self._format_number(basic_stats.get('average_degree', 'N/A'), 2)}",
            f"Clustering Coefficient: {self._format_number(basic_stats.get('clustering_coefficient', 'N/A'), 4)}",
            f"Connected Components: {basic_stats.get('num_connected_components', 'N/A')}",
            f"Largest Component: {basic_stats.get('largest_component_size', 'N/A')} nodes",
            ""
        ])
        
        # Community Analysis
        communities = self.analysis_results["communities"]
        report_lines.extend([
            "🏘️  COMMUNITY STRUCTURE:",
            "-" * 40,
            f"Number of Communities: {communities['count']}",
            f"Modularity Score: {self._format_number(communities['modularity'], 4)}",
            f"Community Sizes: {communities['sizes'][:10]}{'...' if len(communities['sizes']) > 10 else ''}",
            ""
        ])
        
        # Influential Nodes
        influential = self.analysis_results["influential_nodes"]
        report_lines.extend([
            "🎯 MOST INFLUENTIAL NODES:",
            "-" * 40
        ])
        
        for measure, nodes in influential.items():
            if nodes:
                top_3 = nodes[:3]  # nodes is already a list of tuples
                report_lines.append(f"{measure.replace('_', ' ').title()}:")
                for node, score in top_3:
                    report_lines.append(f"  • {node}: {self._format_number(score, 4)}")
                report_lines.append("")
        
        # Robustness (if available)
        if self.analysis_results["robustness"]:
            robustness = self.analysis_results["robustness"]
            report_lines.extend([
                "🛡️  NETWORK ROBUSTNESS:",
                "-" * 40,
                f"Original Connectivity: {self._format_number(robustness.get('original_connectivity', 'N/A'), 4)}",
                f"Critical Nodes Tested: {len(robustness.get('removal_results', []))}",
                ""
            ])
        
        # AI Insights
        if self.analysis_results["ai_insights"]:
            report_lines.extend([
                "🤖 AI ANALYSIS & INSIGHTS:",
                "-" * 40,
                self.analysis_results["ai_insights"],
                ""
            ])
        
        report_lines.extend([
            "="*80,
            "End of Report",
            "="*80
        ])
        
        report = "\n".join(report_lines)
        
        # Save to file if requested
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"📄 Report saved to: {output_file}")
        
        return report
    
    def export_results(self, output_dir: str = "analysis_output") -> Dict[str, str]:
        """Export analysis results to multiple formats."""
        if not self.analysis_results:
            raise ValueError("No analysis results to export.")
        
        os.makedirs(output_dir, exist_ok=True)
        output_files = {}
        
        # JSON export
        json_file = os.path.join(output_dir, "analysis_results.json")
        with open(json_file, 'w') as f:
            json.dump(self.analysis_results, f, indent=2, default=str)
        output_files["json"] = json_file
        
        # Text report
        report_file = os.path.join(output_dir, "analysis_report.txt")
        self.generate_report(report_file)
        output_files["report"] = report_file
        
        # Graph export (if not too large)
        if self.graph and self.graph.number_of_nodes() <= 10000:
            graphml_file = os.path.join(output_dir, "processed_graph.graphml")
            nx.write_graphml(self.graph, graphml_file)
            output_files["graphml"] = graphml_file
        
        print(f"📁 Results exported to: {output_dir}")
        return output_files


def create_sample_datasets():
    """Create sample datasets for testing."""
    print("📝 Creating sample datasets for testing...")
    
    os.makedirs("sample_data", exist_ok=True)
    
    # 1. CSV Edge List - Social Media Network
    social_edges = [
        ["user1", "user2", 0.8],
        ["user1", "user3", 0.6],
        ["user2", "user4", 0.9],
        ["user3", "user4", 0.7],
        ["user4", "user5", 0.5],
        ["user5", "user6", 0.8],
        ["user1", "user6", 0.4],
        ["user2", "user5", 0.6],
        ["user3", "user6", 0.3]
    ]
    
    with open("sample_data/social_network.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source", "target", "weight"])
        writer.writerows(social_edges)
    
    # 2. JSON Network - Collaboration Network
    collab_data = {
        "directed": False,
        "nodes": [
            {"id": "researcher1", "department": "CS", "papers": 25},
            {"id": "researcher2", "department": "CS", "papers": 18},
            {"id": "researcher3", "department": "Math", "papers": 30},
            {"id": "researcher4", "department": "Physics", "papers": 22},
            {"id": "researcher5", "department": "CS", "papers": 15}
        ],
        "edges": [
            {"source": "researcher1", "target": "researcher2", "collaborations": 5},
            {"source": "researcher1", "target": "researcher3", "collaborations": 3},
            {"source": "researcher2", "target": "researcher4", "collaborations": 2},
            {"source": "researcher3", "target": "researcher5", "collaborations": 4},
            {"source": "researcher1", "target": "researcher5", "collaborations": 6}
        ]
    }
    
    with open("sample_data/collaboration_network.json", "w") as f:
        json.dump(collab_data, f, indent=2)
    
    print("✅ Sample datasets created in 'sample_data/' folder:")
    print("   📄 social_network.csv - Social media network (CSV edge list)")
    print("   📄 collaboration_network.json - Research collaboration network (JSON)")


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Analyze real-world social network data")
    
    parser.add_argument("input_file", nargs="?", help="Input graph data file")
    parser.add_argument("--format", choices=["auto", "csv", "json", "graphml", "adjacency"], 
                       default="auto", help="Input file format")
    parser.add_argument("--directed", action="store_true", help="Treat graph as directed")
    parser.add_argument("--source-col", default="source", help="Source column name (for CSV)")
    parser.add_argument("--target-col", default="target", help="Target column name (for CSV)")
    parser.add_argument("--weight-col", help="Weight column name (for CSV)")
    parser.add_argument("--delimiter", default=",", help="CSV delimiter")
    parser.add_argument("--remove-self-loops", action="store_true", help="Remove self loops")
    parser.add_argument("--remove-isolates", action="store_true", help="Remove isolated nodes")
    parser.add_argument("--largest-component", action="store_true", help="Keep only largest component")
    parser.add_argument("--output-dir", default="analysis_output", help="Output directory")
    parser.add_argument("--query", default="Provide a comprehensive analysis of this real-world social network",
                       help="Analysis query for AI insights")
    parser.add_argument("--create-samples", action="store_true", help="Create sample datasets and exit")
    
    args = parser.parse_args()
    
    print("🌍 Real-World Graph Analysis Tool")
    print("="*50)
    
    # Create sample datasets if requested
    if args.create_samples:
        create_sample_datasets()
        return
    
    # Check if input file provided
    if not args.input_file:
        print("❌ No input file provided.")
        print("💡 Use --create-samples to generate sample datasets first")
        print("   Then run: python real_world_analysis.py sample_data/social_network.csv")
        return
    
    try:
        # Initialize analyzer
        analyzer = RealWorldGraphAnalyzer()
        
        # Load graph
        if args.format == "auto":
            graph = analyzer.auto_detect_and_load(args.input_file, 
                                                 source_col=args.source_col,
                                                 target_col=args.target_col,
                                                 weight_col=args.weight_col,
                                                 directed=args.directed,
                                                 delimiter=args.delimiter)
        elif args.format == "csv":
            graph = analyzer.load_graph_from_csv_edgelist(args.input_file,
                                                         source_col=args.source_col,
                                                         target_col=args.target_col,
                                                         weight_col=args.weight_col,
                                                         directed=args.directed,
                                                         delimiter=args.delimiter)
        elif args.format == "json":
            graph = analyzer.load_graph_from_json(args.input_file)
        elif args.format == "graphml":
            graph = analyzer.load_graph_from_graphml(args.input_file)
        elif args.format == "adjacency":
            graph = analyzer.load_graph_from_adjacency_matrix(args.input_file, args.delimiter)
        
        # Preprocess
        analyzer.graph = analyzer.validate_and_preprocess(
            graph,
            remove_self_loops=args.remove_self_loops,
            remove_isolates=args.remove_isolates,
            largest_component_only=args.largest_component
        )
        
        # Analyze
        results = analyzer.analyze_graph_comprehensively(args.query)
        
        # Generate and display report
        report = analyzer.generate_report()
        print("\n" + report)
        
        # Save results
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Save JSON results
        json_file = os.path.join(args.output_dir, "analysis_results.json")
        with open(json_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        # Save text report
        report_file = os.path.join(args.output_dir, "analysis_report.txt")
        analyzer.generate_report(report_file)
        
        print(f"\n🎉 Analysis complete! Files saved:")
        print(f"   📄 JSON: {json_file}")
        print(f"   📄 Report: {report_file}")
        
    except Exception as e:
        print(f"\n❌ Analysis failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main() 