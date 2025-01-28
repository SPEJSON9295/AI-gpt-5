import requests  
from wolframalpha import Client  

class HybridAPI:  
    def __init__(self, wolfram_api_key: str):  
            self.wolfram = Client(wolfram_api_key)  

                def query(self, question: str) -> str:  
                        wolfram_res = self.wolfram.query(question)  
                                if wolfram_res.success:  
                                            return next(wolfram_res.results).text  
                                                    else:  
                                                                return "Błąd: Brak danych w Wolfram. Używam GPT..."  

                                                                hybrid_ai = HybridAPI("TWÓJ_WOLFRAM_API_KEY")  
                                                                print(hybrid_ai.query("Oblicz całkę z x^2 od 0 do 5"))  