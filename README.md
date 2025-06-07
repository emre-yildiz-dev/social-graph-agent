# Social Graph Analysis Agent

A sophisticated LangGraph agent that analyzes social networks using NetworkX tools and Ollama's Gemma3:27b LLM. This system provides comprehensive social network analysis with natural language interfaces, leveraging Python typing and Pydantic for robust data validation.

## 🌟 Features

- **Natural Language Queries**: Ask questions about your social network in plain English
- **Comprehensive Analysis**: Multiple analysis types including centrality, community detection, robustness, and path analysis
- **AI-Powered Insights**: Gemma3:27b model provides intelligent interpretations of network data
- **Type Safety**: Full Python typing and Pydantic data validation
- **Flexible Data Input**: Support for custom graph data or auto-generated sample networks
- **State-based Workflow**: Uses LangGraph for robust, stateful analysis workflows

## 🏗️ Architecture

The system consists of several key components:

1. **`models.py`**: Pydantic data models for type-safe data structures
2. **`graph_tools.py`**: NetworkX-based tools for social network analysis
3. **`llm_client.py`**: Ollama integration for AI-powered insights
4. **`social_graph_agent.py`**: Main LangGraph agent orchestrating the analysis
5. **`example_usage.py`**: Comprehensive examples and demonstrations

## 📋 Prerequisites

- Python 3.8+
- Ollama installed and running
- Gemma3:27b model available in Ollama

## 🚀 Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Ollama**:
   ```bash
   # Install Ollama (if not already installed)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama service
   ollama serve
   
   # Pull the Gemma3:27b model (in another terminal)
   ollama pull gemma2:27b
   ```

3. **Verify installation**:
   ```bash
   python example_usage.py
   ```

## 🎯 Quick Start

### Basic Usage

```python
from social_graph_agent import SocialGraphAgent

# Create the agent
agent = SocialGraphAgent()

# Ask a question about a social network
result = agent.analyze_social_network(
    "Who are the most influential people in this network?"
)

print(f"Analysis: {result['insights']}")
```

### Custom Graph Data

```python
from models import NodeData, EdgeData
from graph_tools import SocialGraphAnalyzer

# Define your network
nodes = [
    NodeData(node_id="alice", name="Alice Johnson", 
             attributes={"department": "Engineering"}),
    NodeData(node_id="bob", name="Bob Smith", 
             attributes={"department": "Marketing"}),
    # ... more nodes
]

edges = [
    EdgeData(source="alice", target="bob", weight=0.8, 
             relationship_type="colleague"),
    # ... more edges
]

# Create graph
analyzer = SocialGraphAnalyzer()
graph = analyzer.load_graph_from_data(nodes, edges)

# Analyze with the agent
result = agent.analyze_social_network(
    "What departments are most connected?", 
    graph_data=graph
)
```

## 🔍 Analysis Types

The agent automatically determines the best analysis approach based on your question:

### 1. **Basic Metrics**
- Network density, clustering coefficient
- Connected components analysis
- Overall network statistics

```python
"What are the basic statistics of this network?"
"How well-connected is this network overall?"
```

### 2. **Centrality Analysis**
- Degree, betweenness, closeness, eigenvector centrality
- Identification of influential nodes
- Ranking by different importance measures

```python
"Who are the most influential people in this network?"
"Which person has the most connections?"
"Who acts as the main bridge between different groups?"
```

### 3. **Community Detection**
- Automatic community discovery
- Group analysis and characterization
- Cross-community connection analysis

```python
"What communities exist in this social network?"
"Can you identify different groups or departments?"
"How are the different communities connected?"
```

### 4. **Robustness Analysis**
- Network resilience to node removal
- Critical node identification
- Vulnerability assessment

```python
"How robust is this network to key people leaving?"
"Which person would cause the most disruption if they left?"
"What happens if we remove the most central people?"
```

### 5. **Path Analysis**
- Shortest paths between nodes
- Connectivity analysis
- Reachability assessment

```python
"What's the shortest path between Alice and Bob?"
"How are different people connected?"
"Find the path between any two people"
```

### 6. **Neighborhood Analysis**
- Local network structure around specific nodes
- Local clustering and density
- Ego network analysis

```python
"Show me the neighborhood analysis for Alice"
"What does the local network around Bob look like?"
"Analyze the connections around the manager"
```

## 📊 Data Models

### Node Data
```python
NodeData(
    node_id="unique_id",
    name="Display Name",
    attributes={
        "age": 30,
        "department": "Engineering",
        "location": "NYC"
        # ... any custom attributes
    }
)
```

### Edge Data
```python
EdgeData(
    source="node_id_1",
    target="node_id_2",
    weight=0.8,  # Connection strength (0-1)
    relationship_type="colleague",
    attributes={
        "interaction_frequency": "daily",
        "years_known": 3
        # ... any custom attributes
    }
)
```

## 🤖 AI Integration

The system uses Ollama's Gemma3:27b model to provide intelligent insights:

- **Query Understanding**: Automatically determines what type of analysis to perform
- **Results Interpretation**: Explains complex network metrics in plain language
- **Contextual Insights**: Provides actionable recommendations based on analysis
- **Natural Language**: All interactions in conversational English

## 📈 Example Queries

Here are some example questions you can ask:

**Influence & Leadership**:
- "Who has the most influence in this organization?"
- "Which people are the key connectors?"
- "Who would be the best person to spread information through the network?"

**Groups & Communities**:
- "What teams or groups can you identify?"
- "How do different departments interact?"
- "Are there isolated groups in the network?"

**Network Health**:
- "How resilient is this network?"
- "What are the weak points in our organization?"
- "How would restructuring affect communication?"

**Connectivity**:
- "How well-connected are our teams?"
- "Who bridges different parts of the organization?"
- "What's the typical path length between people?"

## 🔧 Advanced Usage

### Custom Analysis Parameters

```python
# Specify analysis parameters through natural language
result = agent.analyze_social_network(
    "Find the top 10 most influential people using betweenness centrality"
)

# Or analyze specific nodes
result = agent.analyze_social_network(
    "Analyze the neighborhood around Alice with radius 2",
    graph_data=your_graph
)
```

### Batch Analysis

```python
queries = [
    "Basic network statistics",
    "Community detection",
    "Robustness analysis"
]

results = []
for query in queries:
    result = agent.analyze_social_network(query, graph_data=graph)
    results.append(result)
```

## 🛠️ Troubleshooting

### Common Issues

1. **Ollama Connection Failed**:
   - Ensure Ollama is running: `ollama serve`
   - Check if model is available: `ollama list`
   - Pull the model if needed: `ollama pull gemma2:27b`

2. **Import Errors**:
   - Install all dependencies: `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

3. **Empty Analysis Results**:
   - Verify your graph has nodes and edges
   - Check for disconnected components
   - Ensure node IDs are strings

### Performance Tips

- For large networks (>1000 nodes), consider sampling or filtering
- Some centrality measures can be computationally expensive
- Community detection scales well but may take time on very large networks

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📧 Support

For questions or support, please open an issue on the project repository. 