from agent import get_response 
def startchat(): 
    memory = [] 
    while True: 
        query = input("\nUser:\n") 
        if query.lower() == "stop": 
            break 
        sep = "\n" 
        memory_text = "\n".join(memory)
        chat_template = f"{SYSTEM_PROMPT}\n\nConversation so far:\n{memory_text}\n\nUser: {query}"
        #chat_template = f"Previous conversation: {sep.join(chat for chat in memory)}\nlatest query: {query}" 
        #chat_template = f"Previous conversation: {'\n'.join(chat for chat in memory)}\nlatest query:{query}" 
        #print(chat_template) 
        response = get_response(chat_template) 
        print("response =", response) 
        memory.append(f"User: {query}\nAgent: {response}" ) 
        #memory = memory[-5:] 
        startchat()

