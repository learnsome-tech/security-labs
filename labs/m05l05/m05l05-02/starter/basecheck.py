import json

images = json.load(open('images.json'))
for image in images:
    extras = image['packages']
    print(image['name'], 'packages:', len(extras),
          'shell:', image['shell'], 'package manager:', image['manager'])
    print('  reachable tools:', ', '.join(extras))
small = min(images, key=lambda item: len(item['packages']))
print('smallest base:', small['name'])
