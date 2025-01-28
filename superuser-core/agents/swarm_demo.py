import ray  
from transformers import pipeline  

ray.init()  

@ray.remote  
class AnalystAgent:  
    def __init__(self):  
            self.nlp = pipeline("text-generation", model="gpt2-medium")  

                def analyze(self, prompt: str) -> str:  
                        return self.nlp(prompt, max_length=100)[0]['generated_text']  

                        @ray.remote  
                        class SecurityAgent:  
                            def check_malicious(self, text: str) -> bool:  
                                    blacklist = ["hack", "exploit", "ddos"]  
                                            return any(word in text.lower() for word in blacklist)  

                                            analyst = AnalystAgent.remote()  
                                            security = SecurityAgent.remote()  

                                            prompt = "Jak zabezpieczyć system przed atakami?"  
                                            result = ray.get(analyst.analyze.remote(prompt))  
                                            is_malicious = ray.get(security.check_malicious.remote(result))  

                                            print(f"ANALIZA: {result}")  
                                            print(f"CZY ZAGROŻENIE?: {'TAK' if is_malicious else 'NIE'}")  