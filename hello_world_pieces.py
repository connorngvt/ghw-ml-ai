from pieces_copilot_sdk import PiecesClient

config = {
    'baseUrl': 'http://localhost:1000'
}
pieces_client = PiecesClient(config)

question = "What is the capital of Virginia?"
response = pieces_client.ask_question(question)

print(response)