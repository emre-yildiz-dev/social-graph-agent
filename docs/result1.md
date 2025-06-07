(.venv) ➜  LangGraph git:(master) ✗ python example_usage.py
🎯 Social Graph Analysis Agent - Example Usage
============================================================
🚀 Initializing Social Graph Analysis Agent...
🔗 Testing Ollama connection...
Ollama connection test failed: 'name'
⚠️  Warning: Ollama connection failed. Make sure Ollama is running with gemma2:27b model.
   You can start Ollama and pull the model with:
   ollama serve
   ollama pull gemma3:27b

============================================================
DEMO 1: Analysis with Sample Network
============================================================

📊 Query 1: Who are the most influential people in this network?
--------------------------------------------------
 
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis of your social network to identify the most influential people, based on the results you provided.

**1. Direct Answer: Who are the most influential people?**

Based on this data, **person_9 consistently emerges as the most influential person in your network.**  They rank highest across multiple key centrality measures – degree, betweenness, closeness, and eigenvector. **Person_20 is a very strong second**, consistently appearing in the top five for each measure.  Beyond these two, **person_11 and person_18 also demonstrate significant influence**, although to a lesser extent.

**2. Explaining the Findings in Accessible Terms**

Let's break down what each of these "centrality measures" means, and why they point to these individuals:

* **Degree Centrality:** This is the simplest measure – it's basically the number of connections a person has.  Think of it as popularity. Person_9 and Person_20 have the most connections, meaning they directly interact with the most people in the network.
* **Betweenness Centrality:** This measures how often a person lies *on the shortest path* between two other people in the network.  High betweenness means that person acts as a bridge or gatekeeper of information.  Person_9 & Person_1 are key connectors, meaning information frequently flows *through* them. If you want to get a message from one part of the network to another, you're likely going to go through these people.
* **Closeness Centrality:** This measures how quickly a person can reach everyone else in the network.  It looks at the average distance (in number of connections) to all other nodes.  A high closeness score means that person can efficiently disseminate information or exert influence across the entire network. Person_9 and Person_20 are the most "reachable" people in your network.
* **Eigenvector Centrality:** This is a more sophisticated measure. It's not just *how many* connections you have, but *who* you're connected to. Being connected to other influential people gives you more influence.  Person_9 again ranks highest, showing they are connected to *other* well-connected people, amplifying their impact.

**3. Context and Interpretation**

* **Network Density (0.1867):** Your network is relatively sparse. This means people aren’t connected to *everyone* else, and information relies more on key individuals to travel.  This makes the roles of the central figures (Person_9, Person_20) even more important.
* **Strong Connectivity (Connected Components = 1, Largest Component Size = 25):** The fact that your network has only one connected component and that component contains all 25 nodes indicates good overall communication within the network. Everyone is, in theory, reachable from everyone else.
* **Consistent Ranking of Person_9:**  The consistent appearance of Person_9 at the top of all centrality rankings is a strong indicator of their overall influence. They aren't just popular; they actively bridge connections, are easily reached, and are connected to *other* influential individuals.
* **Person_20's Significance:**  Person_20 is a clear number two and consistently ranks high. They are a significant influencer in their own right, and could potentially act as a good partner for Person_9.



**4. Actionable Insights & Recommendations**

* **Leverage Person_9:**  If you want to disseminate information quickly, gain support for an initiative, or influence the network's behavior, work with Person_9.  They are your most effective channel.
* **Engage Person_20 as a Key Ally:** Person_20 can help amplify the reach and impact of any initiative you undertake. They are a strong secondary influence.
* **Understand the Information Flow:** Pay attention to how information moves through Person_9 and Person_1.  These are critical nodes.  If you want to know what’s happening in the network, observe their activities.
* **Consider Person_11 & Person_18:** While not as central as Person_9 & Person_20, these individuals still hold a significant position. They could be valuable advocates or connectors within specific sub-groups.
* **Don’t Neglect Peripheral Nodes:** While the central people are important, remember that every node plays a role. Ensure that everyone feels connected to avoid creating silos.




**5. Notable Patterns/Anomalies**

* **Consistency in Top Rankings:** The consistent ranking of Person_9 and Person_20 across all measures is a very strong pattern, highlighting their consistent influence.
* **Betweenness vs. Other Measures:** The fact that Person_1 has a relatively high betweenness centrality, but lower rankings in other measures, suggests they may be more of a *broker* of information rather than an overall influencer. They connect disparate groups, but may not be as broadly connected themselves.



In conclusion, this analysis gives you a strong understanding of the key players in your network and how information flows within it. By understanding these dynamics, you can more effectively engage with the network and achieve your goals.
📊 Key Metrics: {'nodes': 25, 'edges': 56, 'density': 0.1867}

📊 Query 2: What communities or groups exist in this social network?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis of the community structure within your social network, based on the provided data.

**1. Direct Answer to Your Question: What communities or groups exist in this social network?**

Based on the network analysis, it appears your social network is **relatively well-integrated and doesn't show strong, clearly defined communities.**  The fact that you have only *one* connected component (meaning everyone is reachable from everyone else) and a moderate density (0.16) suggests a good level of communication and connection across the entire network. While there aren't distinct "cliques" or isolated groups, we can identify individuals who seem to act as bridges between different parts of the network, hinting at loose groupings centered around those individuals.

**2. Explanation of Relevant Findings (Accessible Terms)**

Let's break down the key metrics and what they tell us about potential groupings:

* **Density (0.16):**  This measures how many connections *actually exist* compared to the maximum possible connections. 0.16 means that 16% of all possible connections are present. It's not *super* dense, but it's also not sparse.  This suggests a moderate level of interconnection – people are connected, but not *everyone* is connected to *everyone*.
* **Connected Components (1):** This is the most important finding for understanding communities. Having *one* connected component means everyone in the network is linked, directly or indirectly.  This strongly suggests the absence of isolated subgroups.
* **Clustering Coefficient (0.1311):** This metric measures how likely it is that your friends are also friends with each other. A value of 0.1311 is fairly low, suggesting that while connections exist, people don't necessarily form tightly-knit groups where everyone knows everyone else.  This reinforces the idea of a more spread-out network.
* **Centrality Measures (Degree, Betweenness, Closeness, Eigenvector):** These help pinpoint *influential* individuals and how they connect different parts of the network.  Looking at these together is crucial.



**3. Context and Interpretation of Results**

The analysis shows a network that is *integrated* rather than *segmented*.  The presence of only one connected component clearly indicates this. The relatively low clustering coefficient suggests that friendships don’t always extend to mutual connections.  This is not necessarily a negative thing - it can indicate a network that's open to new connections and ideas.

Let's look at the centrality measures to see if we can identify loose groupings:

* **Person 0, Person 23, Person 8, and Person 9** consistently appear in the top rankings across multiple centrality measures (Degree, Betweenness, Closeness, Eigenvector). This means they are highly connected, act as bridges between others, and are generally influential in the network. They likely form a central core and are connected to many different people, creating loose connections among subgroups.
* **Person 15** consistently ranks within the top 5 for Betweenness and Closeness, suggesting a role as a connector, but doesn't have quite the same broad influence as the top four.
* **Person 19 and Person 21** show high Eigenvector Centrality, suggesting they are connected to other well-connected individuals, further reinforcing the central core.

Instead of strict communities, think of these individuals as *hubs* radiating connections. People connected to these hubs are likely connected to each other, forming loose groupings, but not necessarily tight-knit communities.



**4. Actionable Insights & Recommendations**

* **Focus on Strengthening Existing Connections:** Because the network is already well-integrated, the focus should be on deepening the relationships that *do* exist. Facilitate interactions between people connected to the central hubs (Person 0, 23, 8, 9) to further strengthen the network.
* **Leverage Influencers:**  If you're trying to disseminate information or promote something within the network, target Person 0, Person 23, Person 8, and Person 9 first.  They are the most likely to amplify your message.
* **Monitor for Emerging Subgroups:** While strong communities don’t currently exist, keep an eye on how connections evolve.  Are new, denser connections forming around specific individuals *other* than the central hubs? This could indicate the beginning of a new community.
* **Consider Network Events:** Organize events that bring together individuals connected to different hubs. This can help solidify existing connections and create new ones.
* **Don’t Force Segmentation:** Avoid trying to create artificial communities. The current network structure appears to thrive on integration.



**5. Notable Patterns or Anomalies**

* **Lack of Strong Community Structure:** The most notable pattern is the *absence* of clear communities. This is a key takeaway.
* **The Central Core:** The consistent presence of Person 0, Person 23, Person 8, and Person 9 at the top of multiple centrality rankings signifies their outsized role in the network. It's worth understanding *why* they are so central. Are they leaders, organizers, or simply well-liked individuals?
* **Potential for Growth:** While the network is integrated, it’s not *fully* connected. Further strengthening connections and encouraging more interaction could increase the density and resilience of the network.




**In conclusion:** Your social network is characterized by a high degree of integration and a lack of strong, defined communities. Focus on nurturing the existing connections and leveraging the influential individuals to maintain and strengthen this network.  Remember to monitor for evolving patterns that might indicate the emergence of new subgroups.
📊 Key Metrics: {'nodes': 25, 'edges': 48, 'density': 0.16}

📊 Query 3: How well-connected is this network overall?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive response to your question about how well-connected your network is, based on the analysis results:

**Overall, your network appears moderately well-connected.** It's not *highly* dense, but it's definitely not fragmented either. Let me break down what that means, using the analysis results as evidence.

**Understanding the Key Findings:**

* **Network Size:** You have 25 people (nodes) connected by 42 relationships (edges). This is a decent size for a focused network.
* **Density (0.14):** Density tells us what proportion of *possible* connections actually exist. A density of 0.14 means that only 14% of all possible connections between people in your network are actually present.  While not super high, it's not drastically low. A network with very low density would feel very fragmented, with lots of isolated individuals.  This suggests connections are happening, but there's room for growth.
* **Connectivity (Single Connected Component):** This is a *very* positive finding!  The analysis shows only one connected component, and it includes *all* 25 people. This means everyone in your network is reachable from everyone else, directly or indirectly.  There aren’t isolated subgroups. This is a strong indicator of overall cohesion.
* **Clustering Coefficient (0.1324):**  This measures how likely your friends are to also be friends with each other ("friend of a friend"). A value of 0.1324 suggests a low, but present, tendency for connections to cluster.  This means there's *some* level of group formation, but it's not overly pronounced.  People aren't necessarily strongly embedded in tightly-knit groups.

**Centrality - Who's Connecting Everyone?**

The centrality metrics give us a deeper understanding of *how* people are connected. Let's look at the top players in each category:

* **Degree Centrality:**  `person_21`, `person_23`, `person_8`, and `person_19` have the highest degree centrality.  This means these individuals have the most direct connections within the network.  They are your immediate hubs for information and interaction.
* **Betweenness Centrality:** `person_23` and `person_19` are the biggest ‘bridges’ in your network. They lie on many of the shortest paths between other people. If you want information to flow efficiently, these people are critical.  Disrupting their connections would significantly fragment the network.
* **Closeness Centrality:** `person_8` has the highest closeness centrality, meaning they are, on average, closest to all other people in the network.  Information reaches them quickly, and they can likely disseminate it quickly too.  `person_23` and `person_21` are also relatively close to everyone.
* **Eigenvector Centrality:** `person_21` and `person_8` have the highest eigenvector centrality. This metric is about *influence* – being connected to other well-connected people. These individuals aren’t just connected; they’re connected to the *right* people, amplifying their influence.



**Actionable Insights & Recommendations:**

1. **Leverage Key Connectors:** Focus on nurturing relationships with `person_23`, `person_19`, `person_21` and `person_8`. They are the backbone of your network.  Engage them in important communications and initiatives.
2. **Encourage Triadic Closure:**  The low clustering coefficient suggests opportunities to strengthen connections *between* the people connected *to* your central figures.  Facilitate interactions between their connections. For example, if `person_21` is connected to `person_A` and `person_B`, find opportunities for `person_A` and `person_B` to connect with each other. This builds resilience and strengthens the network.
3. **Consider Network Expansion (Strategically):** While your network is currently well-connected, increasing density further could make it even more robust.  However, don’t just add people randomly.  Think about *who* would be valuable additions and *how* they would connect to existing members. Focus on bridging any gaps or connecting disparate parts of the network.
4. **Monitor Key Individuals:**  Pay attention to the activity and engagement of `person_23` and `person_19` (high betweenness). If they become less active, the network’s efficiency could suffer.
5. **Assess the Purpose of the Network:** What is the primary function of this network? Is it for information sharing, collaboration, support, or something else? Understanding its purpose will help you tailor your efforts to strengthen the connections that matter most for achieving your goals.




**Notable Patterns/Anomalies:**

* **Convergence of Leaders:** Notice how `person_23`, `person_19`, `person_21`, and `person_8` consistently appear high in multiple centrality measures. This suggests they play multifaceted roles in the network, acting as both direct connectors *and* bridges/influencers.  This is a strong and healthy pattern.
* **Relatively Low Clustering:** The clustering coefficient is a bit low. This isn’t necessarily *bad*, but it suggests the network is more like a collection of individuals linked by a few key people, rather than several tightly-knit groups.



In conclusion, your network is reasonably well-connected, with a strong core group of individuals who play crucial roles. By focusing on nurturing these key relationships and fostering more connections between their contacts, you can further strengthen the network and make it even more resilient and effective.  Let me know if you’d like me to explore any of these findings in more detail!
📊 Key Metrics: {'nodes': 25, 'edges': 42, 'density': 0.14}

📊 Query 4: Which person would cause the most disruption if they left the network?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis to answer your question about who would cause the most disruption if they left the network, based on the provided social network analysis results.

**1. Direct Answer: Person 1 appears to be the most critical node and would likely cause the most disruption if they left the network.**

**2. Explanation of Relevant Findings:**

Let's break down what these metrics mean in plain language:

* **Nodes & Edges:** You have a network of 25 people (nodes) with 42 connections (edges) between them.
* **Density (0.14):** This tells us how connected the network is overall. A density of 0.14 is relatively low, meaning there's potential for more connections to be made, and the network isn't incredibly tightly knit.
* **Connected Components (2):** This is important. It means your network isn't *fully* connected. There are two separate "islands" of people.  If a crucial connector between these islands left, it could isolate a portion of the network.
* **Degree Centrality:** This measures how many direct connections a person has.  The top five – Person 1, 14, 19, 21, and 23 – are the most directly connected individuals.
* **Betweenness Centrality:**  This measures how often a person lies *on the shortest path* between other people in the network.  High betweenness means this person is a key connector – removing them would force others to find longer routes to communicate or collaborate.
* **Closeness Centrality:** This measures how quickly a person can reach everyone else in the network.  Higher closeness means information flows through this person more efficiently.
* **Eigenvector Centrality:** This measures a person's influence based on the influence of *their* connections. It's a measure of prestige – being connected to other well-connected people boosts your score.

**3. Context & Interpretation:**

While several people show up as "leaders" in different centrality measures, **Person 1 consistently ranks high across *multiple* key metrics: Degree, Betweenness, Closeness, and Eigenvector.**  This is a very strong indication of their importance.

* **Person 1 isn’t just popular (high degree); they actively bridge connections (high betweenness) and can quickly reach others (high closeness).**  Their connections are also influential (high eigenvector), suggesting they're connected to other key players.
* **The fact that the network has two connected components** means the person linking those components is extra valuable. If Person 1 is bridging that gap, their loss would be especially significant.
* **Person 14, 19, 21 & 23** are also important, but their influence seems more focused on direct connections or prestige, rather than being a fundamental connector within the entire network. They might be specialized knowledge holders or team leads within smaller groups.
* **Low Clustering Coefficient (0.0732):** This means people in the network aren't particularly well-connected to *each other’s* connections.  Removing a key connector like Person 1 will likely have a more noticeable effect because there aren't strong alternative pathways for communication.

**4. Actionable Insights & Recommendations:**

* **Risk Mitigation:**  Identify what roles and responsibilities Person 1 fulfills.  Document their knowledge, key relationships, and decision-making processes.
* **Knowledge Transfer:** If Person 1 were to leave, having documented information would be invaluable.
* **Relationship Building:** Encourage the development of strong secondary connections around Person 1.  Can others step up to fill some of their bridging roles?
* **Succession Planning:**  If Person 1 is in a critical role, identify and mentor potential successors.
* **Strengthen Network Ties:**  Look for opportunities to facilitate connections *between* different parts of the network to reduce reliance on single individuals. Consider team-building activities or cross-departmental projects.
* **Monitor Key Connectors:** Regularly re-run this analysis to track changes in network structure and identify emerging leaders.



**5. Notable Patterns/Anomalies:**

* **The combination of high scores across multiple centrality measures for Person 1 is the most significant pattern.** It’s rare to see one person consistently ranked highly in Degree, Betweenness, Closeness, and Eigenvector.
* **The low clustering coefficient** emphasizes the reliance on a few key connectors.  A more robust network would have more alternative pathways for information flow.  



In conclusion, while several individuals are important, Person 1's centrality across multiple metrics suggests they are the most critical node in your network. Focus on understanding their role and building redundancy to mitigate the risk of disruption if they were to leave. Remember that social network analysis is a snapshot in time, so regular monitoring is key to maintaining a healthy and resilient network.
📊 Key Metrics: {'nodes': 25, 'edges': 42, 'density': 0.14}

============================================================
DEMO 2: Analysis with Custom Network
============================================================
🏗️  Creating custom organizational network...

📊 Query 1: Who has the most influence in this organization?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, let's break down who has the most influence in this organization based on your network analysis.

**1. Direct Answer: Frank appears to be the most influential person in this organization.**

However, it's *not* a simple answer, and we need to look at *how* influence is measured to understand why. Frank consistently ranks highly across multiple centrality measures, suggesting a robust and multifaceted influence.

**2. Explaining the Findings (in accessible terms):**

We used several different ways to measure influence within this network. Think of it like looking at a person from multiple angles:

* **Degree Centrality:**  This measures how *connected* someone is – how many direct ties they have.  Frank and Alice, Charlie, Eve, and Grace have the highest degree, meaning they interact directly with a lot of other people.  This is a good starting point for identifying influence, as it shows who's actively involved.
* **Betweenness Centrality:**  This measures how often someone acts as a *bridge* between other people.  High betweenness means that information frequently flows *through* that person. Grace and Frank are the key bridges, controlling information flow and potentially having a significant impact on how the organization functions.
* **Closeness Centrality:** This measures how quickly someone can reach everyone else in the network.  Frank and Grace have the highest closeness, meaning they can disseminate information (or receive it) quickly and efficiently. They’re well-positioned to be aware of what’s happening across the whole group.
* **Eigenvector Centrality:** This is a measure of influence based on the influence of your connections. It's not just *how many* connections you have, but *who* you're connected to. Being connected to other highly connected people boosts your own score. Frank has the highest Eigenvector score, indicating he’s connected to the ‘right’ people, and his connections amplify his influence.

**3. Context and Interpretation:**

Your network has a relatively high density (0.3929). This means there are a good number of connections within the group, suggesting a fairly collaborative environment.  The fact that you have one connected component and all 8 people are part of it indicates good overall communication.

However, the consistent high ranking of Frank across multiple centrality measures is significant.  He’s not just popular (high degree), he's a key information broker (high betweenness), he’s efficient at reaching everyone (high closeness), and he’s connected to influential people (high eigenvector). This paints a picture of someone who’s genuinely central to how the organization operates.

Grace is also consistently high ranking, particularly in betweenness and closeness. This makes her a very important secondary influencer and a critical communication channel.

**4. Actionable Insights & Recommendations:**

* **Leverage Frank and Grace:** If you want to implement change, gain buy-in for a new idea, or disseminate important information, involving Frank and Grace is crucial. They are the most likely to ensure the message reaches everyone and is well-received.
* **Don’t Neglect Alice, Charlie, and Eve:**  These individuals also have high degree centrality and should be kept engaged. They are active connectors in their own right.
* **Consider Developing Bob, Henry, and Diana:** These individuals have comparatively lower centrality scores. While not necessarily 'weak' links, they may be more peripheral in information flow. Consider ways to integrate them more fully into key conversations and projects, fostering their connections. This isn't about giving them power, but ensuring inclusivity and potentially uncovering untapped perspectives.
* **Monitor Grace:** Grace is highly influential in communication and bridging gaps. While powerful, be mindful of ensuring she isn’t becoming a bottleneck or inadvertently controlling information.

**5. Notable Patterns & Anomalies:**

* **The dominance of Frank:** While other people have high scores in certain areas, Frank consistently appears in the top rankings across multiple measures. This is the most striking pattern.
* **The cluster of high-degree individuals:** Alice, Charlie, Eve, and Grace are all relatively close in degree centrality, forming a core group of actively connected people. This suggests a tightly knit subgroup within the larger network.
* **Eigenvector Centrality difference:** Frank scores significantly higher on Eigenvector Centrality than Grace, Alice, Charlie, and Eve. This suggests Frank’s connections are more impactful than those of others, solidifying his position as a key influencer.



In conclusion, while a network is complex, this analysis strongly suggests Frank is the most influential person in this organization. However, influence isn’t solely about one person; understanding the roles of Grace, Alice, Charlie, and Eve, and nurturing the connections of Bob, Henry, and Diana, will be vital for continued success.

📊 Query 2: What departments or groups can you identify?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis of your social network, focusing on identifying potential departments or groups, based on the provided results.

**1. Direct Answer: Identifying Departments/Groups**

Based on the network analysis, it appears there's a core, tightly-knit group consisting of Frank, Alice, Charlie, and Eve.  Grace and Frank act as important bridges connecting this core to Bob, Henry, and Diana. While the network is fully connected (everyone is reachable from everyone else), the centrality measures suggest a natural division – a more central, influential 'inner circle' and a slightly more peripheral group.  We can tentatively identify two groups: a **Core Group (Frank, Alice, Charlie, Eve)** and a **Connector/Outreach Group (Grace, Bob, Henry, Diana)**.

**2. Explanation of Relevant Findings (Accessible Terms)**

Let's break down what the numbers mean, and why they point to these groupings:

* **Density (0.3929):**  This means about 39% of *all possible* connections within your network actually exist. It’s a moderate density – the network isn’t sparse, but isn’t fully interconnected either. This suggests a balance between focused connections and broader outreach.
* **Connected Components (1) & Largest Component Size (8):**  This is good! It means everyone in the network *is* connected to everyone else, directly or indirectly.  There are no isolated individuals.
* **Clustering Coefficient (0.5714):** This is relatively high. It indicates a strong tendency for your contacts to be connected to *each other*.  Think of it as 'friend of a friend' connections – there's a lot of overlap. This reinforces the idea of a closely-knit group.
* **Degree Centrality:** This measures how many direct connections each person has. Frank and Alice have the highest degree, meaning they are directly connected to the most people. This makes them key players in the network.
* **Betweenness Centrality:** This is crucial for identifying ‘bridges’ or ‘gatekeepers’. Grace and Frank have the highest betweenness, meaning they lie on many of the shortest paths between other people in the network. If you want information to flow through the network, these individuals are vital.
* **Closeness Centrality:** This measures how quickly someone can reach all other people in the network. Frank and Grace are the most central in this respect, meaning they can quickly disseminate information.
* **Eigenvector Centrality:** This is a measure of influence. It considers not just *how many* connections you have, but *who* you’re connected to.  Frank, Alice, Charlie, and Eve have the highest eigenvector centrality, suggesting they are the most influential members of the network.

**3. Context & Interpretation**

The centrality metrics collectively tell a story. The Core Group (Frank, Alice, Charlie, Eve) are highly interconnected, influential, and centrally located within the network. They seem to form the primary hub of information and influence. Grace acts as a crucial link *between* this core and the remaining members (Bob, Henry, and Diana). Bob, Henry, and Diana, while connected, have lower centrality scores, suggesting they may rely more on Grace to connect them to the inner circle.

**4. Actionable Insights & Recommendations**

* **Communication Strategy:** When disseminating important information, *always* include Frank and Grace. They are the most effective channels for reaching the entire network.  Prioritize communication *through* them, rather than trying to reach everyone individually.
* **Knowledge Sharing:** Encourage more direct interaction and knowledge sharing *within* the Core Group (Frank, Alice, Charlie, Eve). They are a valuable source of expertise and can amplify each other's impact.
* **Engagement with Peripheral Members:** Focus on strengthening the connection between Grace and Bob, Henry, and Diana. Ensure these members feel included and have access to information. Perhaps Grace could facilitate regular check-ins or act as a mentor.  Consider if they are getting adequate support.
* **Leverage Grace's Bridging Role:** Recognize Grace's importance as a connector. Give her opportunities to facilitate collaboration between different parts of the network.
* **Monitor Changes:** Regularly re-run this analysis to see if the network structure shifts.  Changes in centrality scores could indicate evolving relationships or influence patterns.

**5. Notable Patterns & Anomalies**

* **Grace's Dual Role:** Grace is interesting. She has high betweenness and closeness, indicating a strong bridging role, but her eigenvector centrality is lower than the core group. This suggests she's excellent at *connecting* people but might not be as influential in shaping opinions *within* the core.
* **Bob, Henry, & Diana's Dependence:** These individuals have consistently lower centrality scores. It's worth investigating *why*. Are they new to the network? Do they have different roles or priorities? Understanding their perspective is important.
* **Relatively Even Distribution of Degree:** While Frank has the highest degree, it's not dramatically higher than others. This suggests a fairly egalitarian network where many people have a reasonable number of connections.



In conclusion, your network appears healthy and relatively well-connected. By understanding the roles and influence of different members, you can optimize communication, foster collaboration, and ensure that everyone feels engaged and informed.  Remember that this is a snapshot in time; ongoing analysis will provide valuable insights into evolving dynamics.

📊 Query 3: How would losing Frank affect the organization?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis of how losing Frank would affect your organization, based on the social network analysis results.

**1. Direct Answer to Your Question: How would losing Frank affect the organization?**

Losing Frank would be significantly disruptive. He appears to be a *critical connector* within your organization. Removing him would likely decrease communication flow, potentially impacting efficiency and collaboration. While the network wouldn't fracture into isolated groups (it's currently fully connected), it *would* become more reliant on other individuals to fill the gaps Frank currently occupies, and those individuals might not have the same breadth of connection.  You’d likely see a decrease in overall network efficiency and potentially slower information dissemination.

**2. Explaining the Relevant Findings (Accessible Terms)**

Let's break down what these metrics mean in a way that's easy to understand:

* **Nodes & Edges:** You have 8 people (nodes) and 11 connections (edges) between them. This is a relatively small network, making each connection quite important.
* **Density (0.3929):** This tells us how interconnected the network is. A density of 0.39 is moderate - meaning roughly 39% of all possible connections *actually* exist. It's not a highly dense network, so each connection is valuable.
* **Connected Components (1):**  Great news! Everyone is connected to everyone else, directly or indirectly. Losing a person doesn’t immediately split the organization into isolated groups.
* **Degree Centrality:** This simply counts how many direct connections a person has. Frank and Alice, Charlie, Eve and Grace have the highest degree centrality. Frank has a slight lead, indicating he’s directly connected to more people than anyone else.
* **Betweenness Centrality:** This is *crucial* for understanding Frank's importance. It measures how often a person lies *on the shortest path* between two other people.  High betweenness means that person acts as a bridge. Grace and Frank have the highest scores here. Frank is a key connector, controlling information flow between different parts of the network. Removing him means others will have to take detours to communicate, increasing the risk of delays or miscommunication.
* **Closeness Centrality:** This measures how quickly someone can reach everyone else in the network. Frank and Grace have the highest scores, meaning they can efficiently disseminate information or receive it from others. 
* **Eigenvector Centrality:** This goes beyond simple counts and considers the *quality* of connections. Being connected to well-connected people boosts your eigenvector score. Frank has the highest score here, meaning he’s connected to the *most influential* people in the network.



**3. Context and Interpretation of the Results**

Frank isn’t just *a* connector; he’s *the* central connector in this network. His high scores across *multiple* centrality measures (Degree, Betweenness, Eigenvector, and Closeness) confirm this.  He's not just connecting to many people (Degree), he's a vital bridge for communication (Betweenness), he can reach others quickly (Closeness), and he's connected to the most influential people (Eigenvector).  

Grace is also a very important node, scoring highly in Betweenness and Closeness, suggesting she's also a significant connector and information disseminator. She would likely be the *primary* person to absorb some of Frank's responsibilities, but she’d be stretched thin.

The other nodes (Alice, Charlie, Eve) have relatively similar profiles, and while important, don’t display the same level of overarching connectivity as Frank and Grace. Bob, Henry and Diana have lower centrality scores, indicating they are more peripheral members of the network.



**4. Actionable Insights and Recommendations**

* **Succession Planning:**  If Frank is considering leaving or there's a risk of losing him, *immediately* start succession planning.  Identify someone (or a team) to take on his bridging role.  
* **Knowledge Transfer:** If Frank *is* leaving, prioritize intensive knowledge transfer.  Document his processes, key relationships, and any unspoken knowledge he holds.
* **Strengthen Grace's Network:** Invest in Grace’s professional development and provide her with support and resources to manage the increased workload.
* **Build Redundancy:**  Proactively encourage more connections between Alice, Charlie and Eve.  Facilitate cross-functional projects and meetings to build relationships outside of their immediate teams.
* **Monitor the Network:**  After Frank's departure (or if he leaves), *re-run* this social network analysis to see how the network has changed and identify any new bottlenecks.
* **Consider a “Connector” Role:** If the organization is growing, consider formally defining and supporting “connector” roles to facilitate communication and collaboration.




**5. Notable Patterns and Anomalies**

* **Centralized Network:** This network is relatively centralized around Frank and Grace. While not necessarily *bad*, it does mean the organization is somewhat reliant on a few key individuals. Diversifying connections is important.
* **Peripheral Nodes:** Bob, Henry and Diana have lower centrality. Understanding their roles and how they contribute to the organization is important, and ensuring they aren't overlooked in communication is advisable. This isn’t necessarily a problem; they may fulfill specialized roles that don’t require broad network connectivity.



**In conclusion:** Losing Frank would be a significant disruption. Proactive planning, knowledge transfer, and a focus on building a more resilient and distributed network will be crucial to mitigate the impact and ensure the organization continues to function effectively.  Don’t underestimate the importance of this role – it's not just about *who* Frank knows, but *how* he connects the organization.

📊 Query 4: Who are the key connectors between different groups?
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis addressing your question about who the key connectors are within your social network, based on the provided data.

**1. Direct Answer: Who are the key connectors?**

Based on this network analysis, **Grace and Frank** are the key connectors between different parts of your network. While several individuals have high scores on certain centrality measures, Grace and Frank consistently appear in the top positions across multiple measures, signifying their broad influence and bridging role.

**2. Explaining the Relevant Findings**

Let's break down what these centrality measures tell us and why Grace and Frank stand out:

* **Degree Centrality:** This measures how many direct connections a person has. Frank and Alice, Charlie, Eve and Grace all have relatively high degree centrality, meaning they're directly connected to a significant portion of the network.  However, *direct* connections don’t necessarily mean they're bridging *different* groups.
* **Betweenness Centrality:** *This is crucial for your question*. It measures how often a person lies on the *shortest path* between two other people. A high betweenness score means this person is a key link – if they were removed, it would disrupt communication between others.  **Grace has the highest betweenness centrality**, followed closely by Frank. This means Grace and Frank are frequently the *only* way certain people can connect with each other in the network.
* **Closeness Centrality:** This measures how quickly someone can reach everyone else in the network. Frank and Grace have the highest closeness, meaning they can efficiently disseminate information or influence the entire network.
* **Eigenvector Centrality:** This measures influence based on the influence of your connections.  Being connected to other well-connected people boosts your eigenvector score. Frank has the highest eigenvector score, indicating he’s connected to, and influenced by, the most influential people in the network.

**3. Context and Interpretation of the Results**

* **Small, Dense Network:**  You have a relatively small network (8 nodes) with a surprisingly high density (0.3929). This means a substantial proportion of possible connections *actually exist*. It suggests a cohesive group where people are well-connected to each other.
* **Single Connected Component:** The fact that you have only one connected component and it includes all 8 nodes is positive. It signifies a unified network where everyone can reach everyone else – directly or indirectly.
* **Grace and Frank as Bridges:**  Grace's high betweenness score means she’s literally *between* different subgroups. Information and influence flow *through* her.  Frank also serves as a key connector but is also high on eigenvector centrality. This indicates Frank’s connections are influential and he’s a prominent figure in the network.
* **Alice, Charlie, and Eve:** While having relatively high degree centrality, these individuals don't appear as prominently in betweenness or closeness. This suggests they are well-connected within their immediate circles but perhaps less involved in bridging different parts of the network.
* **Bob, Henry, and Diana:** These nodes have lower centrality scores across the board. This doesn't necessarily mean they're unimportant, but they are less central to the overall flow of information and influence within the network.



**4. Actionable Insights and Recommendations**

* **Leverage Grace and Frank:** If you want to disseminate information quickly and effectively, or to build consensus across the network, involve Grace and Frank. They are the most likely to reach everyone and to influence opinions.  They’re key for initiatives requiring broad participation.
* **Strengthen Connections Around Bob, Henry, and Diana:** Consider ways to integrate Bob, Henry, and Diana more fully into the network. Perhaps facilitate introductions to other key players or involve them in collaborative projects.  This could make the network even more robust.
* **Monitor Grace:** Because Grace is so central, her engagement and well-being are critical. If she becomes unavailable or disengaged, it could significantly disrupt network communication. Consider having a backup person who can fill a similar bridging role.
* **Identify Subgroups (Further Analysis):** While this analysis shows *who* connects, it doesn't reveal *what* the groups are. Further investigation into the nature of the relationships (e.g., work colleagues, family friends, shared interests) could reveal the specific groups being bridged and help refine your strategies.



**5. Notable Patterns & Anomalies**

The strong cohesion of this network is the most notable pattern. The high density suggests a tight-knit group.  There aren’t any particularly “isolated” nodes. However, the relatively low betweenness scores for Alice, Charlie, and Eve, despite having high degree centrality, suggests they may be focused on maintaining strong ties *within* their immediate circles, rather than *across* different groups.

**In conclusion:** This network analysis provides a valuable snapshot of your social connections. By understanding who the key connectors are and how information flows, you can make more informed decisions about how to leverage your network to achieve your goals.  Remember that this is a static picture, and relationships evolve over time, so periodic re-analysis is beneficial.

============================================================
DEMO 3: Specific Analysis Types
============================================================

📊 Specific Analysis 1: Analyze the robustness of this network
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive analysis of the robustness of your social network, based on the provided data.

**1. Answering the Question: How Robust is Your Network?**

Overall, your network appears moderately robust, but with some vulnerabilities. It's a relatively small, tightly connected network, which is good. However, the centrality metrics reveal a dependence on a few key individuals. Removing those individuals could significantly disrupt information flow and network cohesion.  We’ll delve into *why* with the following analysis.

**2. Explaining the Findings (in Accessible Terms)**

Let's break down what these network metrics mean for robustness:

* **Density (0.3929):** This means about 39% of all possible connections *within* your network actually exist. This is a reasonable density, suggesting a fairly connected group. Higher density generally means greater robustness because there are more alternative paths for information to travel.

* **Connected Components (1) & Largest Component Size (8):**  Excellent! Having one connected component means everyone in the network *can* reach everyone else, directly or indirectly.  The largest component size matching the total number of nodes confirms this full connectivity. This is a strong indicator of robustness – no isolated individuals or subgroups.

* **Clustering Coefficient (0.5714):** This is a good sign. It means that if two people are connected to the same person, there's a 57% chance they are also connected to *each other*. This indicates a strong degree of 'friend of a friend' connections, creating redundancy and resilience. If one connection is lost, alternative connections are likely to exist through mutual friends.

* **Centrality Measures – Where Vulnerabilities Lie:** This is where things get interesting. Centrality measures tell us *who* is important in the network. Different measures highlight different kinds of importance, and thus, different vulnerabilities:

    * **Degree Centrality:**  Frank has the highest degree (57%), meaning they have the most direct connections.  Alice, Charlie, Eve and Grace are also relatively high. Losing Frank would remove a lot of direct links. Removing any of the high-degree individuals would have a noticeable impact.

    * **Betweenness Centrality:**  Grace and Frank have significantly higher betweenness centrality. This means they lie on many of the *shortest paths* between other people in the network. They act as crucial bridges. If Grace or Frank were removed, communication between various parts of the network would be severely disrupted and would need to take longer, less efficient paths. Bob, Henry and Diana have very low betweenness meaning they are not critical to connecting other individuals.

    * **Closeness Centrality:**  Frank and Grace have the highest closeness centrality, meaning they can reach all other individuals in the network quickly. Again, these two are pivotal in fast information dissemination. 

    * **Eigenvector Centrality:** Frank and Alice/Charlie/Eve have the highest eigenvector centrality. This measures influence – being connected to other *important* people. Frank is the most influential, and the others have similar levels, indicating a core group who are particularly well-connected to other key individuals. Grace has a much lower score, suggesting less influence within this network.



**3. Context and Interpretation**

Your network isn’t *fragile*, but it isn’t highly robust either. It relies heavily on Frank and Grace.  If those two individuals were to become unavailable (leave the network, become inactive, etc.), the network's ability to function efficiently would be significantly hampered.  

The relatively high clustering coefficient helps mitigate some of this risk, as information *could* still flow through alternative paths via mutual connections. However, it would likely be slower and less efficient.  

Bob, Henry, and Diana appear to be more peripheral members. Their removal would have a much smaller impact on overall network connectivity.

**4. Actionable Insights and Recommendations**

Here's what you can do to improve network robustness:

* **Reduce Reliance on Frank and Grace:**  This is the most important step. Encourage other members to build more connections *between* different parts of the network. Specifically, encourage Alice, Charlie, and Eve to connect more with Bob, Henry, and Diana. This would create more redundancy and lessen the impact if Frank or Grace were unavailable.
* **Foster Connections Between Peripheral Members:** Strengthen links between Bob, Henry, and Diana. This will make them less reliant on Frank/Grace to communicate with others and increase overall network resilience.
* **Encourage Diverse Connections:**  Don't let connections be concentrated within subgroups.  Promote interaction and relationship-building across different segments of the network.
* **Monitor Changes:** Regularly reassess the network structure. If key individuals become inactive or leave, be proactive in strengthening connections elsewhere.
* **Consider Redundancy:**  If this network represents critical functions (e.g., a project team, a support network), consider building in redundancy.  For example, train multiple people to perform key tasks.



**5. Notable Patterns & Anomalies**

* **Clear Core Group:**  Frank, Alice, Charlie, and Eve form a core group with high centrality across multiple measures. This is not necessarily *bad*, but it does create a potential bottleneck.
* **Peripheral Members:** Bob, Henry, and Diana are relatively isolated. Strengthening their connections is a key area for improvement.
* **Grace’s Importance:** Grace is particularly critical based on Betweenness and Closeness centrality. While Frank has more direct connections (degree), Grace seems to act as a critical bridge for efficient communication.



In conclusion, your network is reasonably well-connected, but a small number of individuals are disproportionately important. By proactively addressing this dependence, you can significantly improve its robustness and ensure its long-term viability. Let me know if you would like me to elaborate on any of these points or perform further analysis.

📊 Specific Analysis 2: Find the shortest path between any two people
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a comprehensive response to your question about finding the shortest path between any two people in your network, based on the social network analysis results:

## Finding Shortest Paths & Understanding Your Network

You asked about finding the shortest path between any two people.  Based on the analysis, since your network has only 8 people and is *fully connected* (meaning there’s a path between *everyone*), the shortest path between *any* two people is likely to be **a direct connection (1 step) or a connection through just one other person (2 steps)**.  The analysis confirms this, with a relatively high density (0.3929) and a single, large connected component.  Let's break down what this means and how to interpret the results to understand *who* bridges connections and how information flows.

**1. What the Analysis Tells Us:**

* **Network Size:** You have a small network of 8 individuals.
* **Density (0.3929):** This is a moderate density. It means that about 39.29% of all possible connections between people *actually exist*. This suggests a fairly well-connected group, though not *completely* dense (a fully dense network would have a density of 1).
* **Connected Components (1):**  This is excellent!  It means everyone in your network is reachable from everyone else. There aren’t isolated subgroups.
* **Largest Component Size (8):**  Confirms everyone is part of the same network.
* **Centrality Measures:** These tell us who the most important individuals are in different ways. We’ll explore these in detail below.



**2. Understanding Centrality – Who Bridges the Gaps?**

The centrality measures are crucial for understanding shortest paths and influence.  Here's a breakdown of each, and how they relate to your question:

*   **Degree Centrality:** This measures how many direct connections someone has.  
    *   **Frank** has the highest degree centrality (0.5714).  This means Frank is connected to the most people directly.  If you want to quickly disseminate information, Frank is a good starting point.  
    *   **Alice, Charlie, Eve, and Grace** are also relatively high in degree centrality.
*   **Betweenness Centrality:** This measures how often someone lies *on the shortest path* between two other people.  High betweenness means this person is a key connector, controlling information flow.
    *   **Grace** has the highest betweenness centrality (0.5952). This is *very* significant. Grace is a critical bridge. If Grace were removed from the network, it would significantly disrupt communication between others.
    *   **Frank** is also a high betweenness node.
    *   **Bob, Henry, and Diana** have very low betweenness, meaning they aren't as frequently used as connectors.
*   **Closeness Centrality:** This measures how quickly someone can reach everyone else in the network.  A high closeness score means information can reach this person and then spread quickly to others.
    *   **Frank and Grace** have the highest closeness centrality.  They can reach everyone else in the network relatively quickly.
    *   **Alice, Bob, and Charlie** have lower closeness.
*   **Eigenvector Centrality:** This measures influence – who is connected to *other* influential people.  It’s about quality of connections, not just quantity.
    *   **Frank** has the highest eigenvector centrality. He’s connected to other well-connected people, making him a strong influencer.
    *   **Alice, Charlie, and Eve** are also highly ranked, indicating they are connected to influential members.



**3. Actionable Insights & Recommendations:**

*   **For Quick Communication:**  Start with **Frank** or **Grace**. They have the most direct connections, high closeness, and significant betweenness.
*   **To Understand Information Flow:** Focus on **Grace**. She is the key connector between many people. Information likely passes *through* Grace frequently. If you want to understand how ideas spread, observe Grace’s interactions.
*   **Engage Peripheral Members:** **Bob, Henry, and Diana** have lower centrality.  Consider ways to integrate them more fully into the network.  Perhaps include them in important conversations or projects. This will strengthen the network as a whole and can help spread information more broadly.
*   **Strengthen Key Connections:**  The connections between **Frank and Grace** are particularly important.  Nurturing this relationship will enhance network resilience.
*   **Identify Potential Bottlenecks:** Since Grace has such high betweenness, relying solely on her to transmit information could be a bottleneck.  Consider identifying secondary connectors to distribute the load.

**4. Notable Patterns & Anomalies:**

*   **Frank & Grace Dominate:** Frank and Grace consistently rank high across multiple centrality measures, highlighting their central roles.
*   **Low Centrality of Bob, Henry, & Diana:** These individuals are less integrated into the core of the network. While this doesn't necessarily indicate a problem, it’s worth noting and considering how to include them more.
*   **Consistency of Centrality:** The ranking of the individuals are fairly consistent across measures. This indicates relatively clear roles within the network.



**In conclusion,** finding the shortest path in your network is relatively straightforward given its size and connectivity. However, understanding *who* plays a key role in those paths – especially Grace and Frank – is crucial for effective communication, influence, and network health.  By focusing on strengthening key connections and integrating peripheral members, you can optimize your network for success.

📊 Specific Analysis 3: Show me the neighborhood analysis for a central person
--------------------------------------------------
📈 Analysis Type: basic_metrics
🤖 AI Insights:
Okay, here's a neighborhood analysis for a central person in your network, based on the results you provided. I'll focus on Frank, as they consistently appear at or near the top across multiple centrality measures.

**1. Answering the Question: Neighborhood Analysis for Frank**

To understand Frank’s influence, let's examine their immediate neighborhood – the people directly connected to them. Based on the analysis, Frank is connected to (we need the edge list to confirm, but we can infer based on the degree centrality): Alice, Charlie, Eve, and Grace.  Let's analyze what this tells us about Frank’s position and influence.

**2. Explaining the Relevant Findings**

* **High Centrality Scores:** Frank consistently ranks high in Degree, Closeness, and Eigenvector Centrality. This suggests Frank isn’t just *connected* to many people (Degree), but is also strategically positioned to efficiently reach others in the network (Closeness) and is connected to other important people (Eigenvector).
* **Degree Centrality:** A degree centrality of 0.5714 means Frank is connected to a majority of the people in this network (57.14% of the other 7 nodes).
* **Betweenness Centrality:**  Frank also has a relatively high Betweenness centrality (0.5714). This means Frank lies on many of the shortest paths between other people in the network.  Information or influence frequently *flows through* Frank.
* **Neighborhood Composition:** Frank's direct connections (Alice, Charlie, Eve, and Grace) are *also* fairly central people themselves – they all have non-negligible centrality scores. This is crucial – Frank isn't just connected to *anyone*; they are connected to *other influential nodes*.

**3. Context and Interpretation**

This network appears to be relatively small (8 nodes) and quite interconnected (density of 0.3929 is fairly high for many networks).  The fact that the entire network is one connected component reinforces this.  Frank is a key connector *within* this strongly linked group.  

Think of it like this: if you wanted to get a message from Bob to Diana, a significant number of the shortest routes likely pass *through* Frank.  This makes Frank a potential gatekeeper of information and influence.  The fact that Frank's neighbors are also central amplifies this – they can help distribute information *from* Frank, and also act as backups if Frank were unavailable.

**4. Actionable Insights & Recommendations**

* **Leverage Frank for Communication:** If you want to disseminate information quickly and efficiently across the network, going through Frank is a smart strategy. They can reach a large portion of the network directly and indirectly.
* **Relationship Building with Frank's Neighbors:** Strengthening relationships with Alice, Charlie, Eve, and Grace is important. They amplify Frank’s influence and can act as alternative channels for communication. Cultivating these connections creates redundancy and resilience in your communication network.
* **Understand Frank’s Motivations:**  Because Frank is so central, understanding their goals and perspectives is critical. They have a lot of power within the network and can significantly influence outcomes.
* **Monitor Frank's Activity:**  Keep an eye on what Frank is doing and who they are interacting with.  Changes in their behavior could signal shifts in the network dynamics.
* **Consider Frank a Key Advocate or Champion:**  If you're trying to promote an idea or initiative, Frank is a valuable person to get on board. Their endorsement could significantly increase its chances of success.

**5. Notable Patterns & Anomalies**

* **Grace as a Secondary Connector:** Grace has the second highest closeness and betweenness centrality scores, placing her as a significant connector alongside Frank. This suggests a potential 'power couple' dynamic within the network, where both individuals play crucial roles. Further investigation of their relationship could be insightful.
* **Bob, Henry, and Diana are Peripheral:** Bob, Henry, and Diana have relatively low centrality scores. This means they are more peripheral to the network's core. While not necessarily a problem, it's worth considering how to better integrate them if increased participation is desired. Their connection to the core is likely through Frank and Grace.
* **Homophily:** It's likely that Frank’s connections (Alice, Charlie, Eve, Grace) share similar characteristics or interests. Further data on node attributes (e.g., department, interests) would confirm this, but it's a common pattern in social networks.



**To take this analysis further, it would be beneficial to:**

* **See the edge list:** Knowing *exactly* who is connected to whom is crucial for a precise interpretation.
* **Add Node Attributes:** Information about the individuals (e.g., their roles, departments, interests) would provide valuable context.
* **Examine Network Evolution:** How has the network changed over time? This would reveal trends and potential emerging patterns.



I hope this in-depth analysis is helpful! Let me know if you have any other questions or would like me to explore a specific aspect of your network in more detail.

============================================================
DETAILED METRICS DEMONSTRATION
============================================================
📊 Generated network with 30 nodes and 47 edges

🔢 Calculating comprehensive metrics...

📈 NETWORK OVERVIEW:
   • Nodes: 30
   • Edges: 47
   • Density: 0.1080
   • Connected Components: 1
   • Largest Component: 30
   • Clustering Coefficient: 0.0726
   
🎯 TOP 3 MOST CENTRAL NODES:
   • Degree: [('person_0', 0.10344827586206896), ('person_1', 0.13793103448275862), ('person_2', 0.1724137931034483)]
   • Betweenness: [('person_7', 0.2521346469622332), ('person_6', 0.18247126436781616), ('person_5', 0.17844827586206896)]
   • Closeness: [('person_7', 0.4393939393939394), ('person_6', 0.4264705882352941), ('person_26', 0.4264705882352941)]
    
🏘️  Detecting communities...
   Found 5 communities
   Community sizes: [7, 7, 7, 5, 4]

🛡️  Analyzing network robustness...
   Original connectivity: {'components': 1, 'largest_component': 30}
   Critical nodes identified: 3

🎉 Demo completed successfully!

💡 Tips for using the agent:
   • Ask natural language questions about your social network
   • The agent automatically determines the best analysis approach
   • You can provide custom graph data or use generated samples
   • Make sure Ollama is running with the gemma2:27b model for best results