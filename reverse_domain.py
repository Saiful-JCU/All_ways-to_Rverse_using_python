site = 'www.programming-hero.com'
parts = site.split('.')
parts.reverse()
rev = '.'.join(parts)
print(rev)

# alternative
reverse = '.'.join(reversed(site.split('.')))
print(reverse)