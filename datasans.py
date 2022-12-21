def sans(text, thread='datasans', show_script=False):
  """
  Anda harus menginstall library openai terlebih dahulu dengan cara "pip install openai"
  Untuk menjalankan fungsi pertama kali anda bisa meng-assign global variabel untuk api_key = [API-OpenAI-Anda], 
  jika tidak anda tetap akan diminta untuk memasukkan API-Key anda.
  
  thread: Untuk menjalankan thread baru, anda perlu meng-assign parameter thread='new' agar semua conversation sebelumnya direset. 
          Ini berguna jika anda baru pertama kali menggunakan fungsi ini atau jika anda ingin mengubah conversation untuk visualisasi/script yang baru
  show_script: Anda juga bisa meminta agar fungsi ini menampilkan script yang digenerate dengan cara mengatur parameter show_script=True, secara default show_script=False
  """
  import openai
  global api_key
  try:
    openai.api_key = api_key
  except:
    api_key = input('Masukkan API-KEY Open AI anda: ')
    openai.api_key = api_key

  global context
  if thread == 'new':
    context=''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text+". "+", write in python script",
        max_tokens=1024
  )
    output = response['choices'][0]['text']
    context = output
  else:
    try:
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=text+' dan perbaiki script: '+context.replace('\n',' ')+". "+", write all in python script.",
          max_tokens=1024
    )
      output = response['choices'][0]['text']
      context = output
    except:
      output = """print("Parameter thread belum diatur, jalankan chatGPT([text_anda], thread='new') ketika menjalankan fungsi untuk pertama kali atau ketika ingin mereset thread.")"""
  
  if show_script==True:
    return exec(output), print('Script:', output)
  else:
    return exec(output)
