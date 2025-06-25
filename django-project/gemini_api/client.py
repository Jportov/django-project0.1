import google.generativeai as genai

genai.configure(api_key='AIzaSyD1_i-io7iAUE3QpFm186bFT--Gscd4V6g')

def get_car_description(model, brand, year):
    prompt = f"Crie uma descrição atrativa de venda para o carro {model} {brand} {year}, com no máximo 250 caracteres. Destaque pontos fortes como estado de conservação, desempenho ou economia."

    model = genai.GenerativeModel('gemini-2.5-flash')  # ou gemini-1.0-pro
    response = model.generate_content(prompt)

    return response.text.strip()
