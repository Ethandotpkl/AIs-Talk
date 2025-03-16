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
            "You are a helpful assistant. Answer all questions to the best of your ability."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

#Initialize the AI with the prompt
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
chain = prompt | chat

while True:
    #Get the user's message
    Content = input("Enter a message(or Q to quit): ")
    if Content == "Q":
        break
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