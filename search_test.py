from retrieve import ImageRetriever

from config import SIMILARITY_THRESHOLD

from PIL import Image


retriever = ImageRetriever()

query = input("Enter your search query: ")

results = retriever.search(query)

best_match = results["best_match"]

print("\nBest Match:\n")

print(f"Image: {best_match['id']}")

print(f"Similarity: {best_match['similarity']:.4f}")

print()


if best_match["similarity"] >= SIMILARITY_THRESHOLD:

    print("Image found in database.")

    image_path = best_match["path"]

    print(f"Opening image: {image_path}")

    image = Image.open(image_path)

    image.show()

else:

    print("No good image found.")

    print("Need to generate a new image.")