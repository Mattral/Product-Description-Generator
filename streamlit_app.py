import cohere
co = cohere.Client('{Tk1YrfGVYRLliKkd87SryJboA9E5h6AImryTZXgK}')
print('Enter your Product name:')
Product = input()
print('Enter Keywords:')
Keywords = input()
response = co.generate( 
  model='xlarge', 
  prompt='Given a product and keywords, this program will generate exciting product descriptions. Here are some examples:\n\nProduct: Chair\nKeywords: luxury, modern\nExciting Product Description: This modern luxury chair is a vision of comfort and essentialism. They are crafted to perfection. This chair can make any room look like a magazine cover. Indulge yourself or any lover of design with this upscale chair that is the perfect addition to any home, office, or work-space. Its durability can withstand the test of time. Come home to one today. You can also select the color you want to match your interior.\n--\nProduct: Mouse\nKeywords: bluetooth, lightweight\nExciting Product Description: Do you ever feel like your computer is too far away? Wouldn\'t it be amazing if you could use your computer from anywhere in your house? Well now you can with the new Bluetooth mouse. This sleek and stylish device has a range of up to 30 feet, meaning that you can go from surfing the web on your laptop to gaming on your desktop with ease. And because this mouse is so small and lightweight, it\'s easy to take with you wherever you go. So don\'t settle for anything less than the best, get yourself a Bluetooth mouse today!\n--\nProduct:'+Product+'\nKeywords:'+Keywords+'\nExciting Product Description:',
  
  max_tokens=150, 
  temperature=0.8, 
  k=0, 
  p=1, 
  frequency_penalty=0, 
  presence_penalty=0, 
  stop_sequences=["--"], 
  return_likelihoods='NONE') 
print('Prediction: {}'.format(response.generations[0].text)) 
