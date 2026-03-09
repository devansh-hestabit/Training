from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.answer_agent import AnswerAgent


class AgentPipeline:

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.summarizer_agent = SummarizerAgent()
        self.answer_agent = AnswerAgent()

    def clean_output(self, text, marker):

        if marker in text:
            return text.split(marker)[-1].strip()

        return text.strip()

    def run(self, user_query):

        print("\nUSER QUESTION:")
        print(user_query)

        research_raw = self.research_agent.research(user_query)

        research_clean = self.clean_output(
            research_raw,
            "Research Notes:"
        )

        print("\nResearch Agent Output:")
        print(research_clean)

        summary_raw = self.summarizer_agent.summarize(research_clean)

        summary_clean = self.clean_output(
            summary_raw,
            "Summary:"
        )

        print("\nSummarizer Agent Output:")
        print(summary_clean)

        answer_raw = self.answer_agent.answer(summary_clean)

        final_answer = self.clean_output(
            answer_raw,
            "Final Answer:"
        )

        print("\nFINAL ANSWER:")
        print(final_answer)


if __name__ == "__main__":

    pipeline = AgentPipeline()

    question = input("\nAsk a question: ")

    pipeline.run(question)