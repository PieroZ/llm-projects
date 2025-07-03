from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()  # optional


def generate_pet_name(animal_type, pet_color):
    llm = OllamaLLM(model="llama3.1", temperature=0.5)

    prompt_template = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template=f"I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color."
                 f" Suggest me five cool names for my pet."
    )

    chain = prompt_template | llm  # RunnableSequence

    response = chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})

    return response

if __name__ == '__main__':
    print(generate_pet_name("cow", 'black'))
