def memory_agent(data):
    memory, key, value = data
    memory.set(key, value)
    print(f"[MEMORY_AGENT] Запомнил: {key} = {value}")
