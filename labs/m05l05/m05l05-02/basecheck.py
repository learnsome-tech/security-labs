# Application Security & Threat Modeling for Engineers — lesson m05l05 — Container Security: Minimal Bases And Non Root
# https://learnsome.tech/courses/security-course/watch?lesson=m05l05
# © LearnSome.tech
import json

images = json.load(open('images.json'))
for image in images:
    extras = image['packages']
    print(image['name'], 'packages:', len(extras),
          'shell:', image['shell'], 'package manager:', image['manager'])
    print('  reachable tools:', ', '.join(extras))
small = min(images, key=lambda item: len(item['packages']))
print('smallest base:', small['name'])
