import dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

dotenv.load_dotenv()

chat_history = ChatMessageHistory()
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            #Tell the AI what type of chatbot it is
            "You are chatting with a user. Answer all questions to the best of your ability."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

#Initialize the AI with the prompt
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
chain = prompt | chat

#Get a starting question
AI2response = input("What is the starting question/phrase? ")

while True:
    cantinue = input("C to continue, M to message as AI #2, or Q to quit ")
    if cantinue.lower() == "c":
        #Get the other AI's message
        Content = AI2response
    elif cantinue.lower() == "q":
         break
    elif cantinue.lower() == "m":
        #Get the user's message
        Content = input("Responding for AI #2: What do you want to say? ")
    #add the message to the chat history
    chat_history.add_user_message(Content)
    #give the message to the AI
    result = chain.invoke(
        {
            "messages":chat_history.messages
        }
    )

    print("")
    print("AI message: " +result.content)
    print("")
   
    #add the AI's message to the chat history
    chat_history.add_ai_message(result.content)