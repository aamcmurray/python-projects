import os
import openai

def get_key(path):
  '''Code to retrieve the API key from a .txt file.'''
    with open(path, encoding='utf8') as f:
        lines = f.readlines()
        f.close()
    key=str(lines[0])
    return key

def input_query(query,maximum_tokens,key):
  '''Generalised query that accepts three arguments, the query, the maximum tokens to be spent on the response and the API key. ''' 
    openai.api_key = key
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": query}
      ],
        max_tokens=maximum_tokens
    )
    return completion

def role_play(query,maximum_tokens,key):
  ''' Function that role plays and responds in the style of a pirate'''
    openai.api_key = key
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
            {"role": "system","content": "You are an assistant that speaks like a pirate."}
        ],
        max_tokens=maximum_tokens
    )
    return completion

def sentiment(query,maximum_tokens,key):
  ''' Function that assesses the sentiment of input query, potentially useful for survey comment responses.'''
    openai.api_key = key
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
            {"role": "system","content": "You will be provided with a comment from a staff survey, and your task is to classify its sentiment as positive, neutral, or negative. Do not answer in complete sentences. Only provide your assessment."}
        ],
        max_tokens=maximum_tokens
    )
    return completion

def token_calculator(number_tokens):
  '''Back of the envelope token conversion (assuming 1 token is approx. 4 characters).'''
    approx_words = number_tokens*75/100
    print(number_tokens, 'tokens equates to approximately', approx_words, 'words.')
    
def get_message(request_output):
  ''' Retrieves the content of the message returned in the response.'''
    return request_output.choices[0].message.content

def get_token_data(request_output):
  ''' Retrieves token data relating to the response. '''
    x=request_output.usage.prompt_tokens
    y=request_output.usage.completion_tokens
    z=request_output.usage.total_tokens
    print('Prompt tokens:', x, '\n',
          'Completion tokens:', y, '\n',
          'total_tokens: ', z, '\n')
    return x,y,z

def get_finish_reason(request_output):
  ''' Function that returns the reason for finishing.'''
    return request_output.choices[0].finish_reason

def main():
  key_path='C:/PATH/TO/API/KEY/FILE_NAME_CONTAINING_KEY.txt'
  OPENAI_API_KEY=get_key(key_path)
  result=input_query('How far from the Earth is the Sun?', 100, OPENAI_API_KEY)
  get_message(result)
  get_token_data(result)
  input_query('Can you summarise linear regression?',500,OPENAI_API_KEY)
  role_play('Can you summarise linear regression?',500,OPENAI_API_KEY)
  sentiment('I dont enjoy being micromanaged, my work is ok but I do not feel respected',500,OPENAI_API_KEY)

if __name__ == "__main__":
  main()
