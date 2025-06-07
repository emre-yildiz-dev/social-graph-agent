from typing import Dict, List, Optional, Any
import ollama
import json
from models import AgentState, GraphMetrics
from pydantic import BaseModel


class OllamaClient:
    """Client for interacting with Ollama's Gemma3:27b model."""
    
    def __init__(self, model_name: str = "gemma3:27b"):
        """Initialize Ollama client with specified model."""
        self.model_name = model_name
        self.client = ollama
        
    def test_connection(self) -> bool:
        """Test if Ollama is running and model is available."""
        try:
            response = self.client.list()
            available_models = [model['name'] for model in response['models']]
            return self.model_name in available_models
        except Exception as e:
            print(f"Ollama connection test failed: {e}")
            return False
    
    def generate_graph_insights(self, metrics: GraphMetrics, user_query: str) -> str:
        """Generate insights about the social graph based on metrics and user query."""
        
        # Prepare structured data for the LLM
        metrics_summary = metrics.to_summary_dict()
        
        prompt = f"""You are a social network analysis expert. Analyze the following social graph metrics and answer the user's question.

GRAPH METRICS:
{json.dumps(metrics_summary, indent=2)}

USER QUESTION: {user_query}

Please provide a comprehensive analysis that includes:
1. Key insights about the network structure
2. Identification of important nodes and their roles
3. Community patterns and connectivity
4. Answers to the specific user question
5. Actionable recommendations based on the analysis

Keep your response informative but concise, focusing on the most relevant insights."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error generating insights: {str(e)}"
    
    def explain_centrality_results(self, influential_nodes: Dict[str, List], user_query: str) -> str:
        """Explain centrality analysis results in natural language."""
        
        prompt = f"""You are explaining social network centrality analysis to a user. Here are the most influential nodes by different measures:

INFLUENTIAL NODES:
{json.dumps(influential_nodes, indent=2)}

USER QUESTION: {user_query}

Please explain:
1. What each centrality measure means in social network context
2. Who are the key players and why they're important
3. The differences between the centrality rankings
4. Practical implications of these findings
5. Answer to the user's specific question

Make your explanation accessible and actionable."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error explaining centrality: {str(e)}"
    
    def analyze_communities(self, communities: List[set], graph_data: Dict, user_query: str) -> str:
        """Analyze and explain community detection results."""
        
        # Convert sets to lists for JSON serialization
        communities_data = [list(community) for community in communities]
        
        prompt = f"""You are analyzing communities detected in a social network. Here's the data:

DETECTED COMMUNITIES:
Number of communities: {len(communities_data)}
Community sizes: {[len(c) for c in communities_data]}
Communities: {json.dumps(communities_data, indent=2)}

GRAPH CONTEXT:
{json.dumps(graph_data, indent=2)}

USER QUESTION: {user_query}

Please analyze:
1. The community structure and what it reveals about the network
2. Size distribution and balance of communities
3. Potential meaning or interpretation of these groupings
4. Cross-community connections and bridges
5. Answer to the user's specific question

Provide insights that would be valuable for understanding social dynamics."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error analyzing communities: {str(e)}"
    
    def interpret_robustness_analysis(self, robustness_data: Dict, user_query: str) -> str:
        """Interpret network robustness analysis results."""
        
        prompt = f"""You are analyzing the robustness of a social network. Here's the analysis of what happens when key nodes are removed:

ROBUSTNESS ANALYSIS:
{json.dumps(robustness_data, indent=2)}

USER QUESTION: {user_query}

Please provide insights on:
1. Which nodes are most critical to network connectivity
2. How resilient the network is to targeted attacks or departures
3. Vulnerabilities and strengths in the network structure
4. Recommendations for improving network robustness
5. Answer to the user's specific question

Focus on practical implications for network stability and resilience."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error interpreting robustness: {str(e)}"
    
    def general_graph_analysis(self, analysis_results: Dict, user_query: str) -> str:
        """Provide general analysis of any graph analysis results."""
        
        prompt = f"""You are a social network analysis expert. The user has asked a question about their social network, and here are the analysis results:

ANALYSIS RESULTS:
{json.dumps(analysis_results, indent=2)}

USER QUESTION: {user_query}

Please provide a comprehensive response that:
1. Directly answers the user's question
2. Explains the relevant findings in accessible terms
3. Provides context and interpretation of the results
4. Offers actionable insights or recommendations
5. Highlights any notable patterns or anomalies

Make your response practical and valuable for decision-making."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error in general analysis: {str(e)}"
    
    def determine_analysis_approach(self, user_query: str) -> Dict[str, Any]:
        """Determine what type of analysis to perform based on user query."""
        
        prompt = f"""You are a social network analysis expert. Based on the user's question, determine what type of analysis would be most appropriate.

USER QUESTION: {user_query}

Respond with a JSON object containing:
{{
    "analysis_type": "one of: basic_metrics, centrality, community_detection, path_analysis, robustness, neighborhood, custom",
    "parameters": {{"key": "value pairs for analysis parameters"}},
    "reasoning": "brief explanation of why this analysis type was chosen"
}}

Available analysis types:
- basic_metrics: Overall network statistics and structure
- centrality: Finding influential nodes and their roles
- community_detection: Identifying groups and clusters
- path_analysis: Shortest paths and connectivity
- robustness: Network resilience to node removal
- neighborhood: Local analysis around specific nodes
- custom: Combination of multiple analysis types

Only respond with valid JSON."""

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            
            # Try to parse the JSON response
            try:
                result = json.loads(response['message']['content'])
                return result
            except json.JSONDecodeError:
                # Fallback to basic metrics if JSON parsing fails
                return {
                    "analysis_type": "basic_metrics",
                    "parameters": {},
                    "reasoning": "Default analysis due to parsing error"
                }
                
        except Exception as e:
            return {
                "analysis_type": "basic_metrics",
                "parameters": {},
                "reasoning": f"Default analysis due to error: {str(e)}"
            } 