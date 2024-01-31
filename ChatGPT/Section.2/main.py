from langchain.llms import OpenAI 


# SECURE THIS KEY!
api_key="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"

llm = OpenAI(
    openai_api_key = api_key
)

result = llm("How much dose a Tesla worker make?")
print(result)

