from llama_cpp import Llama
from deploy.config import MODEL_PATH, CONTEXT_SIZE, THREADS

model = None

def load_model():
    global model

    if model is None:
        print("Loading GGUF model...")

        model = Llama(
            model_path=MODEL_PATH,
            n_ctx=CONTEXT_SIZE,
            n_threads=THREADS,
            verbose=False
        )

    return model