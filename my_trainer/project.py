"""Apply one of the RL algorithms (or use Tinker) for the use-case of Tree-of-Thoughts conversation optimization.

Input:
- A conversation history
- A goal

Output:
- Next response to the conversation

Methodology:
- Forecast the conversation forward using tree search and TOP_K reasoning.
- Rank the final outcome at the end of the conversation on how favorable it was to the goal.
- Use the RL algorithm to optimize the conversation.
- Return the next response to the conversation.

Also look into NemoRL and NemoGym.

Make reference to OpenAI paper https://arxiv.org/pdf/1805.00899 (AI safety via debate), which has useful language around self-play for language "games".
Also make connection to paper "Bridging the Human–AI Knowledge Gap: Concept Discovery and Transfer in AlphaZero" in terms of then how to learn most effectively
frmo this "optimal" agent.
"""
