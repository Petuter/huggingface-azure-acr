import gradio as gr
from transformers import pipeline

# Lade das GPT-2 Modell
generator = pipeline("text-generation", model="gpt2")

# Definiere die Funktion zur Textgenerierung
def generate_text(prompt):
    result = generator(prompt, max_length=35, num_return_sequences=1)
    return result[0]["generated_text"]

# Erstelle das Gradio-Interface
demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(label="Eingabetext", placeholder="Schreibe hier deinen Prompt..."),
    outputs=gr.Textbox(label="Generierter Text"),
    title="GPT-2 Textgenerator",
    description="Gib einen Text ein, und GPT-2 schreibt ihn weiter.",
    theme="soft"
)

# Starte die App


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)

