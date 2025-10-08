from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()


<<<<<<< HEAD
<<<<<<< HEAD
# Starte die App


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)

=======
=======
>>>>>>> parent of f190eac (In Gradio geändert)
class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return Response("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")


@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
<<<<<<< HEAD
>>>>>>> parent of f190eac (In Gradio geändert)
=======
>>>>>>> parent of f190eac (In Gradio geändert)
