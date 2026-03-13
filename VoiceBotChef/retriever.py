from rank_bm25 import BM25Okapi

class RecipeRetriever:

    def __init__(self, recipes):
        self.recipes = recipes
        tokenized = [r.lower().split() for r in recipes]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query):
        tokens = query.lower().split()
        result = self.bm25.get_top_n(tokens, self.recipes, n=1)
        return result[0]