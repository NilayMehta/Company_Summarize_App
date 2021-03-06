import wikipedia

class Summary:
    def correctName(self,name):
        results = wikipedia.search(name,5)
        atLeastCompany=[]
        for result in results:
            try:
                for category in wikipedia.WikipediaPage(result).categories:
                    category=category.lower()
                    if "compan" in category:
                        atLeastCompany.append(result)
                    if "software" in category or "comput" in category or "internet" in category or "invest"in category:
                        return result
            except:
                print("Error")
        for company in atLeastCompany:
            return company
        return ""
    def getSummary(self,name):
        try:
            name=self.correctName(name)
            if(name==""):
                return "Company Not Found"
            s=wikipedia.summary(name, sentences=2)
            return s
        except wikipedia.exceptions.DisambiguationError as ex:
            s=wikipedia.summary(ex.args[1][0],sentences=2)
            return s

