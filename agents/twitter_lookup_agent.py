from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import OutputParserException

from langchain.agents import initialize_agent, Tool, AgentType

from decouple import Config
from tools.tools import get_profile_url

# Create a Config object
config = Config(
    "D:\VIT Material\VIT material\Courses\Langchain\Github\ice_breaker\.env"
)


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=config.get("OPENAI_API_KEY"),
    )
    template = """given the full name {name_of_person} I want you to find a link to their Twitter profile page,
                    and extract from it, their username. Your final answer should contain only the person's username."""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url,
            description="useful for when you need to get the Twitter Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    try:
        twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    except OutputParserException:
        print(
            "Sorry, but it seems like I couldn't find such a profile available through my searches!"
        )

    return twitter_username
