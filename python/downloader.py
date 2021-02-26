from requests import get


for page in range(495, 972):
	main_url = f'https://content-delivery-service.savvasrealize.com/content-delivery-service/eps/prod-realize-reader/api/item/a458e8c7-00f1-4459-9692-0c589ff1361f/1/file/1011766/OPS/images/decorative_page_{page}_0.png'
	page_data = get(main_url).content
	with open(f'{page}.png', 'wb') as img:
		img.write(page_data)
