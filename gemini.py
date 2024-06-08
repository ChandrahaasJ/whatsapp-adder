import google.generativeai as genai
def askgem(question):
                apikey="AIzaSyAra-xAvVrX5VGZN0h95ZBYy2jJWZ6Mfok"
                genai.configure(api_key=apikey)
                model = genai.GenerativeModel('gemini-pro')

                response = model.generate_content(question)
                return response.text

if __name__=='__main__':
        print(askgem("how are you gemini?"))