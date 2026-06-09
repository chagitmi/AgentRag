import open_clip
import torch

from PIL import Image


class CLIPEmbeddingModel:

    def __init__(self, model_name, pretrained):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name=model_name,
            pretrained=pretrained
        )

        self.tokenizer = open_clip.get_tokenizer(model_name)

        self.model.to(self.device)

    def encode_image(self, image_path):

        image = Image.open(image_path).convert("RGB")

        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)

        with torch.no_grad():

            embedding = self.model.encode_image(image_tensor)
            embedding /= embedding.norm(dim=-1, keepdim=True)

        embedding = embedding.cpu().numpy()[0]

        return embedding.tolist()
    
    def encode_text(self, text):

        text_tokens = self.tokenizer([text]).to(self.device)

        with torch.no_grad():

            embedding = self.model.encode_text(text_tokens)
            embedding /= embedding.norm(dim=-1, keepdim=True)

        embedding = embedding.cpu().numpy()[0]

        return embedding.tolist()